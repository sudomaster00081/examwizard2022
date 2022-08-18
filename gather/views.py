

from time import time
from django.shortcuts import render
from allocate.views import vpapers
from gather.models import Temp
from gather.models import Timetable 
from gather.models import Papers, Student, Exam, Invigilator, Hall
from django.contrib import messages
from django.shortcuts import redirect
from .resources import PapersResource, StudentResource
from tablib import Dataset   

def sfileupload(request):
    if request.method == 'POST' :
        student_resource = StudentResource()
        dataset = Dataset()
        eid = request.POST['eid']
        new_student = request.FILES['myfile']

        if not new_student.name.endswith('xlsx'):
            messages.info(request, 'Wrong File Kindly Use .XLSL File')
            return render (request, 'addstudent.html', {'eid' : eid})

        imported_data  = dataset.load(new_student.read(), format ='xlsx')
        for data in imported_data :
            value = Student(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[10],
            )
            value.eid = eid
            value.pid = 0
            value.seat =0
            value.hid=0
            value.save()
            exam= Exam.objects.get(id=eid)
            exam.studentcheck=(exam.studentcheck+1)
            exam.save();
    students = Student.objects.filter(eid=eid)
    messages.info(request, 'Students Data Successfully Uploaded')
    return render(request, 'studentinfo.html',{'students' : students, 'eid' : eid})





def pfileupload(request):
    if request.method == 'POST' :
        paper_resource = PapersResource()
        dataset = Dataset()
        eid = request.POST['eid']
        new_papers = request.FILES['myfile']

        if not new_papers.name.endswith('xlsx'):
            messages.info(request, 'Wrong File Kindly Use .XLSx File')
            return render (request, 'addpaper.html', {'eid' : eid})

        imported_data  = dataset.load(new_papers.read(), format ='xlsx')
        for data in imported_data :
            value = Papers(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],    
                data[5],
                data[6],
            )
            value.eid = eid

            value.save()
            exam= Exam.objects.get(id=eid)
            exam.papercheck=(exam.papercheck+1)
            exam.save();
    papers = Papers.objects.filter(eid=eid)
    return render(request, 'vpaper.html',{'papers' : papers, 'eid' : eid})

# Create your views here.
def new(request):
    return render(request, 'new.html')

"""def nominal(request):
    return render(request, 'nominal.html')
"""
def newexam(request):
    if request.method == 'POST':
        ecode = request.POST['ecode']
        ename = request.POST['ename']
        year= request.POST['year']
        pgm= request.POST['country']
        sem= request.POST['state']
        if not Exam.objects.filter(ename =ename,eyear=year, ecode=ecode, eprogram=pgm, esemester=sem).exists():

            exam = Exam(ename =ename,eyear=year, ecode=ecode, eprogram=pgm, esemester=sem)
            exam.papercheck=0;
            exam.studentcheck=0;
            exam.save();
            messages.info(request, 'New Exam SuccessFully Added')
            response = selectexam(request)
            return response
        else:
            messages.info(request, 'Exam Already Exists')
            return render(request, 'newexam.html')

    else :
        return render(request, 'newexam.html')

def paperinfo(request):
        papers = Papers.objects.all()
        return render(request, 'paperinfo.html',{'papers' : papers})

def studentinfo(request):
    students = Student.objects.all()
    return render(request, 'studentinfo.html',{'students' : students})

def hallinfo(request):
    halls = Hall.objects.all()
    return render(request, 'hallinfo.html', {'halls' : halls})

def invigilatorinfo(request):
    if request.method == 'POST' :
        invigilators = Invigilator.objects.all()
        return render(request, 'invigilatorinfo.html', {'invigilators' : invigilators})
    else :
        return render(request, 'invigilatorinfo.html', {'invigilators' : invigilators})

def addhall(request):
    if request.method == 'POST':
        hcode = request.POST['hcode']
        hname = request.POST['hname']
        hcapacity = request.POST['hcapacity']
        if not Hall.objects.filter(hcode = hcode, hname = hname, hcapacity= hcapacity,eid=0).exists():

            hvalue = Hall(hcode = hcode, hname = hname, hcapacity= hcapacity,eid=0)
            hvalue.save();
            halls = Hall.objects.all()
            messages.info(request, 'Hall SuccessFully Added')
            return render(request, 'hallinfo.html', {'halls' : halls})
        else:
            messages.info(request, 'Hall Already Exists')
            return render (request, 'addhall.html')
    else :
        return render (request, 'addhall.html')


def addInvigilator(request):
    if request.method == 'POST':
        icode = request.POST['icode']
        iname = request.POST['iname']
        idepartment = request.POST['idepartment']
        icount =0
        eid=0
        hid=0
        if not Invigilator.objects.filter(icode=icode,iname = iname, icount=icount, idepartment=idepartment ).exists():

            ivalue = Invigilator(icode=icode,iname = iname, icount=icount, idepartment=idepartment, eid=eid, hid=hid )
            ivalue.save();
            messages.info(request, 'Invigilator SuccessFully Added')
            #invigilators = Invigilator.objects.all()
            #return render(request, 'invigilatorinfo.html', {'invigilators' : invigilators})
            response= invigilatorinfo(request)
            return response
        else:
            messages.info(request, 'Hall Already Exists')
            return render (request, 'addInvigilator.html')
    else :
        return render (request, 'addInvigilator.html')
    
def hedit(request):
    return render (request, )

def hdelete(request ):
    id= request.POST['id']
    dele = Hall.objects.get(id=id)
    dele.delete();
    messages.info(request, 'Hall SuccessFully Deleted')
    response = hallinfo(request)
    return response


