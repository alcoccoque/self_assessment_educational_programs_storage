from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView

from .forms import TeacherFileForm, TeacherForm
from .models import (
    Course,
    Education,
    ProfessionalActivity,
    ProfessionalDevelopment,
    Qualification,
    Teacher, AcademicDegree,
)
from .parsers import parse_docx

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


def teacher_upload(request):
    if request.method == "POST":
        form = TeacherFileForm(request.POST, request.FILES)
        if form.is_valid():
            teacher_file = form.save(commit=False)
            teacher_file.teacher = request.user.teacher  # Link the current teacher
            teacher_file.save()

            # Extract and parse the file contents
            file_path = teacher_file.file.path
            parsed_data_list = parse_docx(file_path)

            # Get the user's choice: 'overwrite' or 'append'
            overwrite_or_append = form.cleaned_data['overwrite_or_append']

            # Loop over each teacher data found in the document
            for parsed_data in parsed_data_list:
                full_name = parsed_data["full_name"]

                # Check if a teacher with this full name exists
                existing_teacher = Teacher.objects.filter(
                    first_name=full_name["first_name"],
                    last_name=full_name["last_name"],
                    middle_name=full_name.get("middle_name", "")
                ).first()

                if existing_teacher:
                    if request.user.teacher == existing_teacher:
                        # Apply 'overwrite' or 'append' logic for current user
                        if overwrite_or_append == 'overwrite':
                            # Overwrite the existing teacher's data
                            overwrite_teacher_data(existing_teacher, parsed_data)
                        else:
                            # Append to the existing teacher's data
                            append_teacher_data(existing_teacher, parsed_data)
                    else:
                        # For other users, always append data
                        append_teacher_data(existing_teacher, parsed_data)
                else:
                    # Create a new teacher record if not found
                    create_new_teacher(parsed_data)

            teacher_pk = request.user.teacher.pk
            return redirect("users:teacher_detail", pk=teacher_pk)

    else:
        form = TeacherFileForm()
    return render(request, "teacher/teacher_upload.html", {"form": form})

# Helper function to overwrite existing teacher data
def overwrite_teacher_data(teacher, parsed_data):
    teacher.first_name = parsed_data["full_name"].get("first_name", teacher.first_name)
    teacher.last_name = parsed_data["full_name"].get("last_name", teacher.last_name)
    teacher.middle_name = parsed_data["full_name"].get("middle_name", teacher.middle_name)

    # Overwrite other fields
    teacher.position = parsed_data.get("position", teacher.position)
    teacher.academic_title = parsed_data.get("justification").get("academicTitle", teacher.academic_title)
    teacher.experience_years = parsed_data.get("experience", teacher.experience_years)
    teacher.is_main_job = parsed_data.get("is_main_job", teacher.is_main_job)
    teacher.faculty = parsed_data.get("faculty", teacher.faculty)

    teacher.save()

    # Overwrite courses
    Course.objects.filter(teacher=teacher).delete()
    for course_name in parsed_data.get("courses", []):
        Course.objects.create(name=course_name, teacher=teacher)

    # Overwrite academic degrees
    AcademicDegree.objects.filter(teacher=teacher).delete()
    for degree in parsed_data["justification"].get("academicDegree", []):
        AcademicDegree.objects.create(
            teacher=teacher,
            degree=degree["degree"],
            details=degree["specialty"],
            dissertation_topic=degree.get("dissertation_topic", ""),
            date_awarded=degree.get("date", None),
        )

    # Overwrite qualifications
    Qualification.objects.filter(teacher=teacher).delete()
    for qualification in parsed_data.get("qualification", []):
        Qualification.objects.create(
            teacher=teacher,
            name=qualification["name"],
            text=qualification.get("text", ""),
            code=qualification.get("code", None),
            date=qualification.get("date", ""),
        )

    # Overwrite professional development
    ProfessionalDevelopment.objects.filter(teacher=teacher).delete()
    for development in parsed_data["justification"].get("professionalDevelopment", []):
        ProfessionalDevelopment.objects.create(
            teacher=teacher,
            type=development["type"],
            details=development["details"],
            date=development.get("date", None),
            duration=development.get("duration", ""),
        )

    # Overwrite professional activities
    ProfessionalActivity.objects.filter(teacher=teacher).delete()
    for activity in parsed_data["justification"].get("professionalActivity", []):
        ProfessionalActivity.objects.create(
            teacher=teacher,
            paragraph=activity.get("paragraph", ""),
            text=activity["text"],
        )

    # Overwrite education
    Education.objects.filter(teacher=teacher).delete()
    for education_entry in parsed_data["justification"].get("education", []):
        Education.objects.create(teacher=teacher, text=education_entry)


