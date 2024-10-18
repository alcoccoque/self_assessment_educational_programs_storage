from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from cryptography.x509.verification import Subject
from django import forms
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import (
    Course,
    Education,
    ProfessionalActivity,
    ProfessionalDevelopment,
    Qualification,
    Teacher,
    TeacherFile, AcademicDegree, StudentSupervision, ResearchProject, QualificationImprovement, Conference,
)

User = get_user_model()


def link_user_to_teacher(user):
    """
    Try to link a user to an existing teacher profile based on their full name.
    """
    teacher = Teacher.objects.filter(
        first_name=user.first_name,
        last_name=user.last_name,
        middle_name=user.middle_name,
    ).first()

    if teacher and teacher.user is None:
        teacher.user = user
        teacher.save()
        return teacher
    return None


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("Це ім'я вже використовується.")}
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign-up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """

    first_name = forms.CharField(max_length=30, label="Ім'я", required=True)
    last_name = forms.CharField(max_length=30, label="Прізвище", required=True)
    middle_name = forms.CharField(max_length=30, label="По батькові", required=True)
    is_teacher = forms.BooleanField(required=False, label="Викладач")

    def clean_username(self):
        # Check if the username already exists
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise ValidationError("Це ім'я вже використовується.")
        return username

    def clean_email(self):
        # Check if the email already exists
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Це пошта вже використовується.")
        return email

    def save(self, request):
        user = super(UserSignupForm, self).save(request)

        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.middle_name = self.cleaned_data.get("middle_name")

        user.save()

        linked_teacher = link_user_to_teacher(user)
        if linked_teacher:
            # Optionally, you can display a message or handle linking logic further
            pass

        if self.cleaned_data.get("is_teacher") and not linked_teacher:
            Teacher.objects.create(
                first_name=user.first_name,
                last_name=user.last_name,
                middle_name=user.middle_name,
                user=user,
            )

        return user


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when a user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """


class TeacherForm(forms.ModelForm):
    first_name = forms.CharField(label="Ім'я", max_length=100, required=True)
    last_name = forms.CharField(label="Прізвище", max_length=100, required=True)
    middle_name = forms.CharField(label="По батькові", max_length=100, required=False)

    class Meta:
        model = Teacher
        fields = ["position", "experience_years"]

    def save(self, commit=True):
        teacher = super(TeacherForm, self).save(commit=False)
        # Update the related user's name fields
        teacher.user.first_name = self.cleaned_data["first_name"]
        teacher.user.last_name = self.cleaned_data["last_name"]
        teacher.user.middle_name = self.cleaned_data["middle_name"]

        if commit:
            teacher.save()
            teacher.user.save()

        return teacher


class AcademicDegreeForm(forms.ModelForm):
    class Meta:
        model = AcademicDegree
        fields = ['degree', 'details', 'date_awarded', 'dissertation_topic']

class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = ['name', 'text', 'code', 'date']


class ProfessionalDevelopmentForm(forms.ModelForm):
    class Meta:
        model = ProfessionalDevelopment
        fields = ["type", "details", "date", "duration"]


class ProfessionalActivityForm(forms.ModelForm):
    class Meta:
        model = ProfessionalActivity
        fields = ["paragraph", "text"]


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ["text"]


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["name"]


class TeacherFileForm(forms.ModelForm):
    OVERWRITE_APPEND_CHOICES = [
        ('overwrite', 'Перезаписати дані'),
        ('append', 'Додати дані'),
    ]

    overwrite_or_append = forms.ChoiceField(
        choices=OVERWRITE_APPEND_CHOICES,
        widget=forms.RadioSelect,
        label="Вибрати дію"
    )

    class Meta:
        model = TeacherFile
        fields = ['file', 'overwrite_or_append']


class ConferenceForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ['teacher', 'name', 'level', 'date', 'location', 'report_topic']


class QualificationImprovementForm(forms.ModelForm):
    class Meta:
        model = QualificationImprovement
        fields = ['teacher', 'course_name', 'organizer', 'start_date', 'end_date', 'certificate']


class ResearchProjectForm(forms.ModelForm):
    class Meta:
        model = ResearchProject
        fields = ['teacher', 'project_name', 'organizer', 'start_date', 'end_date', 'results']


class StudentSupervisionForm(forms.ModelForm):
    class Meta:
        model = StudentSupervision
        fields = ['teacher', 'student', 'work_type', 'work_topic', 'start_date', 'defense_date']
