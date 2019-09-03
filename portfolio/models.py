from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=45)
    is_draft = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    title = models.CharField(max_length=120)
    portfolio_type = models.CharField(max_length=45)
    photo = models.ImageField(upload_to='portfolio/')
    description = RichTextUploadingField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    client = models.CharField(max_length=45)
    website = models.URLField(blank=True, null=True)
    complete_date = models.DateField()
    is_draft = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
