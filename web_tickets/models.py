from django.db import models

class UserAuth(models.Model):
    user = models.CharField(max_length=30)
    passwd = models.CharField(max_length=50)
    god = models.CharField(max_length=20)
    def __unicode__(self):
        return self.user

#class Tickets(models.Model):
#    
#    user = models.CharField(max_length=30)
#    tk_type = models.CharField(max_length=50)
#    tk_msg = models.TextField()
#    tk_time = models.DateTimeField(auto_now_add=True)
#    answer = models.CharField(max_length=30,null=True,blank=True)
#    answer_msg = models.TextField()
#    answer_time = models.DateTimeField(auto_now=True)
#    tks_status = models.CharField(max_length=30,default="nyet")
class Server(models.Model):
    create_time = models.DateTimeField(auto_now=True)
    server_ip = models.CharField(max_length=30)
    needtime = models.CharField(max_length=30)
    needother = models.TextField()
    over_time = models.DateTimeField(auto_now_add=True)
    make_user = models.CharField(max_length=30,null=True)
    over_user = models.CharField(max_length=30,null=True)
class Upgrade(models.Model):
    create_time = models.DateTimeField(auto_now=True)
    upgrade = models.CharField(max_length=100)
    howtime = models.CharField(max_length=30)
    up_msg = models.TextField()
    up_error = models.TextField()
    over_time = models.DateTimeField(auto_now_add=True)
    make_user = models.CharField(max_length=30,null=True)
    over_user = models.CharField(max_length=30,null=True)
class Virtual(models.Model):
    create_time = models.DateTimeField(auto_now=True)
    virtual = models.CharField(max_length=30)
    system = models.CharField(max_length=30)
    needconf = models.TextField()
    over_time = models.DateTimeField(auto_now_add=True)
    make_user = models.CharField(max_length=30,null=True)
    over_user = models.CharField(max_length=30,null=True)
class Fix(models.Model):
    create_time = models.DateTimeField(auto_now=True)
    fix = models.CharField(max_length=30)
    howtime = models.CharField(max_length=30)
    fix_msg = models.TextField()
    over_time = models.DateTimeField(auto_now_add=True)
    make_user = models.CharField(max_length=30,null=True)
    over_user = models.CharField(max_length=30,null=True)
class Update(models.Model):
    create_time = models.DateTimeField(auto_now=True)
    update = models.CharField(max_length=30)
    howtime = models.CharField(max_length=30)
    update_msg = models.TextField()
    over_time = models.DateTimeField(auto_now_add=True)
    make_user = models.CharField(max_length=30,null=True)
    over_user = models.CharField(max_length=30,null=True)

