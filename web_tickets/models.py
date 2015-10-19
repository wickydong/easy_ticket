from django.db import models

class UserAuth(models.Model):
    user = models.CharField(max_length=30)
    passwd = models.CharField(max_length=50)
    god = models.CharField(max_length=20)
    def __unicode__(self):
        return self.user

class Tickets(models.Model):
    user = models.CharField(max_length=30)
    tk_type = models.CharField(max_length=50)
    tk_msg = models.TextField()
    tk_time = models.DateTimeField(auto_now_add=True)
    answer = models.CharField(max_length=30,null=True,blank=True)
    answer_msg = models.TextField()
    answer_time = models.DateTimeField(auto_now=True)
