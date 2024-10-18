import re

from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from self_assessment_educational_programs_storage.users.forms import (
    UserAdminChangeForm,
    UserAdminCreationForm,
)
from self_assessment_educational_programs_storage.users.models import (
    Course,
    Education,
    ProfessionalActivity,
    ProfessionalDevelopment,
    Qualification,
    Student,
    Teacher,
    TeacherFile, AcademicDegree, Author, Citation, Conference, StudentSupervision, ResearchProject,
    QualificationImprovement,
)

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

class AcademicDegreeInline(admin.TabularInline):  # Must inherit from TabularInline
    model = AcademicDegree
    extra = 1

class QualificationInline(admin.TabularInline):  # Must inherit from TabularInline
    model = Qualification
    extra = 1

class ProfessionalDevelopmentInline(admin.TabularInline):  # Must inherit from TabularInline
    model = ProfessionalDevelopment
    extra = 1

class ProfessionalActivityInline(admin.TabularInline):  # Must inherit from TabularInline
    model = ProfessionalActivity
    extra = 1

class EducationInline(admin.TabularInline):  # Must inherit from TabularInline
    model = Education
    extra = 1

class CourseInline(admin.TabularInline):  # Must inherit from TabularInline
    model = Course
    extra = 1

class TeacherFileInline(admin.TabularInline):  # Must inherit from TabularInline
    model = TeacherFile
    extra = 1

class CitationInline(admin.StackedInline):
    model = Citation
    extra = 1

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "last_name",
        "first_name",
        "middle_name",
        "faculty",
        "position",
        "experience_years",
        "is_main_job",
        "is_approved",
        "hire_date",
        "user",
    )
    search_fields = ("id", "last_name", "first_name", "middle_name", "faculty", "position")
    list_filter = ("is_approved", "is_main_job", "faculty", "hire_date")
    ordering = ("last_name", "first_name")
    filter_horizontal = ("department",)  # For many-to-many relationships
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "id",
                    "last_name",
                    "first_name",
                    "middle_name",
                    "hire_date",
                    "department",
                    "faculty",
                    "position",
                    "experience_years",
                    "academic_title",
                    "is_main_job",
                    "is_approved",
                    "user",
                )
            },
        ),
    )
    readonly_fields = ("id",)
    inlines = [
        AcademicDegreeInline,
        QualificationInline,  # Use the actual class, not the string
        ProfessionalDevelopmentInline,
        ProfessionalActivityInline,
        EducationInline,
        CourseInline,
        TeacherFileInline,
    ]

    actions = ['approve_teachers', 'disable_teachers', 'add_or_update_teachers_as_authors']

    def approve_teachers(self, request, queryset):
        # Filter out teachers that are already approved
        not_approved_teachers = queryset.filter(is_approved=False)

        # Check if there are teachers to approve
        if not_approved_teachers.exists():
            not_approved_teachers.update(is_approved=True)
            self.message_user(request, _("Selected teachers have been approved."))
        else:
            self.message_user(request, _("No teachers were approved."), level='warning')

    approve_teachers.short_description = _("Approve selected teachers")

    def disable_teachers(self, request, queryset):
        # Filter out teachers that are currently approved
        approved_teachers = queryset.filter(is_approved=True)

        # Check if there are teachers to disable
        if approved_teachers.exists():
            approved_teachers.update(is_approved=False)
            self.message_user(request, _("Selected teachers have been disabled."))
        else:
            self.message_user(request, _("No teachers were disabled."), level='warning')

    disable_teachers.short_description = _("Disable approval for selected teachers")

    def add_or_update_teachers_as_authors(self, request, queryset):
        for teacher in queryset:
            short_name = teacher.get_short_name()

            # Look for existing author by full name
            author = Author.objects.filter(
                last_name=teacher.last_name,
                first_name=teacher.first_name,
                middle_name=teacher.middle_name
            ).first()

            # If no match by full name, look for existing author by short name
            if not author:
                author = Author.objects.filter(
                    last_name=teacher.last_name,
                    first_name__startswith=teacher.first_name[0],
                    middle_name__startswith=teacher.middle_name[0] if teacher.middle_name else None
                ).first()

            # If author found, update their information; otherwise, create a new author
            if author:
                author.first_name = teacher.first_name
                author.middle_name = teacher.middle_name
                author.save()
            else:
                Author.objects.create(
                    last_name=teacher.last_name,
                    first_name=teacher.first_name,
                    middle_name=teacher.middle_name
                )

        self.message_user(request, "Selected teachers have been added or updated in authors.")

    add_or_update_teachers_as_authors.short_description = "Add or update selected teachers as authors"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # If the user is a superuser, allow access to all teachers
        if request.user.is_superuser:
            return qs
        # Otherwise, return only the logged-in user's teacher data
        return qs.filter(user=request.user)

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        # Allow the logged-in user to change their own data
        if obj is not None and obj.user == request.user:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        # Allow superusers to view anything
        if request.user.is_superuser:
            return True
        # Allow the logged-in user to view their own data
        if obj is not None and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        # Allow superusers to delete anything
        if request.user.is_superuser:
            return True
        # Allow the logged-in user to delete their own data
        if obj is not None and obj.user == request.user:
            return True
        return False

    def has_add_permission(self, request):
        # Restrict adding new teachers unless the user is a superuser
        return request.user.is_superuser


