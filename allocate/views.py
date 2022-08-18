from django.contrib import messages
from genericpath import exists
from django.shortcuts import render
from gather.models import Attendancestored
from gather.models import Hallstorage
from gather.models import Sexambydate

from gather.models import Temp
from gather.models import Timetable,Invigilator,Hall,Student,Papers,Exam  
# Create your views here.

def allocate (request):
    
    if request.method == 'POST': 
        eid = request.POST['eid']
        tid = request.POST['tid']
        edate = request.POST['edate']
        etime = request.POST['etime']
        mainsexams = Sexambydate.objects.filter(edate=edate, etime=etime, eid=eid)
        halllists = Hall.objects.filter(eid=eid)
        for hallist in halllists :
            hid=hallist.id
            count = hallist.hcapacity
            seats = list(range(0, count))
            for seat in seats :
                if Hallstorage.objects.filter(eid=eid, edate=edate, etime=etime, hid=hid, seatno = seat).exists():
                    continue
                else :
                    for student in mainsexams :
                        if Hallstorage.objects.filter(eid=eid, edate=edate, etime=etime, scode=student.scode).exists():
                            continue
                        else :
                            hallstorage = Hallstorage()
                            hallstorage.seatno = seat
                            hallstorage.pid = student.pid
                            hallstorage.hid = hallist.id
                            hallstorage.scode = student.scode
                            hallstorage.edate = student.edate
                            hallstorage.etime = student.etime
                            hallstorage.eid = student.eid
                            hallstorage.save();
                            break; 
        timetable = Timetable.objects.get(eid=eid, edate=edate, etime=etime)
        timetable.dornot='disabled'
        timetable.allocation = 'ALLOCATED'
        timetable.view='enabled'
        timetable.save();  
        time1 =Timetable.objects.get(eid=eid, edate=edate, etime=etime)
        time1.final='enabled'
        time1.save();
        times = Timetable.objects.filter(eid=eid)
        for time in times:
            if time.final == 'enabled':
                final='enabled'
            else :
                final='disabled'
                break
        timetables=Timetable.objects.filter(eid=eid)   
        
        messages.info(request, 'Allocation Successfull')
        return render(request, 'timetableinfo.html', { 'timetables' : timetables, 'eid' : eid, 'final' : final})
    else :
        exams = Exam.objects.all()
        action = 'vpapers'
        return render (request, 'selectexam.html' ,{'exams' : exams, 'action' : action})

def vhalls(request):
    if request.method == 'POST':
        eid=request.POST['eid']
        if Hall.objects.all().exists():
            halls = Hall.objects.all()
            for hall in halls:
                hall.eid=eid
                hall.save()
            return render (request, 'vhall.html' ,{'halls' : halls, 'eid' : eid})
        else:
            messages.info(request, 'Add Halls First')
            return render(request, 'main.html')

    else :
        eid=request.GET['eid']
        halls = Hall.objects.all()
        for hall in halls :
            temp=request.GET[hall.hcode]
            if temp == 'checked':
                hall.eid = eid
                #attendance=Attendancestored()
                hall.save();
        if Invigilator.objects.all().exists():

            invigilators = Invigilator.objects.all()
            for invigilator in invigilators:
                invigilator.eid=eid
                invigilator.save()
            return render (request, 'vinvigilator.html' ,{'invigilators' : invigilators, 'eid' : eid})
        else:
            messages.info(request, 'Add Invigilators First')
            return render(request, 'main.html')


"""def managetemp(request):
    temp=Temp()
    temp.echeck=0
    temp.save();
    return render(request, "base.html")"""
   

