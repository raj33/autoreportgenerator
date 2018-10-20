from django.db import models
from datetime import datetime
from django.contrib import admin
from django.db import models
from django.utils.html import format_html
class Question(models.Model):

    crn = models.CharField('CRN',max_length=200,null='True')
    distr = models.CharField('District',max_length=200,null='True',blank=True)
    name = models.CharField('Name',max_length=200,null='True')
    phone=models.IntegerField('Phone',null='True')
    category=models.IntegerField('Category',null='True')
    typee=models.CharField('Type',null='True',max_length=200)
    ulbname=models.CharField('ulb',null='True',max_length=200)
    status=models.CharField('Status',null='True',max_length=200,default='Pending')
    frm = models.DateTimeField('Registed On',default=datetime.now, blank=True)
    to = models.DateTimeField('Completed On',blank=True,null='True')
    def __str__(self):
        return self.crn
     
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #choice_text = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
