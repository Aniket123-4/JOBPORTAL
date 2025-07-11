from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date

# Create your views here.

def index(request):
    return render(request, 'index.html')

def admin_login(request):
    error=""
    if request.method=="POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d ={'error' :error}
    return render(request, 'admin_login.html',d)


def user_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['email'];
        p = request.POST['pwd'];
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = StudentUser.objects.get(user=user)
                if user1.type == "student":
                    login(request, user)
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"
        else:
            error = "yes"
    d = {'error': error}
    return render(request, 'user_login.html', d)


def recruiter_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname'];
        p = request.POST['pwd'];
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = Recruiter.objects.get(user=user)
                if user1.type == "recruiter" and user1.status!="pending":
                    login(request, user)
                    error = "no"
                else:
                    error = "not"
            except:
                error = "yes"
        else:
            error = "yes"
    d = {'error': error}
    return render(request, 'recruiter_login.html',d)

def recruiter_signup(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        gen = request.POST['gender']
        con = request.POST['contact']
        company = request.POST['company']
        try:
            user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
            Recruiter.objects.create(user=user, mobile=con, image=i, gender=gen,company=company, type="recruiter",status="pending")
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'recruiter_signup.html',d)


def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    student = StudentUser.objects.get(user=user)
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        gen = request.POST['gender']
        con = request.POST['contact']
        student.user.first_name = f
        student.user.last_name = l
        student.mobile = con
        student.gender = gen
        try:
            student.save()
            student.user.save()
            error = "no"
        except:
            error = "yes"
        try:
            i = request.FILES['image']
            student.image = i
            student.save()
            error = "no"
        except:
            pass
    d = {'student': student, 'error': error}
    return render(request, 'user_home.html',d)

def admin_home(request):
    if not request.user.is_authenticated:
       return redirect('admin_login')
    rcount = Recruiter.objects.all().count()
    scount = StudentUser.objects.all().count()
    d = {'rcount':rcount,'scount':scount}
    return render(request, 'admin_home.html',d)

def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        gen = request.POST['gender']
        con = request.POST['contact']
        recruiter.user.first_name = f
        recruiter.user.last_name = l
        recruiter.mobile = con
        recruiter.gender= gen
        try:
            recruiter.save()
            recruiter.user.save()
            error = "no"
        except:
            error = "yes"
        try:
            i = request.FILES['image']
            recruiter.image = i
            recruiter.save()
            error = "no"
        except:
            pass
    d = {'recruiter':recruiter,'error':error}
    return render(request, 'recruiter_home.html',d)

def Logout(request):
    logout(request)
    return redirect('index')


def user_signup(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        gen = request.POST['gender']
        con = request.POST['contact']
        try:
            user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
            StudentUser.objects.create(user=user, mobile=con, image=i, gender=gen, type="student")
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'user_signup.html', d)

def view_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = StudentUser.objects.all()
    d = {'data':data}
    return render(request, 'view_users.html',d)

def delete_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    student = User.objects.get(id=pid)
    student.delete()
    return redirect('view_users')

def delete_recruiter(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    recruiter =User.objects.get(id=pid)
    recruiter.delete()
    return redirect('recruiter_all')


def recruiter_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='pending')
    d = {'data':data}
    return render(request, 'recruiter_pending.html',d)

def change_status(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    recruiter = Recruiter.objects.get(id=pid)
    if request.method=="POST":
        s = request.POST['status']
        recruiter.status=s
        try:
            recruiter.save()
            error="no"
        except:
            error="yes"
    d = {'recruiter':recruiter,'error':error}
    return render(request, 'change_status.html',d)

def recruiter_accepted(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='Accept')
    d = {'data':data}
    return render(request, 'recruiter_accepted.html',d)

def recruiter_rejected(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='Reject')
    d = {'data':data}
    return render(request, 'recruiter_rejected.html',d)

def recruiter_all(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.all()
    d = {'data':data}
    return render(request, 'recruiter_all.html',d)

def add_job(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error=""
    if request.method == 'POST':
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        sal = request.POST['salary']
        l = request.FILES['logo']
        exp = request.POST['experience']
        loc = request.POST['location']
        skills = request.POST['skills']
        des = request.POST['description']
        user = request.user
        recruiter = Recruiter.objects.get(user=user)
        try:
            job.objects.create(recruiter=recruiter,start_date=sd,end_date=ed,title=jt,salary=sal,image=l,description=des,experience=exp,locaton=loc,skills=skills,creationdate=date.today())
            error="no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request,'add_job.html',d)

def job_list(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    Job = job.objects.filter(recruiter=recruiter)
    d = {'Job':Job}
    return render(request, 'job_list.html',d)

def edit_jobdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error=""
    Job = job.objects.get(id=pid)
    if request.method == 'POST':
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        sal = request.POST['salary']
        exp = request.POST['experience']
        loc = request.POST['location']
        skills = request.POST['skills']
        des = request.POST['description']

        Job.title =jt
        Job.salary = sal
        Job.experience = exp
        Job.locaton = loc
        Job.skills = skills
        Job.description = des
        try:
            Job.save()
            error="no"
        except:
            error = "yes"
            if sd:
                try:
                    Job.start_date = sd
                    Job.save()
                except:
                    pass
            else:
                pass
            if ed:
                try:
                    Job.end_date = ed
                    Job.save()
                except:
                    pass
            else:
                pass

    d = {'error': error,'Job':Job}
    return render(request,'edit_jobdetail.html',d)

def change_companylogo(request,pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error=""
    Job = job.objects.get(id=pid)
    if request.method == 'POST':
        cl = request.FILES['logo']

        Job.image = cl
        try:
            Job.save()
            error="no"
        except:
            error = "yes"
    d = {'error': error,'Job':Job}
    return render(request,'change_companylogo.html',d)

def latest_job(request):
    Job = job.objects.all().order_by('-start_date')
    d = {'Job':Job}
    return render(request,'latest_job.html',d)

def user_latestjob(request):
    Job = job.objects.all().order_by('-start_date')
    user = request.user
    student = StudentUser.objects.get(user=user)
    data = Apply.objects.filter(student=student)
    li=[]
    for i in data:
        li.append(i.jobs.id)
    d = {'Job':Job,'li':li}
    return render(request,'user_latestjob.html',d)

def job_detail(request,pid):
    Job = job.objects.get(id=pid)
    d = {'Job':Job}
    return render(request,'job_detail.html',d)

def applyforjob(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""
    user = request.user
    student = StudentUser.objects.get(user=user)
    Job = job.objects.get(id=pid)
    date1 = date.today()
    if Job.end_date <date1:
        error="close"
    elif Job.start_date > date1:
        error="notopen"
    else:
        if request.method == 'POST':
            r = request.FILES['resume']
            Apply.objects.create(jobs=Job,student=student,resume=r,applydate=date.today())
            error="Done"
    d = {'error': error}
    return render(request,'applyforjob.html',d)

def applied_candidatelist(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')

    data = Apply.objects.all()

    d = {'data': data}
    return render(request,'applied_candidatelist.html',d)

def contact(request):
    return render(request,'contact.html',)




from django.shortcuts import render

# Create your views here.