def vinvigilators(request):
    if request.method == 'GET':
        eid=request.GET['eid']
        invigilators = Invigilator.objects.all()
        for invigilator in invigilators :
            temp=request.GET[invigilator.icode]
            if temp == 'checked':
                invigilator.eid = eid
                invigilator.save();
            tobe = 'verify_And_Allocate'
            disornot ='enabled'
        
        """students = Student.objects.filter(eid=eid)
        for student in students:
            scode =student.scode
            sexambydate1 = Sexambydate()
            paper1=Papers.objects.filter(eid=eid,pcode = student.pid0)
            sexambydate1(scode=scode,  etime=paper1.etime, pid=paper1.pid, pcode=paper1.pcode)
            sexambydate1.save();

            sexambydate2 = Sexambydate()
            paper2=Papers.objects.filter(eid=eid,pcode =student.pid1)
            sexambydate2(scode=scode,edate=paper2.edate,etime=paper2.etime,pid=paper2.pid,pcode=paper2.pcode)
            sexambydate2.save();


            sexambydate3 = Sexambydate()
            paper3=Papers.objects.filter(eid=eid,pcode =student.pid2)
            sexambydate3(scode=scode,edate=paper3.edate,etime=paper3.etime,pid=paper3.pid,pcode=paper3.pcode)
            sexambydate3.save();


            sexambydate4 = Sexambydate()
            paper4=Papers.objects.filter(eid=eid,pcode =student.pid3)
            sexambydate4(scode=scode,edate=paper4.edate,etime=paper4.etime,pid=paper4.pid,pcode=paper4.pcode)
            sexambydate4.save();


            sexambydate5 = Sexambydate()
            paper5=Papers.objects.filter(eid=eid,pcode =student.pid4)
            sexambydate5(scode=scode,edate=paper5.edate,etime=paper5.etime,pid=paper5.pid,pcode=paper5.pcode)
            sexambydate5.save();


            sexambydate6 = Sexambydate()
            paper6=Papers.objects.filter(eid=eid,pcode =student.pid5)
            sexambydate6(scode=scode,edate=paper6.edate,etime=paper6.etime,pid=paper6.pid,pcode=paper6.pcode)
            sexambydate6.save();"""
            


        papers1 = Papers.objects.filter(eid=eid)
        if Timetable.objects.filter(eid=eid).exists():
            i=1
        else :
            i=0
        for papers11 in papers1 :
            flag=0
            timetables1 = Timetable()
            if i==0:
                timetables1.edate = papers11.edate
                timetables1.etime = papers11.etime
                timetables1.eid=papers11.eid
                timetables1.pid=papers11.id
                timetables1.save();
                i=i+1
            
            if Timetable.objects.filter( edate=papers11.edate, eid=eid, etime=papers11.etime).exists():
                flag=1
            
            if flag != 1 :
                timetables1.edate = papers11.edate
                timetables1.etime = papers11.etime
                timetables1.eid = papers11.eid
                timetables1.pid=papers11.id
                timetables1.save();



                
        if Sexambydate.objects.filter(eid=eid).exists():
            timetables=Timetable.objects.filter(eid=eid)   
            final=timetables[0].final 
            return render(request, 'timetableinfo.html', { 'timetables' : timetables, 'eid' : eid, 'final' :final })
        else :    
            timetableo = Timetable.objects.filter(eid=eid)
            for timetable in timetableo :
                edate=timetable.edate
                etime= timetable.etime
                papersondate = Papers.objects.filter(edate = edate, etime = etime, eid = eid)
                for papers in papersondate :
                    val = papers.pcode
                    if Student.objects.filter(eid=eid, pid0 = val).exists():
                        
                        student1 = Student.objects.filter(eid=eid, pid0=papers.pcode)
                        for student in student1 :
                            studentstorage = Sexambydate()
                            studentstorage.scode = student.scode
                            studentstorage.edate = papers.edate
                            studentstorage.etime = papers.etime
                            studentstorage.pid = papers.id
                            studentstorage.pcode = papers.pcode
                            studentstorage.eid = eid

                            #studentstorage1 = Sexambydate.objects.filter()
                            if not Sexambydate.objects.filter(eid=eid, pid = papers.id, scode =student.scode).exists():
                                studentstorage.save();

                    elif Student.objects.filter(eid=eid, pid1 = papers.pcode).exists():
                        student1 = Student.objects.filter(eid=eid, pid1=papers.pcode)
                        for student in student1 :
                            
                            studentstorage = Sexambydate()
                            studentstorage.scode = student.scode
                            studentstorage.edate = papers.edate
                            studentstorage.etime = papers.etime
                            studentstorage.pid = papers.id
                            studentstorage.pcode = papers.pcode
                            studentstorage.eid = eid

                            studentstorage1 = Sexambydate.objects.filter()
                            if not Sexambydate.objects.filter(eid=eid, pid = papers.id, scode =student.scode).exists():
                                studentstorage.save();

                    elif Student.objects.filter(eid=eid, pid2 = papers.pcode).exists():
                        student1 = Student.objects.filter(eid=eid, pid2=papers.pcode)
                        for student in student1 :
                            
                            studentstorage = Sexambydate()
                            studentstorage.scode = student.scode
                            studentstorage.edate = papers.edate
                            studentstorage.etime = papers.etime
                            studentstorage.pid = papers.id
                            studentstorage.pcode = papers.pcode
                            studentstorage.eid = eid

                            studentstorage1 = Sexambydate.objects.filter()
                            if not Sexambydate.objects.filter(eid=eid, pid = papers.id, scode =student.scode).exists():
                                studentstorage.save();

                    elif Student.objects.filter(eid=eid, pid3 = papers.pcode).exists():
                        student1 = Student.objects.filter(eid=eid, pid3=papers.pcode)
                        for student in student1 :
                            
                            studentstorage = Sexambydate()
                            studentstorage.scode = student.scode
                            studentstorage.edate = papers.edate
                            studentstorage.etime = papers.etime
                            studentstorage.pid = papers.id
                            studentstorage.pcode = papers.pcode
                            studentstorage.eid = eid

                            studentstorage1 = Sexambydate.objects.filter()
                            if not Sexambydate.objects.filter(eid=eid, pid = papers.id, scode =student.scode).exists():
                                studentstorage.save();

                    elif Student.objects.filter(eid=eid, pid4 = papers.pcode).exists():
                        student1 = Student.objects.filter(eid=eid, pid4=papers.pcode)
                        for student in student1 :
                            
                            studentstorage = Sexambydate()
                            studentstorage.scode = student.scode
                            studentstorage.edate = papers.edate
                            studentstorage.etime = papers.etime
                            studentstorage.pid = papers.id
                            studentstorage.pcode = papers.pcode
                            studentstorage.eid = eid

                            studentstorage1 = Sexambydate.objects.filter()
                            if not Sexambydate.objects.filter(eid=eid, pid = papers.id, scode =student.scode).exists():
                                studentstorage.save();

                    elif Student.objects.filter(eid=eid, pid5 = papers.pcode).exists():
                        student1 = Student.objects.filter(eid=eid, pid5=papers.pcode)
                        for student in student1 :
                            
                            studentstorage = Sexambydate()
                            studentstorage.scode = student.scode
                            studentstorage.edate = papers.edate
                            studentstorage.etime = papers.etime
                            studentstorage.pid = papers.id
                            studentstorage.pcode = papers.pcode
                            studentstorage.eid = eid

                            studentstorage1 = Sexambydate.objects.filter()
                            if not Sexambydate.objects.filter(eid=eid, pid = papers.id, scode =student.scode).exists():
                                studentstorage.save();    


        timetables=Timetable.objects.filter(eid=eid)
        final=timetables[0].final    
        return render(request, 'timetableinfo.html', { 'timetables' : timetables, 'eid' : eid, 'final':final})
    else:
        timetables=Timetable.objects.filter(eid=eid)
        final='enabled'   
        return render(request, 'timetableinfo.html', { 'timetables' : timetables, 'eid' : eid, 'final':final})
