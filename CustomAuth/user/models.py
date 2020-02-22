from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, staff=False, admin=False):
        if not email:
            raise ValueError("email must be set")
        if not password:
            raise ValueError("password must be set")
       
        user_obj = self.model(
            email=self.normalize_email(email),
        )

        user_obj.password   = password
        user_obj.staff      = staff
        user_obj.admin      = admin

        user.save(using=self._db)
        return user_obj
    
    def create_superuser(self, email, password=None, staff=True, admin=True):
        return self.create_user(
            email,
            password=password,
            staff=staff,
            admin=admin
        )


class UserModel(AbstractBaseUser):
    email       = models.EmailField(max_length=255, unique=True, primary_key=True)
    active      = models.BooleanField(default=True)
    staff       = models.BooleanField(default=False)
    admin       = models.BooleanField(default=False)
    timestamp   = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email

    def get_name(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin