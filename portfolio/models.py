from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=120)
    photo = models.ImageField(upload_to='portfolio/')
    description = RichTextUploadingField()
    client = models.CharField(max_length=45)
    website = models.URLField(blank=True, null=True)
    complete_date = models.DateField()
    is_draft = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