"""def vinvigilatorss(request):
    if request.method == 'POST':
        hello =123
    else :
        return render (request, 'selectexam.html' ,{ 'eid' : eid})
"""
def vpapers (request):
    if request.method == 'POST':
        eid=request.POST['id']
        papers = Papers.objects.filter(eid=eid)
        return render (request, 'vpaper.html' ,{'papers' : papers, 'eid' : eid})
    else :
        eid=request.GET['eid']
        exam= Exam.objects.get(id=eid)
        if exam.studentcheck == 0 :
            return render(request, 'addstudent.html', {'eid' : eid})
        students = Student.objects.filter(eid=eid)
        return render (request, 'studentinfo.html',{'students' : students, 'eid' :eid})


"""def vstudents (request):
    eid=request.POST['eid']
    return render (request, 'vhall.html')
"""
"""def tgenerate (request):
    if request.method == 'POST':
        eid=request.POST['eid']
        halls= Hall.objects.filter(eid=eid)
        invigilators = Invigilator.objects.filter(eid=eid)
        papers = Papers.objects.filter(eid=eid)
        timetables = Timetable.objects.filter(eid=eid)
        students = Student.objects.filter(eid=eid)
        i=0
        for student in students :

            for hall in halls:
                while (i<= hall.hcapacity):
                    iname =123
        return render (request, 'waitingscreen.html' ,{ 'eid' : eid,'students' : students,'papers' : papers, 
        'halls' : halls,'invigilators' : invigilators, })
"""
def edelete (request) :
    if request.method == 'POST' :
        eid = request.POST['id']
        papers = Papers.objects.filter(eid=eid)
        papers.delete();
        students = Student.objects.filter(eid=eid)
        students.delete();
        timetables = Timetable.objects.filter(eid=eid)
        timetables.delete();
        hallstorage = Hallstorage.objects.filter(eid=eid)
        hallstorage.delete();
        sexamstorage = Sexambydate.objects.filter(eid=eid)
        sexamstorage.delete();
        attendance = Attendancestored.objects.filter(eid=eid)
        attendance.delete();
        exam = Exam.objects.get(id=eid)
        exam.delete();
        action ='addpaper'
        exams = Exam.objects.all()
        return render(request, 'selectexam.html', {'action' : action, 'exams' : exams})

