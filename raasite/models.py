from django.db import models
from django.contrib import admin

# Create your models here.
# Member
class Member(models.Model):
    lastname = models.CharField(max_length = 30)
    firstname = models.CharField(max_length = 30)
    photo_url = models.CharField(max_length = 200)
    major = models.CharField(max_length = 30)
    grade = models.CharField(max_length = 30)
    position = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    intro = models.TextField()

class MemberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname')

admin.site.register(Member,MemberAdmin)
