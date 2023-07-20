from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core import exceptions


ROLE_OPTIONS = [(i, i) for i in ["User", "Admin"]]

class User(AbstractUser):
    role = models.CharField(max_length=32, choices=ROLE_OPTIONS, default="User")

    @property
    def initials_picture_url(self):
        return f"https://ui-avatars.com/api/?name={self}"
    
    @property
    def all_permissions(self):
        return list(self.get_all_permissions())
    
    def save(self, *args, **kwargs):
        # harshed password always equals 88 charecters
        if len(self.password) != 88:
            self.set_password(self.password)
        return super().save(*args, **kwargs)
    
    def get_form_options(self):
        return {
            "group": {
                "choices": [(i.pk, str(i)) for i in Group.objects.all()]
            },
            "role": {
                "choices": ROLE_OPTIONS
            },
            "user_permissions": {
                "choices": [(i.pk, str(i)) for i in Permission.objects.all()]
            }
        }


class Department(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=128)
    date_of_registration = models.DateField()
    registration_number = models.CharField(max_length=128)
    address = models.TextField(max_length=512, blank=True, null=True)
    departments = models.ManyToManyField(Department, blank=True)
    contact_person = models.CharField(max_length=128)
    contact_phone = models.CharField(max_length=128)
    email_address = models.EmailField(max_length=128)

    def __str__(self) -> str:
        return self.name
    
    @property
    def department_names(self):
        return ", ".join([i.name for i in self.departments.all()])
    
    @property
    def number_of_employees(self):
        return Employment.objects.filter(company=self, date_left=None).count()
    
    def get_form_options(self):
        return {
            "departments": {
                "choices": [(i.pk, str(i)) for i in Department.objects.all()]
            }
        }


class Employee(models.Model):
    name = models.CharField(max_length=128)
    id_number = models.CharField(max_length=128, unique=True)
    contact_phone = models.CharField(max_length=128)
    email_address = models.EmailField(max_length=128)
    trade = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name


class Employment(models.Model):
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    role = models.CharField(max_length=128)
    date_started = models.DateField()
    date_left = models.DateField(blank=True, null=True)
    duties = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"{self.employee} at {self.company}"
    
    @property
    def data(self):
        return {
            "department": str(self.department),
            "employee": str(self.employee),
            "company": str(self.company),
        }
    
    def validate_department(self):
        if self.company.departments.filter(id=self.department_id).exists():
            raise exceptions.ValidationError("Company does not have the selected department")
    
    def validate_dates(self):
        if self.date_left and (self.date_left < self.date_started):
            raise exceptions.ValidationError("Start and end dates don't make sense!")

    def clean(self) -> None:
        print("Cleaning")
        super().clean()
        self.validate_department()
        self.validate_dates()
    
    def get_form_options(self):
        return {
            "department": {
                "choices": [(i.pk, str(i)) for i in Department.objects.all()]
            },
            "employee": {
                "choices": [(i.pk, str(i)) for i in Employee.objects.all()]
            },
            "company": {
                "choices": [(i.pk, str(i)) for i in Company.objects.all()]
            },
        }


