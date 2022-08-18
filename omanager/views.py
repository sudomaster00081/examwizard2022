import imp
from django.shortcuts import render
from gather.models import Paperinfo
from gather.models import Attendancestored, Student
from gather.models import Invigilator,Papers
from gather.models import Hallstorage
from gather.models import Hall, Invi
from gather.models import Timetable
from django.contrib import messages
from gather.models import Exam
from gather.views import addpaper




# Create your views here.
def selectoexam (request):
    if request.method == 'POST':
        eid = request.POST['id']
        if Hallstorage.objects.filter(eid=eid).exists():
            return render(request, 'aaselect.html', {'eid':eid})
        else :
            exams = Exam.objects.all()
            action = 'selectoexam'
            messages.info(request, 'Initialise The Exam First')
            response = addpaper(request)
            return response #render(request, 'selectexam.html', {'exams' : exams, 'action' : action })
    else:
        exams = Exam.objects.all()
        action = 'selectoexam'
        return render(request, 'selectexam.html', {'exams' : exams, 'action' : action })


def selectshedule (request):
    if request.method == 'POST':
        eid = request.POST['eid']
        timetables=Timetable.objects.filter(eid=eid)  
        action = 'selecthall' 
        return render(request, 'selectshedule.html', {'action' : action, 'timetables' : timetables, 'eid' : eid,})
    else:
        eid = request.GET['eid']
        return render(request, 'aaselect.html', {'eid':eid})


def selecthall (request):
    if request.method == 'POST':
        eid = request.POST['eid']
        edate = request.POST['edate']
        etime = request.POST['etime']
        halls = []
        halls1 = Hallstorage.objects.values('hid').filter(eid=eid, edate=edate, etime=etime).distinct();
        for halls11 in halls1:
            hallss=Hall.objects.get( id=halls11['hid'])
            halls.append(hallss)
            action='oviewseating'
            back = 'selectshedule'
        return render(request, 'selecthall.html', {'back':back, 'eid':eid, 'halls':halls, 'edate':edate, 'etime':etime, 'action':action})
    else:
        eid = request.GET['eid']
        return render(request, 'aaselect.html', {'eid':eid})


def oviewseating (request):
    if request.method == 'POST':
        eid = request.POST['eid']
        edate = request.POST['edate']
        etime = request.POST['etime']
        hid = request.POST['hid']
        allocateinfo = Hallstorage.objects.filter(eid=eid,edate=edate,etime=etime,hid = hid)
        invigilator = allocateinfo[0].iname
        #invigilator = Invigilator.objects.get(id=invigilator1['iid'])
        return render (request, 'oseatinginfo.html', {'hid':hid, 'allocateinfo' : allocateinfo ,'eid':eid, 'edate':edate, 'etime':etime,'invigilator' : invigilator })
    else :
        eid = request.POST['eid1']
        edate = request.POST['edate1']
        etime = request.POST['etime1']
        halls = []
        halls1 = Hallstorage.objects.values('hid').filter(eid=eid, edate=edate, etime=etime).distinct();
        for halls11 in halls1:
            hallss=Hall.objects.get(eid=eid, id=halls11['hid'])
            halls.append(hallss)
        return render(request, 'selecthall.html', {'eid':eid, 'halls':halls, 'edate':edate, 'etime':etime})

def attendancemanagement (request):
    if request.method == 'POST':
        eid = request.POST['eid']

        return render(request, 'attendancemanagement.html' , {'eid' : eid})
    else :
         eid = request.GET['eid']
         return render(request, 'aaselect.html', {'eid':eid})

def invioutput (request):
    eid = request.POST['eid']
    exams =Exam.objects.get(id=eid)
    edate1 = request.POST['edate']
    etime = request.POST['etime']
    hid = request.POST['hid']
    edate11 = Papers.objects.filter(eid=eid, edate=edate1, etime=etime)
    edate = edate11[0].edate
    hall=Hall.objects.get(id=hid)
    students = Hallstorage.objects.filter(eid=eid, etime=etime, edate=edate, hid=hid)
    invigilator = students[0].iname
    
    
    return render(request, 'invioutput.html', {'invigilator': invigilator,'edate1':edate1,'hall':hall, 'edate':edate,'students':students, 'eid':eid , 'exams': exams,'etime':etime})

def iselectshedule (request):
    if request.method == 'POST':
        eid = request.POST['eid']
        timetables=Timetable.objects.filter(eid=eid)
        action = 'iselecthall'   
        return render(request, 'selectshedule.html', {'action':action, 'timetables' : timetables, 'eid' : eid,})
    else:
        eid = request.GET['eid']
        return render(request, 'aaselect.html', {'eid':eid})
        