def iedit(request):
    return render (request, )

def idelete(request):
    id= request.POST['id']
    dele = Invigilator.objects.get(id=id)
    dele.delete();
    messages.info(request, 'Invigilator SuccessFully Deleted')
    response = invigilatorinfo(request)
    return response

def examinfo(request) :
    exams = Exam.objects.all()
    return render(request, 'examinfo.html', {'exams' : exams})

"""def selectpexam (request):
    if request.method == 'POST':
        eid=request.POST['id']
        papers = Papers.objects.filter(eid=eid)
        action = 'selectpexam'
        if papers == None:
            messages.info(request, 'No Papers Found For The Exam')
            return render(request, 'selectexam.html')
        return render(request, 'paperinfo.html',{'papers' : papers, 'eid' : eid, 'action': action})
    else:
        exams = Exam.objects.all()
        return render(request, 'selectexam.html', {'exams' : exams})"""

"""def selectsexam (request):
    
    if request.method == 'POST':
        eid=request.POST['id']
        students = Student.objects.filter(eid=eid)
        action = 'selectsexam'
        if students == None:
            messages.info(request, 'No Students Found For The Exam')
            return render(request, 'selectexam.html')
        return render(request, 'studentinfo.html',{'students' : students, 'eid' : eid, 'action': action})
    else:
        exams = Exam.objects.all()
        return render(request, 'selectexam.html', {'exams' : exams})"""

"""def addstudent (request):
    eid = request.POST['eid']
    exam= Exam.objects.get(id=eid)
    if exam.studentcheck == 0 :
        return render(request, 'addstudent.html', {'eid' : eid})
    else :
        response = vstudents(request)
        return response"""

def addpaper (request):
    
    eid = request.POST['id']
    exam= Exam.objects.get(id=eid)
    if exam.papercheck == 0 :
        return render(request, 'addpaper.html', {'eid' : eid})
    else :
        response = vpapers(request)
        return response

def pdelete(request):
    eid= request.POST['eid']
    dele = Papers.objects.filter(eid=eid)
    pcheck =Exam.objects.get(id=eid)
    dele.delete()
    pcheck.papercheck = 0
    pcheck.save()
    messages.info(request, 'Papers SuccessFully Deleted')
    eid = request.POST['eid']
    return render (request, 'addpaper.html', {'eid' : eid})


def sdelete(request):
    eid= request.POST['eid']
    dele = Student.objects.filter(eid=eid)
    scheck =Exam.objects.get(id=eid)
    dele.delete()
    scheck.studentcheck = 0
    scheck.save();
    messages.info(request, 'Student SuccessFully Deleted')
    eid = request.POST['eid']
    return render (request, 'addstudent.html', {'eid' : eid})

"""def selecttexam (request):
    if request.method == 'POST':
        eid=request.POST['id']
        timetables = Timetable.objects.filter(eid=eid)
        action = 'selecttexam'
        if timetables == None:
            messages.info(request, 'No Timetable Found For The Exam')
            return render(request, 'selecttexam.html')
        return render(request, 'timetableinfo.html',{'timetables' : timetables, 'eid' : eid, 'action': action})
    else:
        exams = Exam.objects.all()
        return render(request, 'selectexam.html', {'exams' : exams})"""

"""def addtimetable (request):
    if request.method== 'POST' :
        eid=request.POST['eid']
        papers = Papers.objects.filter(eid=eid)
        date = request.POST['date']
        time = request.POST['time']
        pid = request.POST['pid']
        if Timetable.objects.filter(pid=pid).exists():
            messages.info(request, 'Time Table Taken ,Delete Existing before making changes')
            papers = Papers.objects.filter(eid=eid)
            timetables = Timetable.objects.filter(eid=eid)
            return render(request, 'addtimetable.html', {'papers' : papers , 'timetables' : timetables, 'eid' : eid})
        pvalue =Papers.objects.get(id=pid)
        pvalue.edate = date
        pvalue.etime = time
        ecode1 = Papers.objects.get(id=pid)
        ecode = ecode1.pcode
        dornot = 'disabled'
        tvalue = Timetable(eid=eid, edate=date, etime=time, pid=pid, ecode=ecode, dornot=dornot)
        ecode1.dornot = 'disabled'
        tvalue.save();
        ecode1.save();
        messages.info(request, 'Time Table Added Success Fully')
        timetables = Timetable.objects.filter(id=eid)
        return render (request, 'addtimetable.html',{'papers' : papers , 'timetables' : timetables, 'eid' : eid})
"""
"""def tdelete(request):
    id= request.POST['tid']
    pid= request.POST['pid']
    val = Papers.objects.get(id=pid)
    val.dornot = 'none'
    val.save();
    dele = Timetable.objects.get(id=id)
    dele.delete();
    val.dornot = 'none'
    val.save();
    messages.info(request, 'Time Table SuccessFully Deleted')
    eid=request.POST['eid']
    timetables = Timetable.objects.filter(eid=eid)
    action = 'selecttexam'
    if timetables == None:
        messages.info(request, 'No Timetable Found For The Exam')
        return render(request, 'selecttexam.html')
    return render(request, 'timetableinfo.html',{'timetables' : timetables, 'eid' : eid, 'action': action})
   """ 
def selectexam (request):
    if not Exam.objects.all().exists():
        response = newexam(request)
        return response
    action ='addpaper'
    exams = Exam.objects.all()
    return render(request, 'selectexam.html', {'action' : action, 'exams' : exams})


def about (request):

        return render (request, 'about.html')