#!/usr/bin/python
# -*-coding:utf8-*-


import smtplib  
from email.mime.text import MIMEText  
  
def send_mail(sub,content,*args):  
    mailto_list = args
    mail_host="smtp.ym.163.com"  #设置服务器
    mail_user="tickets"    #用户名
    mail_pass="RJgrid@2015"   #口令 
    mail_postfix="gridinfo.com.cn"  #发件箱的后缀
    me="Tickets"+"<"+mail_user+"@"+mail_postfix+">"  
    msg = MIMEText(content,_subtype='plain',_charset='utf8')  
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = ";".join(mailto_list)  
    try:  
        server = smtplib.SMTP()  
        server.connect(mail_host)  
        server.login(mail_user,mail_pass)  
        server.sendmail(me,mailto_list, msg.as_string())  
        server.close()  
        return True
    except Exception, e:  
        print str(e)  
        return False  