def iselecthall (request):
    if request.method == 'POST':
        eid = request.POST['eid']
        edate = request.POST['edate']
        etime = request.POST['etime']
        halls = []
        halls1 = Hallstorage.objects.values('hid').filter(eid=eid, edate=edate, etime=etime).distinct();
        for halls11 in halls1:
            hallss=Hall.objects.get( id=halls11['hid'])
            halls.append(hallss)
        action = 'invioutput'
        back = 'iselectshedule'
        blank='_blank'
        return render(request, 'selecthall.html', {'blank':blank,'action':action,'back':back,'eid':eid, 'halls':halls, 'edate':edate, 'etime':etime})
    else:
        eid = request.GET['eid']
        return render(request, 'aaselect.html', {'eid':eid})

def halloutput (request):
    eid = request.POST['eid']
    edate = request.POST['edate']
    etime = request.POST['etime']
    hid = request.POST['hid']
    invigilator = request.POST['invigilator']
    etime = request.POST['etime']
    exams =Exam.objects.get(id=eid)
    hall=Hall.objects.get(id=hid)
    students = Hallstorage.objects.filter(eid=eid, edate=edate, etime=etime, hid=hid)
    paperinfo=[]
    papers= Papers.objects.filter(eid=eid,edate=edate,etime=etime)
    for paper in papers:
        ptemp=Hallstorage.objects.filter(eid=eid,edate=edate,etime=etime,hid=hid,pid=paper.id)
        paperinfo1= Paperinfo()
        paperinfo1.pcount= len(ptemp)
        paperinfo1.code =paper.pcode
        paperinfo.append(paperinfo1)
    return render(request, 'halloutput.html',{'hall':hall,'exams':exams,'students':students, 'eid':eid, 'edate':edate, 'etime':etime,'invigilator' : invigilator,'paperinfo':paperinfo})


def mselectshedule (request):
    if request.method == 'POST':
        eid = request.POST['eid']
        timetables=Timetable.objects.filter(eid=eid)  
        action = 'mselecthall' 
        return render(request, 'selectshedule.html', {'action' : action, 'timetables' : timetables, 'eid' : eid,})
    else:
        eid = request.GET['eid']
        return render(request, 'aaselect.html', {'eid':eid})

def mselecthall (request):
    if request.method == 'POST':
        eid = request.POST['eid']
        edate = request.POST['edate']
        etime = request.POST['etime']
        halls = []
        halls1 = Hallstorage.objects.values('hid').filter(eid=eid, edate=edate, etime=etime).distinct();
        for halls11 in halls1:
            hallss=Hall.objects.get( id=halls11['hid'])
            halls.append(hallss)
            action='markattendance'
            back = 'mselectshedule'
        return render(request, 'selecthall.html', {'back':back, 'eid':eid, 'halls':halls, 'edate':edate, 'etime':etime, 'action':action})
    else:
        eid = request.GET['eid']
        return render(request, 'aaselect.html', {'eid':eid})

def markattendance (request):
    if request.method == 'POST':
        eid = request.POST['eid']
        edate = request.POST['edate']
        etime = request.POST['etime']
        hid = request.POST['hid']
        if Attendancestored.objects.filter(eid=eid,edate=edate,etime=etime,hid=hid).exists():
            messages.info(request, 'Attendance Already Marked')
            halls = []
            halls1 = Hallstorage.objects.values('hid').filter(eid=eid, edate=edate, etime=etime).distinct();
            for halls11 in halls1:
                hallss=Hall.objects.get( id=halls11['hid'])
                halls.append(hallss)
            action='markattendance'
            back = 'mselectshedule'
            return render(request, 'selecthall.html', {'back':back, 'eid':eid, 'halls':halls, 'edate':edate, 'etime':etime, 'action':action})
        else :
            students = Hallstorage.objects.filter(eid=eid, edate=edate, etime=etime, hid= hid)
            return render(request, 'markattendance.html', {'hid1':hid, 'eid':eid,'students':students, 'edate':edate, 'etime':etime })

