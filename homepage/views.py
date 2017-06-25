from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.http import HttpResponse
from .forms import uform
from .models import Myusr, Student, Teacher
from django.http import Http404


def index(request):
    return render(request, 'homepage/index.html')


def base(request):
    return render(request, 'homepage/index1.html')

def application(request):
    return render(request, 'homepage/application.html')
	
def index1(request):
	return render(request, 'homepage/index1.html')


def detail(request):
    return render(request, 'homepage/detail.html')


def logout_user(request):
    logout(request)
    form = uform(request.POST or None)
    return render(request, 'homepage/login.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                obj = Myusr.objects.get(user=request.user)
                u = obj.cat
                if u == 1:
                    return redirect('homepage:index1')
                else:
                    stud = Student.objects.get(user=request.user)
                    if stud.check == 0:
                        return redirect('homepage:index')
                    else:
                        return redirect('homepage:index')

            else:
                return render(request, 'homepage/login.html')
        else:
            return render(request, 'homepage/login.html')
    return render(request, 'homepage/login.html')


class userformview(View):
    form_class = uform
    template_name = 'homepage/register.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            uid = form.cleaned_data['uid']

            if form.cleaned_data['password'] != form.cleaned_data['cpassword']:
                return HttpResponse("passwords dont match")
            else:
                password = form.cleaned_data['password']
                cpassword = form.cleaned_data['cpassword']
                user.set_password(password)
                user.save()
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        u = Myusr()
                        u.user = request.user
                        u.cat = 0
                        print(uid)
                        u.save()
                        s = Student()
                        s.s_id = uid						
                        s.user = request.user
                        obj=Student.objects.all()
                        c=0
                        for ob in obj:
                            c=c+1
                        c=c+1
                        s.g_id=c
                        s.save()
                        return render(request, 'homepage/index.html')
                    else:
                        return HttpResponse("registration failed")
                else:
                    return HttpResponse("registration failed")
        else:
            return HttpResponse("registration failed")


def student_request(request):
    ch = request.POST.get('option')
    print(ch)
    # s_id = request.POST.get('s_id')
    title = request.POST.get('title')
    student1 = request.POST.get('student1')
    student2 = request.POST.get('student2')
    student3 = request.POST.get('student3')
    abstract = request.POST.get('abstract')
    amt = request.POST.get('amt')
    fund_approved = request.POST.get('fund_approved')
    stage = request.POST.get('stage')
    user_obj = Student.objects.get(user=request.user)
    user_obj.t_id = ch
    user_obj.status=4
    # user_obj.s_id=s_id
    user_obj.title = title
    user_obj.abstract = abstract
    user_obj.amt = amt
    user_obj.fund_approved = fund_approved
    user_obj.stage = stage
    user_obj.check = 1
    user_obj.student1=student1
    user_obj.student2=student2
    user_obj.student3=student3
    user_obj.save()


    s = Student.objects.get(user=request.user)
    if s.status == 4:
        str = "Your application is awaiting assessment by the mentor."
    if s.status == 0:
        str = "Sorry,Your Application has been rejected<br> Reason : "+s.rej+""
    if s.status == 1:
        str = "Your Application has been approved by the mentor and is sent to the HOD for approval"
    if s.status == 5:
        str = "You haven't filled the form yet"
    return render(request, 'homepage/studenthome.html', {'str': str})


def notify(request):
    us = Teacher.objects.get(user=request.user)
    v = us.teacher_id
    students = Student.objects.filter(t_id=v).filter(status=4)
    c = 0
    flag = 0
    flag1 = 0
    for s in students:
        c = c + 1
        print(s.s_id)
    if c == 0:
        flag1 = 1
    else:
        flag = 1
    context = {'students': students, 'flag': flag, 'flag1': flag1}
    return render(request, 'homepage/teacherhome.html', context)


def	rejectform(request,sid2):
    sid=sid2
    context={'sid':sid}	
    return render(request,'homepage/rejectform.html',context)
	
	
def reject(request, sid):
    s = Student.objects.get(s_id=sid)
    s.status = 0
    res=request.POST.get('reason')
    s.rej=res
    s.save()
    print(s.status)
    print("hey")
    f = 4
    students = Student.objects.filter(status=f)
    c = 0
    flag = 0
    flag1 = 0
    for so in students:
        c = c + 1
        print("hii")
    if c == 0:
        flag1 = 1
        print("smruti")
    else:
        flag = 1
        print("sam")
    context = {'students': students, 'flag': flag, 'flag1': flag1}
    return render(request, 'homepage/teacherhome.html', context)


def accept(request, sid1):
    s = Student.objects.get(s_id=sid1)
    s.status = 1
    s.save()
    print(s.status)
    f = 4
    students = Student.objects.filter(status=f)
    c = 0
    flag = 0
    flag1 = 0
    for so in students:
        c = c + 1
        print("hii")
    if c == 0:
        flag1 = 1
        print("smruti")
    else:
        flag = 1
        print("sam")
    context = {'students': students, 'flag': flag, 'flag1': flag1}
    return render(request, 'homepage/teacherhome.html', context)


# return HttpResponse("Your Application has been approved by the mentor and is sent to the HOD for approval ")

# return HttpResponse("Sorry,Your Application has been rejected")


def check(request):
    s = Student.objects.get(user=request.user)
    if s.status == 5:
        str = "You haven't filled the form yet."
    if s.status == 4:
        str = "Your application is awaiting assessment by the mentor."
    if s.status == 0:
        str = "Sorry, your Application has been rejected Reason : "+s.rej+""
    if s.status == 1:
        str = "Your Application has been approved by the mentor and is sent to the HOD for approval"
    return render(request, 'homepage/studenthome.html', {'str': str})


def retrievestud(request):
    te=""
    s = Student.objects.get(user=request.user)
    if s.t_id == 1:
        te = "ABC"
    if s.t_id == 2:
        te = "BCD"
    if s.t_id == 3:
        te = "CDE"
    if s.t_id == 4:
        te = "DEF"
    if s.t_id == 5:
        te = "EFG"
    return render(request, 'homepage/studdata.html', {'s': s, 'te': te})

	
	
def alll(request):
    us = Teacher.objects.get(user=request.user)
    v = us.teacher_id
    students = Student.objects.filter(t_id=v).exclude(status=4)
    for s in students:
        print(s.status)
        print("ff")
    return render(request,'homepage/ppl.html',{'s':students})
	
	
	# context = {'students': students, 'flag': flag, 'flag1': flag1}
    # return render(request, 'homepage/teacherhome.html', context)
