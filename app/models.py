from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db import models   
from django.urls import reverse
from tinymce import models as tinymce_models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class PostModel(models.Model):
    post_title = models.CharField(max_length=50, null=False)
    post_summery = models.TextField()
    post_body =  tinymce_models.HTMLField()
    post_image = models.ImageField(upload_to='post_images/', null=True )

    def __str__(self) -> str:
        return self.post_title
    
class CommentModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    comment_body = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.comment_body

class ContactModel(models.Model):
    Name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)
    phone_number = PhoneNumberField(blank = True)
    contact_body = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    Image = models.ImageField(null=True)

    def __str__(self) -> str:
        return self.contact_body

    