"""
def vhallss(request):
    if request.method == 'POST':
        eid=request.POST['eid']
        halls= Hall.objects.filter(eid=eid)
        invigilators = Invigilator.objects.filter(eid=eid)
        papers = Papers.objects.filter(eid=eid)
        timetables = Timetable.objects.filter(eid=eid)
        students = Student.objects.filter(eid=eid)
        return render (request, 'waitingscreen.html' ,{ 'eid' : eid,'students' : students,'papers' : papers, 
        'halls' : halls,'invigilators' : invigilators, })

        return render (request, 'waitingscreen.html' ,{ })
"""
def viewseating (request):
    eid = request.POST['eid']
    tid = request.POST['tid']
    edate = request.POST['edate']
    etime = request.POST['etime']
    allocateinfo = Hallstorage.objects.filter(eid=eid,edate=edate,etime=etime)
    #a=len(allocateinfo)
    #print (a)
    return render (request, 'studentseating.html', { 'allocateinfo' : allocateinfo})


def aaselect(request):
    if request.method == 'POST':
        eid = request.POST['eid']
        #invigilators = Invigilator.objects.filter(eid=eid)
        if Hallstorage.objects.filter(eid=eid, iname = 'UNASSIGNED'):
            timetables = Timetable.objects.filter(eid=eid)
            for timetable in timetables:
                halls = Hallstorage.objects.values('hid').filter(eid=eid, edate=timetable.edate, etime=timetable.etime).distinct();
                for hall in halls:
                    invigilator = Invigilator.objects.order_by('icount')[0]
                    hall1=Hallstorage.objects.filter(eid=eid, edate=timetable.edate , etime=timetable.etime , hid=hall['hid']).update(iid= invigilator.id, iname = invigilator.iname)
                    print(invigilator.iname)
                    invigilator.icount = invigilator.icount+1
                    invigilator.save();
                    #hall1.save()
         
            return render(request, 'aaselect.html', {'eid':eid}) 
        else:
            eid = request.POST['eid']
            return render(request, 'aaselect.html', {'eid':eid})
    else :
        eid= request.GET['eid']
        timetables=Timetable.objects.filter(eid=eid)
        final='enabled'   
        return render(request, 'timetableinfo.html', { 'timetables' : timetables, 'eid' : eid, 'final':final})


