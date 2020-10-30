from django.db import models
from django.contrib.auth.models import  AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import  PermissionsMixin
# Create your models here.
class UserProfileManager(BaseUserManager):
    """ Manager User similar """
    def create_user(self,email ,name ,password=None):
        pass
        if not email :
            raise ValueError("Input email please")
        email = self.normalize_email(email)
        user = self.model(email=email ,name=name)
        user.set_password(password)
        user.save(using =self._db)
        return user
    
    def create_superuser(self, email, name ,password):
        """ create superuser"""
        user =self.create_user(email =email,name =name ,password=password)
        user.is_superuser =True
        user.is_staff =True
        user.save(using =self._db)
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    
    email =models.EmailField(blank =True ,max_length=250,unique =True)
    name =models.CharField(max_length=200,null =True)
    is_active =models.BooleanField(default =True)
    is_staff =models.BooleanField(default =False)
    
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['name']
    
    def __str__(self):
        return self.email
    
    def get_name(self):
        return self.name
    
