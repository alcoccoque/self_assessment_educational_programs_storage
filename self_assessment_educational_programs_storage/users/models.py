from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Custom user model for educational programs storage.
    """

    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = models.CharField(_("Ім'я"), max_length=100, blank=True)
    last_name = models.CharField(_("Прізвище"), max_length=100, blank=True)
    middle_name = models.CharField(_("По батькові"), max_length=100, blank=True)

    def get_absolute_url(self):
        """Get url for user's detail view."""
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
        max_length=15,
        null=True,
        blank=True,
        verbose_name="Унікальний номер у системі",
        unique=True,
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


class Teacher(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Ім'я")
    last_name = models.CharField(max_length=100, verbose_name="Прізвище")
    middle_name = models.CharField(max_length=100, blank=True, verbose_name="По батькові")
    hire_date = models.DateField(null=True, blank=True, verbose_name="Дата прийняття на роботу")
    department = models.ManyToManyField("general_information.StructuralSubdivision", verbose_name="Структурний підрозділ")
    faculty = models.CharField(max_length=255, blank=True, verbose_name="Факультет")
    position = models.CharField(max_length=600, blank=True, verbose_name="Посада")
    experience_years = ArrayField(
        models.IntegerField(),  # Stores list of integers
        default=list,
        verbose_name="Стаж роботи"
    )
    academic_title = models.CharField(max_length=255, blank=True, verbose_name="Вчене звання")
    is_main_job = models.BooleanField(default=False, verbose_name="Основне місце роботи")
    is_approved = models.BooleanField(default=False, verbose_name="Підтверджений викладач")
    user = models.OneToOneField("users.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="teacher")

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    def get_short_name(self):
        return f"{self.last_name} {self.first_name[0]}. {self.middle_name[0]}."


class AcademicDegree(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="academic_degrees")
    degree = models.CharField(max_length=600, verbose_name="Назва наукового ступеня")
    details = models.TextField(null=True, blank=True, verbose_name="Деталі")
    date_awarded = models.DateField(null=True, blank=True, verbose_name="Дата присудження або код спеціальності")
    dissertation_topic = models.TextField(null=True, blank=True, verbose_name="Тема дисертації")

    def __str__(self):
        return f"{self.degree} - {self.teacher}"

class Qualification(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="qualifications")
    name = models.CharField(max_length=600, verbose_name="Назва кваліфікації")
    text = models.TextField(blank=True, verbose_name="Текст кваліфікації")
    code = models.CharField(max_length=100, verbose_name="Код кваліфікації")
    date = models.DateField(null=True, blank=True, verbose_name="Дата присудження")

    def __str__(self):
        return f"{self.name} - {self.teacher}"


class ProfessionalDevelopment(models.Model):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="professional_development"
    )
    type = models.CharField(
        max_length=600,
        null=True,
        blank=True,
        verbose_name="Тип (сертифікат, свідоцтво)",
    )
    details = models.TextField(verbose_name="Деталі")
    date = models.DateField(null=True, blank=True, verbose_name="Дата")
    duration = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Тривалість"
    )

    def __str__(self):
        return f"{self.type} - {self.teacher}"


class ProfessionalActivity(models.Model):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="professional_activities"
    )
    paragraph = models.CharField(
        max_length=3,
        blank=True,
        verbose_name="Види і результати професійної діяльності",
    )
    text = models.TextField(verbose_name="Текст")

    # GenericForeignKey fields for dynamic linking
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"Activity {self.paragraph} - {self.teacher}"


# Example structured model: Citation
class Author(models.Model):
    last_name = models.CharField(max_length=100, verbose_name="Прізвище")
    first_name = models.CharField(max_length=100, verbose_name="Ім'я")
    middle_name = models.CharField(max_length=100, blank=True, verbose_name="По-батькові")
    short_name = models.CharField(max_length=255, blank=True, verbose_name="Скорочене ім'я")

    def __str__(self):
        return f"{self.last_name}, {self.first_name} {self.middle_name or ''}".strip()

    def get_short_name(self):
        return f"{self.last_name} {self.first_name[0]}. {self.middle_name[0]}." if self.middle_name else self.short_name


class Citation(models.Model):
    authors = models.ManyToManyField(Author, related_name='citations', verbose_name="Автори")
    title = models.CharField(
        max_length=500,
        verbose_name="Назва публікації або діяльності",
        help_text="Назва публікації або діяльності"
    )
    publication_year = models.CharField(
        max_length=4,
        verbose_name="Рік публікації",
        help_text="Рік, коли було опубліковано або здійснено діяльність"
    )
    publisher_name = models.CharField(
        max_length=255,
        verbose_name="Назва видавництва або організації",
        blank=True,
        help_text="Назва організації або видавництва, якщо застосовується"
    )
    publication_city = models.CharField(
        max_length=100,
        verbose_name="Місто публікації",
        blank=True,
        help_text="Місто, де відбулася діяльність або публікація"
    )
    pages = models.CharField(
        max_length=50,
        verbose_name="Сторінки",
        blank=True,
        help_text="Сторінки, якщо це друкований документ"
    )
    document_type = models.CharField(
        max_length=100,
        verbose_name="Тип документа",
        choices=[
            ('book', 'Книга'),
            ('article', 'Стаття'),
            ('conference', 'Матеріали конференції'),
            ('patent', 'Патент'),
            ('other', 'Інше')
        ],
        help_text="Тип джерела для цитування"
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"



class Education(models.Model):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="education"
    )
    text = models.CharField(max_length=600, verbose_name="Освіта")

    def __str__(self):
        return f"{self.text})"


class Course(models.Model):  # Standardizing as Course (instead of Subject)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="courses"
    )
    name = models.CharField(max_length=600, verbose_name="Навчальна дисципліна")

    def __str__(self):
        return f"{self.name} - {self.teacher}"


class TeacherFile(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File for {self.teacher}"


class Conference(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=255)
    report_topic = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class QualificationImprovement(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    certificate = models.CharField(max_length=255)

    def __str__(self):
        return self.course_name


class ResearchProject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    results = models.TextField()

    def __str__(self):
        return self.project_name


class StudentSupervision(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    work_type = models.CharField(max_length=100)
    work_topic = models.CharField(max_length=255)
    start_date = models.DateField()
    defense_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.student_name
