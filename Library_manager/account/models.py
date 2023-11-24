from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .model_managers import UserManager
from django.template.defaultfilters import slugify


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    date_of_birth = models.DateField()
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    phone_number = models.CharField(verbose_name="phone number", max_length=10, null=True, blank=True, unique=True)
    slug = models.CharField(max_length=50, unique=True, editable=False)
    created_time = models.DateTimeField(auto_now_add=True)
    member_code = models.CharField(verbose_name="member code", max_length=10, null=True, blank=True, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('member', 'Member'),
    )
    role = models.CharField(default='member', max_length=20, choices=ROLE_CHOICES)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number", "member_code", "first_name", "last_name", "date_of_birth", "role"]

    def __str__(self):
        return f"{self.email} - {self.member_code}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # only staff members have permission
        return self.is_staff
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.member_code)
        super(User, self).save(*args, **kwargs)

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin