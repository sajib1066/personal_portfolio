# import modules
from django.db import models
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField

# create views here ...

# create author profile views
class AuthorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    photo = models.ImageField(upload_to='author/')
    about = models.TextField()
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = models.CharField(choices=gender_choice, max_length=5)
    facebook_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    skype_url = models.URLField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# create category views
class PostCategory(models.Model):
    name = models.CharField(max_length=120, unique=True)
    photo = models.ImageField(upload_to='category/')
    about = models.TextField()
    author = models.ForeignKey(AuthorProfile, on_delete=models.SET_NULL, null=True)
    is_draft = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# create tag views
class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    author = models.ForeignKey(AuthorProfile, on_delete=models.SET_NULL, null=True)
    is_draft = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# create post views
class Post(models.Model):
    title = models.CharField(max_length=245, unique=True)
    photo = models.ImageField(upload_to='post/')
    content = RichTextUploadingField()
    category = models.ForeignKey(PostCategory, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag)
    author = models.ForeignKey(AuthorProfile, on_delete=models.SET_NULL, null=True)
    is_draft = models.BooleanField(default=False)
    pub_date = models.DateField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
