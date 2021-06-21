from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class BlogModel(models.Model):
    title = models.CharField(max_length = 140)
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    publish_date = models.DateField(auto_now_add = True)
    short_desc = models.TextField(max_length = 1024)
    text = RichTextUploadingField()
    
    def __str__(self):
        return self.title
    

class AboutModel(models.Model):
    text = RichTextUploadingField()
    
    def __str__(self):
        strid = str(self.id)
        return strid
    

    
    