@admin.register(AcademicDegree)
class AcademicDegreeAdmin(admin.ModelAdmin):
    list_display = ['degree', 'date_awarded', 'dissertation_topic', 'teacher']
    search_fields = ("degree", "dissertation_topic")
    list_filter = ("date_awarded",)

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'text', 'code', 'date', 'teacher'
    )
    search_fields = ("name", "date")
    list_filter = ("name",)


@admin.register(ProfessionalDevelopment)
class ProfessionalDevelopmentAdmin(admin.ModelAdmin):
    list_display = ("teacher", "type", "date", "duration")
    search_fields = ("type",)
    list_filter = ("date",)


@admin.register(ProfessionalActivity)
class ProfessionalActivityAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'paragraph', 'get_linked_object', 'text', 'content_type')
    search_fields = ('teacher__last_name', 'paragraph')
    list_filter = ('teacher', 'paragraph')
    actions = ['set_citation_as_content_type']

    # Action to set Citation as content type for specific paragraphs
    def get_linked_object(self, obj):
        if obj.content_object:
            # Get the related model instance (like Citation)
            link = reverse("admin:%s_%s_change" % (
                obj.content_object._meta.app_label, obj.content_object._meta.model_name), args=[obj.object_id]
                           )
            return format_html('<a href="{}">Переглянути</a>', link)  # Display same text for all links
        return "No linked object"

    get_linked_object.short_description = "Об'єкт"


    # Action to set Citation as content type for specific paragraphs and create citation using parsed text
    def set_citation_as_content_type(self, request, queryset):
        citation_content_type = ContentType.objects.get_for_model(Citation)

        activities = queryset.filter(paragraph__in=['1', '3', '12'])

        for activity in activities:
            activity.content_type = citation_content_type

            # Parse the text to fill citation fields based on ДСТУ 8302:2015 structure
            citation = self.parse_citation_from_text(activity)

            # Check if the citation was successfully created (i.e., all required fields are present)
            if citation is not None:
                # Only set the object_id if a valid citation was returned
                activity.object_id = citation.id
                activity.save()

        self.message_user(request, "Citations were generated for the selected activities where valid data was found.")


    def parse_citation_from_text(self, activity):
        text = activity.text

        parsed_data = {
            'authors': [],
            'title': '',
            'publication_year': '',
            'publisher_name': '',
            'publication_city': '',
            'pages': '',
            'document_type': ''
        }

        # Pattern to extract authors (both in English and Ukrainian formats)
        authors_pattern = r'([А-ЯA-Z][а-яa-zA-Z]*\s+[А-ЯA-Z][а-яa-zA-Z]*\.*(?:\s+[А-ЯA-Z][а-яa-zA-Z]*\.*)?)'
        authors = re.findall(authors_pattern, text)
        parsed_data['authors'] = authors

        # Pattern to extract the title (everything between the last author and the first period)
        title_pattern = r'{}\.\s*([^\.]+)'.format(re.escape(authors[-1])) if authors else r'([^\.]+)\.'
        title_match = re.search(title_pattern, text)
        if title_match:
            parsed_data['title'] = title_match.group(1).strip()

        # Pattern to extract publication year
        year_pattern = r'\b(20\d{2}|19\d{2})\b'
        year_match = re.search(year_pattern, text)
        if year_match:
            parsed_data['publication_year'] = year_match.group(0)

        # Pattern to extract publisher name (after title and before year)
        publisher_pattern = r'([^—,]+)(?:\s*—)?\s*\b{}\b'.format(parsed_data['publication_year'])
        publisher_match = re.search(publisher_pattern, text)
        if publisher_match:
            parsed_data['publisher_name'] = publisher_match.group(1).strip()

        # Pattern to extract publication city (appears after publisher, before pages or year)
        city_pattern = r'—\s*([^,]+)\s*—'
        city_match = re.search(city_pattern, text)
        if city_match:
            parsed_data['publication_city'] = city_match.group(1).strip()

        # Pattern to extract pages (if any)
        pages_pattern = r'С\.\s*(\d+-?\d*)'
        pages_match = re.search(pages_pattern, text)
        if pages_match:
            parsed_data['pages'] = pages_match.group(1)

        # Determine document type based on keywords in the string
        if 'конференції' in text or 'тези' in text:
            parsed_data['document_type'] = 'conference'
        elif 'книга' in text or 'видання' in text:
            parsed_data['document_type'] = 'book'
        elif 'стаття' in text:
            parsed_data['document_type'] = 'article'
        else:
            parsed_data['document_type'] = 'other'

        if all([parsed_data.get('author'), parsed_data.get('title'), parsed_data.get('year')]):
            citation, created = Citation.objects.get_or_create(
                title=parsed_data['title'],
                publication_year=parsed_data['publication_year'],
                publisher_name=parsed_data['publisher_name'],
                publication_city=parsed_data['publication_city'],
                pages=parsed_data['pages'],
                document_type=parsed_data['document_type'],
            )

            # Add author details
            for author in parsed_data['authors']:
                short_name = self.convert_to_short_name(
                    author)  # Assuming you have a method to convert full name to short name
                author_obj, author_created = Author.objects.get_or_create(
                    full_name=author,
                    short_name=short_name
                )
                citation.authors.add(author_obj)  # Link author to the citation

            citation.save()


            return citation
        return None

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("teacher", "text")
    search_fields = ("text",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("teacher", "name")
    search_fields = ("name",)


@admin.register(TeacherFile)
class TeacherFileAdmin(admin.ModelAdmin):
    list_display = ("teacher", "file", "uploaded_at")
    search_fields = ("teacher__last_name", "teacher__first_name")
    list_filter = ("uploaded_at",)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', "short_name")
    search_fields = ("last_name", "first_name", "short_name")
    ordering = ("last_name", "first_name")


@admin.register(Citation)
class CitationAdmin(admin.ModelAdmin):
    list_display = ('title', 'document_type', 'publication_year', 'publisher_name', 'publication_city')
    filter_horizontal = ("authors",)

    fieldsets = (
        ('Автори', {
            'fields': ('title', 'authors')
        }),
        ('Деталі публікації', {
            'fields': ('publication_year', 'publisher_name', 'publication_city'),
        }),
        ('Метадані', {
            'fields': ('pages', 'document_type'),
        }),
    )
    

@admin.register(QualificationImprovement)
class QualificationImprovementAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'teacher', 'organizer', 'start_date', 'end_date', 'certificate')
    search_fields = ('course_name', 'organizer', 'certificate')
    ordering = ('start_date', 'course_name')


@admin.register(ResearchProject)
class ResearchProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'teacher', 'organizer', 'start_date', 'end_date', 'results')
    search_fields = ('project_name', 'organizer')
    ordering = ('start_date', 'project_name')


@admin.register(StudentSupervision)
class StudentSupervisionAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'teacher', 'work_type', 'work_topic', 'start_date', 'defense_date')
    search_fields = ('student_name', 'work_topic')
    ordering = ('start_date', 'student_name')


@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'level', 'date', 'location', 'report_topic')
    search_fields = ('name', 'location', 'report_topic')
    ordering = ('date', 'name')
