
from django.shortcuts import redirect ,render
from .models import  CustomUser,Master ,MasterLevel , Yonalish ,Service,Project ,Resume
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .decorator import check_image , deco_is_authenticated ,deco_user ,create_verification_code
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime ,  timedelta

def user_(request,username):
    user  = CustomUser.objects.get(username=username)
    template = loader.get_template('user.html')
    phone = 'None'
    email = 'None'
    github = 'None'
    linkedin = 'None'
    instagram = 'None'
    telegram = 'None'
    if user.phone :
       phone = user.phone
    if  user.email:
       email = user.email
    if  user.github:
       github = user.github
    if  user.linkedin:
       linkedin = user.linkedin
    if  user.instagram:
       instagram = user.instagram
    if  user.telegram:
       telegram = user.telegram



    try:
        resume = user.resumes.get()
        texnalogy = user.users.all().order_by('-percentage')
        context ={
            'phone':phone,
            'email':email,
            'github':github ,
            'linkedin':linkedin,
            'instagram':instagram ,
            'telegram':telegram ,
            'user':user,
            'resume':resume ,
            'texnalogy':texnalogy
        }
        return HttpResponse(template.render(context, request))
    except:
        texnalogy = user.users.all().order_by('-percentage')
        context ={
            'phone':phone,
            'email':email,
            'github':github ,
            'linkedin':linkedin,
            'instagram':instagram ,
            'telegram':telegram ,
            'user':user,
            'texnalogy':texnalogy
        }
        return HttpResponse(template.render(context, request))


def register_(request):
    username = str(request.POST['username'])
    first_name = str(request.POST['first_name'])
    last_name = str(request.POST['last_name'])
    phone = str(request.POST['phone'])
    master= int(request.POST['master'])
    email = str(request.POST['email'])
    password1= str(request.POST['password1'])
    password2= str(request.POST['password2'])

    master = Master.objects.get(id=master)

    if len(password1) < 8:
        messages.error(request, "Parol 8 ta belgidan kam bo'lmasligi kerak !")
        return False

    if password1 != password2:
        messages.error(request, "Parollar bir xil emas !")
        return False

    user = CustomUser.objects.filter(username=username)
    if user.exists():
        messages.error(request, "Bu username oldin ro'yxatdan o'tgan !")
        return False

    if user:
        if user[0].phone == phone:
            messages.error(request, "Bu telefon raqam oldin ro'yxatdan o'tgan !")
            return False

    if master == 0:
        messages.error(request, "Categoriya belgilashda xatolik ! ")
        return False

    user = CustomUser.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password1,
            email=email,
            master=master,
        )
    return True




def edit_(request,pk):
    last_name = str(request.POST.get('last_name'))
    first_name = str(request.POST.get('first_name'))
    email = str(request.POST.get('email'))
    phone = str(request.POST.get('phone'))

    instagram= str(request.POST.get('instagram'))
    linkedin = str(request.POST.get('linkedin'))
    github = str(request.POST.get('github'))
    telegram = str(request.POST.get('telegram','None'))
    master = request.POST.get('master',False)
    masterlevel = request.POST.get('masterlevel')
    ok = request.POST.get('ok')
    birthday = str(request.POST.get('birthday',None))

    user = request.user
    img = request.FILES.get('img',None)
    img = user.img if img == None else check_image(img)

    master = Master.objects.get(id=int(master))
    user.master = master
    masterlevel = MasterLevel.objects.get(id=int(masterlevel))
    user.masterlevel = masterlevel
    user.last_name = last_name
    user.first_name = first_name
    user.instagram = instagram
    user.linkedin = linkedin
    user.github = github
    user.telegram= telegram
    user.birthday = birthday
    user.phone = phone
    user.email = email
    user.img = img
    ok =  True if ok == 'on' else False

    user.ok = ok
    user.save()
    return True

class Password_reset(View):
    def get(self,request):
        from django.utils import timezone

        now = timezone.now() + timedelta(minutes=292)
        try :
            email_login = request.GET.get('login')
            user = CustomUser.objects.get(Q(username=email_login)|Q(email=email_login))
            if user :
                verification_code = create_verification_code()

                request.session['id'] = user.id
                request.session['verification_code'] = verification_code
                request.session['time'] = f"{now.year} {now.month} {now.day} {now.hour }:{now.minute }:{now.second}"
                print(request.session['verification_code'])
                send_mail (subject = 'sizning mahfi codingiz  ',message=verification_code,from_email=settings.EMAIL_HOST_USER,recipient_list=[user.email])
                return redirect(f'/{request.LANGUAGE_CODE}/ver-code')
        except:
            messages.success(request, "?  not found login or email ")
            return redirect(f'/{request.LANGUAGE_CODE}/accounts/login')

def ver_code(request):
    return render(request,'account/ver-code.html')


def edit_password(request):
    id = request.session['id']
    password = request.POST.get('password_1')
    password_2 = request.POST.get('password_2')
    if password == password_2:
        user = CustomUser.objects.get(id=int(id))
        user.set_password(password)
        user.save()
        messages.success(request, "password reset")
    return redirect(f'/{request.LANGUAGE_CODE}')


def post_technology(request):
    technology = str(request.GET.get("technology"))
    percentage = int(request.GET.get("percentage"))

    if percentage > 100:
        percentage = 100
    user = request.user
    Yonalish.objects.create(user=user,technology=technology,percentage=int(percentage))

    return redirect (f'/{request.LANGUAGE_CODE}/profil/{request.user.id}/{request.user.username}#technology')

def create_service(request):
    icon = str(request.POST['icon'])
    name = str(request.POST['service_name'])
    text = str(request.POST['service_text'])
    user = request.user
    service = Service.objects.create(user=user ,name=name, text = text,icon=icon)
    if service:
        messages.success(request, "service created !")
        return redirect (f'/{request.LANGUAGE_CODE}/profil/{request.user.id}/{request.user.username}')
    return False

def edit_service(request,pk):
    name = str(request.POST.get('service_name'))
    text = str(request.POST.get('service_text'))
    service = Service.objects.get(id=pk)
    service.name = name
    service.text = text
    service.save()
    return True

def project_edit(request,pk):
    img = (request.FILES.get('img',False))
    name = str(request.POST.get('project_name',None))
    text = str(request.POST.get('project_text',None))
    github = str(request.POST.get('github',None))
    live_link = str(request.POST.get('live_link',None))
    project = Project.objects.filter(id=pk)[0]
    if img != False:
        project.image = img
    if name :
        project.name = name
    if text:
        project.title = text
    if github:
        project.github = github
    if live_link:
        project.live_link = live_link
    project.save()
    return True

def project_create(request):
    img = request.FILES.get('img')
    id = int(request.POST.get('user_id'))
    name = str(request.POST.get('project_name'))
    title = request.POST.get('title')
    github = str(request.POST.get('github'))
    live_link = str(request.POST.get('live_link'))
    user = CustomUser.objects.get(id=id)
    if Project.objects.filter(user=user.id).count() >= 6 :
        return False
    Project.objects.create(
        user=user,
        name=name,
        title=title,
        image=img,
        github=github,
        live_link=live_link,
    )
    return True




# def login_(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     if username and password:
#             try:
#                 user = authenticate(request, username=username, password=password)
#                 if user is not None:
#                     login(request,user)
#                     return True
#             except:
#                 return False
#     messages.error(request, "Login yoki parol xato !")