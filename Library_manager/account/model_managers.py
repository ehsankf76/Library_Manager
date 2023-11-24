from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, date_of_birth, email, phone_number, member_code, role, password=None):
        """
        Creates and saves a User with the given email, date of
        birth, first_name, last_name, created_time and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            email=self.normalize_email(email),
            phone_number=phone_number,
            member_code=member_code,
            role=role,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, date_of_birth, email, phone_number, member_code, role, password=None):
        """
        Creates and saves a superuser with the given username, email, date of
        birth, first_name, last_name, created_time, image and password.
        """
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            email=email,
            phone_number=phone_number,
            member_code=member_code,
            password=password,
            role=role,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user