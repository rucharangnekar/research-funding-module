from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Myusr(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cat = models.IntegerField(default=0)


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)	
    student1 =  models.CharField(max_length=150,null=True)
    student2 =  models.CharField(max_length=150,null=True)
    student3 =  models.CharField(max_length=150,null=True)
    t_id = models.IntegerField(default=0,null=True)
    s_id = models.IntegerField(default=0,null=True)
    g_id = models.IntegerField(default=1,null=True)
    title = models.CharField(max_length=150,null=True)
    abstract = models.CharField(max_length=250,null=True)
    amt = models.IntegerField(null=True)
    fund_approved = models.CharField(max_length=150,null=True)
    stage = models.IntegerField(null=True)
    status=models.IntegerField(default=5,null=True)
    check=models.IntegerField(default=0)
    rej= models.CharField(max_length=250,null=True)
 
class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher_id = models.IntegerField(null=True)
