from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, full_name, password=None):
        "Creates a new user with the given info."

        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have a username')

        if not full_name:
            raise ValueError('User must have a fullname')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            full_name=full_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, username, full_name, password=None):
        user = self.create_user(
            email,
            username=username,
            full_name=full_name,
            password=password
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, full_name, password=None):
        user = self.create_user(
            email,
            username=username,
            full_name=full_name,
            password=password
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img/users/images/', default='img/users/images/default.jpg')
    cover = models.ImageField(upload_to='img/users/covers/', default='img/users/covers/default.jpg')
    is_online = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'full_name']

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    @property
    def is_superuser(self):
        "Is the user superuser?"
        return self.is_admin and self.is_staff
