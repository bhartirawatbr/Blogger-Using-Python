from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


#https://docs.djangoproject.com/en/1.9/topics/db/managers/
class Profile(models.Model):
    GENDER_STATUS = (("female",_("Female")),("male",_("Male")))
    user = models.ForeignKey(User)
    contact = models.CharField(unique=True,max_length=100,null=True)
    image = models.ImageField(upload_to=user_directory_path,blank=True, null=True)
    website = models.URLField(blank=True)
    gender = models.SmallIntegerField(choices=GENDER_STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

    def __unicode__(self):
        return str(self.contact)

class Category(models.Model):
    STATUS_CHOICE = ((0,'Inactive'),(1,'active'),(2,'Delete'))
    name = models.CharField(max_length=500)
    status = models.SmallIntegerField(choices=STATUS_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserBlog(models.Model):
    PUBLIC_CHOICE = ((0,'False'),(1,'True'))
    STATUS_CHOICE = ((0,'Inactive'),(1,'active'),(2,'Delete'))
    user = models.ForeignKey(User)
    title = models.CharField(max_length=500, blank=False)
    category = models.ForeignKey('Category')
    description = models.TextField(max_length=1000,blank=True,null=True)
    is_publish = models.SmallIntegerField(choices=PUBLIC_CHOICE)
    status = models.SmallIntegerField(choices=STATUS_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(User)
    blog = models.ForeignKey('UserBlog')
    description = models.TextField(max_length=1000,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Rating(models.Model):
    user = models.ForeignKey(User)
    blog = models.ForeignKey('UserBlog')
    rating = models.FloatField(max_length=1000,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserToken(models.Model):
    owner = models.OneToOneField(User, unique=True,related_name='owner')
    token = models.CharField(max_length=200)