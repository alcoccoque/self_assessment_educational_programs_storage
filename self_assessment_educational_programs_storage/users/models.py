from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for Self assessment educational programs storage.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True, verbose_name="День народження")
    phone_number = models.CharField(
        max_length=15, blank=True, verbose_name="Номер телефона"
    )
    address = models.CharField(
        max_length=255, blank=True, verbose_name="Домашня адреса"
    )

    class Meta:
        abstract = True


class Student(UserProfile):
    class StudentType(models.TextChoices):
        BACHELOR = 1, _("Бакалавр")
        MASTER = 2, _("Магістр")
        POSTGRADUATE = 3, _("Аспірант")

    student_id = models.CharField(
        max_length=15, verbose_name="Унікальний номер у системі", unique=True
    )
    enrollment_date = models.DateField(
        verbose_name="Дата вступу в заклад освіти",
    )
    student_type = models.IntegerField(
        choices=StudentType.choices,
        verbose_name="Освітній ступінь",
    )

    class Meta:
        db_table = "student"
        verbose_name = "Студент"
        verbose_name_plural = "Студенти"


class Teacher(UserProfile):
    teacher_id = models.CharField(
        max_length=15, verbose_name="Унікальний номер у системі", unique=True
    )
    hire_date = models.DateField(
        verbose_name="Дата прийняття на роботу",
    )
    department = models.ManyToManyField(
        "general_information.StructuralSubdivision",
        verbose_name="Структурний підрозділ",
        help_text="Структурний підрозділ (кафедра або інший підрозділ), відповідальний за реалізацію ОП",
    )

    class Meta:
        db_table = "Teacher"
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"

    def __str__(self):
        return f"{self.teacher_id} {self.user.get_full_name()}"
