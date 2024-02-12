from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, 
                                        PermissionsMixin, 
                                        BaseUserManager
                                        )
from profiles_project import settings


#base user model customized
class UserModel(BaseUserManager):
    """Manager for user profile"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """create and save new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user
        

# custom user model
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """DB model for user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = UserModel()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """get full name"""
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        """returning representation of user"""
        return self.email

class ProfileFeedItems(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )

    status_text = models.CharField(max_length = 255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text