def saveattendance (request):
    if request.method == 'POST':
        eid = request.POST['eid']
        edate = request.POST['edate']
        etime = request.POST['etime']
        hid = request.POST['hid']
        students = Hallstorage.objects.filter(eid=eid, edate=edate, etime=etime, hid=hid)
        for student in students :
            temp=request.POST[student.scode]
            attendance = Attendancestored()
            attendance.scode = student.scode
            attendance.eid=student.eid
            attendance.seatno=student.seatno
            attendance.edate=student.edate
            attendance.etime=student.etime
            attendance.hid=student.hid
            if temp == 'checked':
                attendance.present='present'
            else:
                attendance.present='absent' 
            ostudent=Student.objects.get(scode=student.scode, eid=eid)
            pcheckk = Papers.objects.filter(eid=eid, edate=edate, etime=etime)
            for pcheck in pcheckk:
                
                if ostudent.pid0 == pcheck.pcode:
                    attendance.pid=pcheck.id   
                elif ostudent.pid1 == pcheck.pcode:
                    attendance.pid=pcheck.id   
                elif ostudent.pid2 == pcheck.pcode:
                    attendance.pid=pcheck.id   
                elif ostudent.pid3 == pcheck.pcode:
                    attendance.pid=pcheck.id   
                elif ostudent.pid4 == pcheck.pcode:
                    attendance.pid=pcheck.id   
                elif ostudent.pid5 == pcheck.pcode:
                    attendance.pid=pcheck.id   
                else:
                    continue
            attendance.save();
        #response = mselecthall(request)
        messages.info(request, 'Attendance Marked Successfully')
        halls = []
        halls1 = Hallstorage.objects.values('hid').filter(eid=eid, edate=edate, etime=etime).distinct();
        for halls11 in halls1:
            hallss=Hall.objects.get( id=halls11['hid'])
            halls.append(hallss)
            action='markattendance'
            back = 'mselectshedule'
        return render(request, 'selecthall.html', {'back':back, 'eid':eid, 'halls':halls, 'edate':edate, 'etime':etime, 'action':action})
        #return response

def pselectshedule (request):
    if request.method == 'POST':
        eid = request.POST['eid']
        timetables=Timetable.objects.filter(eid=eid)  
        action = 'aselectpaper' 
        return render(request, 'selectshedule.html', {'action' : action, 'timetables' : timetables, 'eid' : eid,})
    else:
        eid = request.GET['eid']
        return render(request, 'aaselect.html', {'eid':eid})


def pselecthall (request):
    if request.method == 'POST':
        eid = request.POST['eid']
        edate = request.POST['edate']
        etime = request.POST['etime']
        halls = []
        action='aselectpaper'
        back = 'pselectshedule'
        halls1 = Hallstorage.objects.values('hid').filter(eid=eid, edate=edate, etime=etime).distinct();
        for halls11 in halls1:
            hallss=Hall.objects.get( id=halls11['hid'])
            if Attendancestored.objects.filter(eid=eid,hid=hallss.id, edate=edate,etime=etime).exists():
                halls.append(hallss)
            else :
                if not Attendancestored.objects.filter(eid=eid,edate=edate,etime=etime).exists():
                    messages.info(request, 'Mark Attendance First ')
                    timetables=Timetable.objects.filter(eid=eid)  
                    action = 'pselecthall' 
                    return render(request, 'selectshedule.html', {'action' : action, 'timetables' : timetables, 'eid' : eid,})
            
        return render(request, 'selecthall.html', {'back':back, 'eid':eid, 'halls':halls, 'edate':edate, 'etime':etime, 'action':action})
    else:
        eid = request.GET['eid']
        return render(request, 'aaselect.html', {'eid':eid})

def aselectpaper (request):
    if request.method == 'POST':
        eid = request.POST['eid']
        edate = request.POST['edate']
        etime = request.POST['etime']
        papers = Papers.objects.filter(eid=eid,edate=edate,etime=etime)
        blank = '_blank'
        back = 'pselectshedule'
        return render (request, 'aselectpaper.html', {'blank':blank,'back':back,'eid':eid,'papers':papers, 'edate':edate, 'etime':etime})

