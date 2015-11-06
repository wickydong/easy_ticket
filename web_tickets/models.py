from django.db import models

class UserAuth(models.Model):
    user = models.CharField(max_length=30)
    passwd = models.CharField(max_length=50)
    god = models.CharField(max_length=20)
    def __unicode__(self):
        return self.user

class AllForm(models.Model):
    create_time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=30)
    howtime = models.CharField(max_length=30,null=True)
    msg = models.TextField()
    qus = models.TextField(null=True)
    sys = models.CharField(max_length=30,null=True)
    conf = models.CharField(max_length=50,null=True)
    over_time = models.DateTimeField(auto_now_add=True)
    make_user = models.CharField(max_length=30,null=True)
    over_user = models.ManyToManyField(UserAuth)
    tic_type = models.CharField(max_length=30)