# Helper function to append data to existing teacher profile
def append_teacher_data(teacher, parsed_data):
    teacher.first_name = parsed_data["full_name"].get("first_name", teacher.first_name)
    teacher.last_name = parsed_data["full_name"].get("last_name", teacher.last_name)
    teacher.middle_name = parsed_data["full_name"].get("middle_name", teacher.middle_name)

    # Overwrite other fields
    teacher.position = parsed_data.get("position", teacher.position)
    teacher.academic_title = parsed_data.get("justification").get("academicTitle", teacher.academic_title)
    teacher.experience_years = parsed_data.get("experience", teacher.experience_years)
    teacher.is_main_job = parsed_data.get("is_main_job", teacher.is_main_job)
    teacher.faculty = parsed_data.get("faculty", teacher.faculty)

    teacher.save()

    # Append courses
    for course_name in parsed_data.get("courses", []):
        Course.objects.get_or_create(name=course_name, teacher=teacher)

    # Append academic degrees
    for degree in parsed_data["justification"].get("academicDegree", []):
        AcademicDegree.objects.get_or_create(
            teacher=teacher,
            degree=degree["degree"],
            details=degree["specialty"],
            dissertation_topic=degree.get("dissertation_topic", ""),
            date_awarded=degree.get("date", None),
        )

    # Append qualifications
    for qualification in parsed_data.get("qualification", []):
        Qualification.objects.get_or_create(
            teacher=teacher,
            name=qualification["name"],
            text=qualification.get("text", ""),
            code=qualification.get("code", None),
            date=qualification.get("date", ""),
        )

    # Append professional development
    for development in parsed_data["justification"].get("professionalDevelopment", []):
        ProfessionalDevelopment.objects.get_or_create(
            teacher=teacher,
            type=development["type"],
            details=development["details"],
            date=development.get("date", None),
            duration=development.get("duration", ""),
        )

    # Append professional activities
    for activity in parsed_data["justification"].get("professionalActivity", []):
        ProfessionalActivity.objects.get_or_create(
            teacher=teacher,
            paragraph=activity.get("paragraph", ""),
            text=activity["text"],
        )

    # Append education
    for education_entry in parsed_data["justification"].get("education", []):
        Education.objects.get_or_create(teacher=teacher, text=education_entry)


# Helper function to create a new teacher
def create_new_teacher(parsed_data):
    new_teacher = Teacher.objects.create(
        first_name=parsed_data["full_name"]["first_name"],
        last_name=parsed_data["full_name"]["last_name"],
        middle_name=parsed_data["full_name"].get("middle_name", ""),
        position=parsed_data.get("position"),
        experience_years=parsed_data.get("experience", 0),
        academic_title=parsed_data["justification"].get("academicTitle", ""),
        is_main_job=parsed_data.get("is_main_job", False),
        faculty=parsed_data.get("faculty", ""),
        user=None,
        is_approved=False,
    )

    # Add courses
    for course_name in parsed_data.get("courses", []):
        Course.objects.get_or_create(name=course_name, teacher=new_teacher)

    # Add academic degrees
    for degree in parsed_data["justification"].get("academicDegree", []):
        AcademicDegree.objects.get_or_create(
            teacher=new_teacher,
            degree=degree["degree"],
            details=degree["specialty"],
            dissertation_topic=degree.get("dissertation_topic", ""),
            date_awarded=degree.get("date", None),
        )

    # Add qualifications
    for qualification in parsed_data.get("qualification", []):
        Qualification.objects.get_or_create(
            teacher=new_teacher,
            name=qualification["name"],
            text=qualification.get("text", ""),
            code=qualification.get("code", None),
            date=qualification.get("date", ""),
        )

    # Add professional development
    for development in parsed_data["justification"].get("professionalDevelopment", []):
        ProfessionalDevelopment.objects.get_or_create(
            teacher=new_teacher,
            type=development["type"],
            details=development["details"],
            date=development.get("date", None),
            duration=development.get("duration", ""),
        )

    # Add professional activities
    for activity in parsed_data["justification"].get("professionalActivity", []):
        ProfessionalActivity.objects.get_or_create(
            teacher=new_teacher,
            paragraph=activity.get("paragraph", ""),
            text=activity["text"],
        )

    # Add education
    for education_entry in parsed_data["justification"].get("education", []):
        Education.objects.get_or_create(teacher=new_teacher, text=education_entry)


def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    qualifications = teacher.qualifications.all()
    academic_degrees = teacher.academic_degrees.all()
    professional_development = teacher.professional_development.all()
    professional_activities = teacher.professional_activities.all()
    education = teacher.education.all()
    courses = teacher.courses.all()

    context = {
        'teacher': teacher,
        'qualifications': qualifications,
        'academic_degrees': academic_degrees,
        'professional_development': professional_development,
        'professional_activities': professional_activities,
        'education': education,
        'courses': courses,
    }

    return render(request, 'teacher/teacher_detail.html', context)


@login_required
def teacher_edit(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)

    # Ensure the user is editing their own profile
    # if request.user != teacher.user:

    if request.user == teacher.user:
        return redirect('users:teacher_detail', pk=pk)

    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('users:teacher_detail', pk=teacher.pk)
    else:
        form = TeacherForm(instance=teacher)

    return render(request, 'teacher/teacher_edit.html', {'form': form, 'teacher': teacher})

