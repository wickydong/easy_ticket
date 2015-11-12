from django.db import models

class UserAuth(models.Model):
    uid = models.AutoField(primary_key=True)
    user = models.CharField(max_length=30)
    passwd = models.CharField(max_length=50)
    def __unicode__(self):
        return self.user

class AllForm(models.Model):
    allid = models.AutoField(primary_key=True)
    tic_id = models.CharField(max_length=30)
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
    reply = models.IntegerField(default=0)

class FormMsg(models.Model):
    formid = models.AutoField(primary_key=True)
    tic_id = models.CharField(max_length=30)
    queue = models.IntegerField(default=0) 
    times = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserAuth)
    msg = models.TextField()
    behind = models.ManyToManyField(UserAuth,related_name="behind")