def opattendance (request):
    if request.method == 'POST':
        eid = request.POST['eid']
        edate = request.POST['edate']
        etime = request.POST['etime']
        pid = request.POST['pid']
        exam=Exam.objects.get(id=eid)
        paper= Papers.objects.get(id=pid)
        halls= Attendancestored.objects.values('hid').filter(eid=eid, edate=edate, etime=etime).distinct();
        hallscheck = Hallstorage.objects.values('hid').filter(eid=eid, edate=edate, etime=etime).distinct();
        if len(halls) == len(hallscheck) :
            absenties = Attendancestored.objects.filter( edate=edate, eid=eid, etime=etime, pid=pid, present ='absent' )
            presents = Attendancestored.objects.filter(edate=edate, etime=etime, eid=eid, pid=pid, present = 'present' )
            papercount = len(presents)
            apapercount = len(absenties)
            return render(request, 'attendancesheet.html',{'apapercount':apapercount,'absenties':absenties,'edate':edate,'etime':etime,'exam':exam,'paper':paper,'papercount':papercount,'presents':presents  })
        else:
            messages.info(request, 'Hall Attendance Missing !!! ')
            papers = Papers.objects.filter(eid=eid,edate=edate,etime=etime)
            blank = '_blank'
            back = 'pselectshedule'
            return render (request, 'aselectpaper.html', {'blank':blank,'back':back,'eid':eid,'papers':papers, 'edate':edate, 'etime':etime})

def viewshedule (request):
    exams=Exam.objects.all()
    timetables = Timetable.objects.all()
    return render (request, 'shedule.html',{'exams':exams, 'timetables':timetables})


def viewstudentshedule (request):
    if request.method == 'POST':
        scode = request.POST['scode']
        if not Student.objects.values('scode').filter(scode=scode).exists():
            messages.info(request, 'Student With id Does not Exist')

            return render(request,'home.html')
        name = Student.objects.get(scode=scode)
        iid = Student.objects.values('scode').get(scode=scode)
        abc= []
        timetables = Timetable.objects.all()
        for timetable in timetables:
            invi1 = Hallstorage.objects.values('hid').filter(edate=timetable.edate,etime=timetable.etime,scode=iid['scode'])
            eid1 = Hallstorage.objects.values('eid').filter(edate=timetable.edate,etime=timetable.etime,scode=iid['scode'])
            i = len(invi1)
            if not i == 0:
                
                print(invi1)     
                invi2 = invi1[0]
                eid2=eid1[0]
                print(invi2)
                invi= invi2['hid']
                eid=eid2['eid']
                #print(invi)
                hall1 = Hall.objects.get(id=invi)
                invig = Invi()
                invig.hall=hall1.hname
                invig.edate=timetable.edate
                invig.etime=timetable.etime
                invig.eid=eid
                abc.append(invig)
        if len(abc)==0 :
            messages.info(request, 'No Shedules Available for You at the Moment!!!')
            return render(request,'home.html')
        return render(request, 'studentarea.html', {'name':name,'abc':abc})


def viewinvigilatorshedule (request):
    if request.method == 'POST':
        icode = request.POST['icode']
        if not Invigilator.objects.filter(icode=icode).exists():
            messages.info(request, 'Invigilator With id Does not Exist')

            return render(request,'home.html')
        else:
            name = Invigilator.objects.get(icode=icode)

            iid = Invigilator.objects.values('id').get(icode=icode)
            abc= []
            timetables = Timetable.objects.all()
            for timetable in timetables:
                invi1 = Hallstorage.objects.values('hid').filter(edate=timetable.edate,etime=timetable.etime,iid=iid['id'])
                eid1 = Hallstorage.objects.values('eid').filter(edate=timetable.edate,etime=timetable.etime,iid=iid['id'])
                i = len(invi1)
                if not i == 0:
                    print(i)
                    print(invi1)     
                    invi2 = invi1[0]
                    eid2=eid1[0]
                    print(invi2)
                    invi= invi2['hid']
                    eid=eid2['eid']
                    #print(invi)
                    hall1 = Hall.objects.get(id=invi)
                    invig = Invi()
                    invig.hall=hall1.hname
                    invig.edate=timetable.edate
                    invig.etime=timetable.etime
                    invig.eid=eid
                    abc.append(invig)
            if len(abc)==0 :
                messages.info(request, 'No Shedules Available for You at the Moment!!!')
                return render(request,'home.html')
            return render(request, 'invigilatorarea.html', {'name':name,'abc':abc})



def error_404(request, exception):
        data = {}
        return render(request,'certman/404.html', data)


def navselectexam (request):
    action="mselectshedule"
    exams=Exam.objects.all()
    return render (request, 'selectexam.html', {'exams':exams,'action':action})

def navselectexam2 (request):
    action="pselectshedule"
    exams=Exam.objects.all()
    return render (request, 'selectexam.html', {'exams':exams,'action':action})

def navselectexam23 (request):
    action="selectshedule"
    exams=Exam.objects.all()
    return render (request, 'selectexam.html', {'exams':exams,'action':action})


def navselectexam24 (request):
    action="iselectshedule"
    exams=Exam.objects.all()
    return render (request, 'selectexam.html', {'exams':exams,'action':action})
























































