from inspect import iscode
from pyexpat import model
from socket import if_nameindex
from django.db import models
from django.utils.timezone import now


# Create your models here.

class Student(models.Model):

    scode = models.CharField(max_length=15)
    sname = models.TextField()
    sdob = models.DateField()
    department = models.CharField(max_length=20)
    pid0 =models.CharField(max_length=15)
    pid1 =models.CharField(max_length=15)
    pid2 =models.CharField(max_length=15)
    pid3 =models.CharField(max_length=15)
    pid4 =models.CharField(max_length=15)
    pid5 =models.CharField(max_length=15)
    seat =models.IntegerField(default=-1)
    hid = models.IntegerField(default=-1)
    seated = models.IntegerField(default=-1)
    eid =models.IntegerField()

class Papers(models.Model):

    pcode = models.CharField(max_length=10)
    pname = models.TextField()
    pcount =models.IntegerField()
    department = models.CharField(max_length=20)
    edate =models.DateField(default=now)
    etime = models.CharField (max_length=5)
    dornot = models.CharField (max_length=8)
    eid =models.IntegerField()

class Hall(models.Model):
    hcode = models.CharField(max_length=10, unique=True)
    hname = models.TextField(unique=True)
    hcapacity = models.IntegerField()
    eid = models.IntegerField(default=-1)

class Invigilator(models.Model):
    icode = models.CharField(max_length=10,unique=True)
    iname = models.TextField()
    icount = models.IntegerField(default=0)
    idepartment = models.TextField()
    eid = models.IntegerField(default=-1)
    hid = models.IntegerField()

class Exam(models.Model):
    ecode = models.CharField(max_length=10, unique=True)
    ename = models.TextField()
    eyear = models.IntegerField()
    eprogram = models.TextField()
    esemester = models.TextField()
    action = models.TextField()
    papercheck = models.IntegerField(default = 0)
    studentcheck = models.IntegerField(default = 0)

class Timetable(models.Model):
    eid = models.IntegerField()
#    ecode = models.CharField(max_length=10)
    edate = models.DateField()
    etime = models.CharField (max_length=5)
    pid = models.IntegerField(default=-1)
    dornot = models.CharField (max_length=8, default='enabled')
    view = models.CharField (max_length=8, default='disabled')
    allocation = models.CharField(max_length=10, default = 'Allocate')
    full = models.IntegerField(default=0)
    final = models.CharField (max_length=8, default='disabled')


class Temp(models.Model):
    echeck = models.IntegerField(default=0)


class Sexambydate (models.Model):
    scode = models.CharField(max_length=15)
    edate = models.DateField()
    etime = models.CharField (max_length=5)
    pid = models.IntegerField(default= -1)
    pcode = models.CharField(max_length=10)
    sdone =models.IntegerField(default= -1)
    eid= models.IntegerField(default = -1)


class Hallstorage (models.Model):
    seatno =models.IntegerField(default= -1)
    pid = models.IntegerField(default= -1)
    hid = models.IntegerField(default= -1)
    scode = models.CharField(max_length=15)
    edate = models.DateField()
    etime = models.CharField (max_length=5)
    eid= models.IntegerField(default = -1)
    iname = models.TextField(default='UNASSIGNED')
    iid = models.IntegerField(default= -1)
    sassigned = models.IntegerField(default = -1)
    
#class Hallstored
#class Invigilatorstored
#class Paperstored
class Attendancestored (models.Model):
    eid= models.IntegerField(default = -1)
    seatno =models.IntegerField(default= -1)
    pid = models.IntegerField(default= -1)
    edate = models.DateField()
    etime = models.CharField (max_length=5)
    hid = models.IntegerField(default= -1)
    scode = models.CharField(max_length=15)
    present = models.CharField(max_length=15)

class Paperinfo:
    code : str
    pcount : int
class Invi:
    hall : str
    edate : str
    etime : str
    eid : int


#class stored