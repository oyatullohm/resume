from django.shortcuts import render,redirect
from django.views import View
from .models import (
    CustomUser,
    Yonalish,
    Service,
    Project,
    Contact,
    Master,
    MasterLevel,
    Sped_resume
)
from .decorator import deco_login ,deco_user ,deco_edit

from django.contrib import messages
from .help import (
                   register_,
                   create_service,
                   edit_service,
                   project_edit,
                   project_create
                   )


class ViewsView(View):
    def get(self,request):
        master = Master.objects.all().prefetch_related('masters')
        context = {
                    "master":master,
                    }
        return render(request, 'index.html',context)
    def post(self,request):

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if  message :
            Contact.objects.create(first_name=first_name,last_name=last_name,email=email,message=message)
            messages.success(request, "Sent Message !")
        return redirect(f'/{request.LANGUAGE_CODE}')

class ProfilUserView(View):
    @deco_edit
    def get(self,request,pk,username):
        service = Service.objects.filter(user=pk)
        project = Project.objects.filter(user=pk)
        user = CustomUser.objects.get(id=pk)
        masterlevel = MasterLevel.objects.all().prefetch_related('masterlevel').order_by('id')
        master =  Master.objects.all()
        category =  Yonalish.objects.filter(user=pk).order_by('-percentage')
        context = {
                    'category':category,
                    'user':user,
                    'service':service,
                    'project':project,
                    "masterlevel":masterlevel,
                    'master':master,
                   }

        return render(request, 'edit_profil_user.html',context)
from django import template


class DevelopersView(View):
    def get(self,request,pk):
        if pk == 0:
            developers = CustomUser.objects.prefetch_related('master','users','masterlevel').filter(ok=True)
        else:
            developers = CustomUser.objects.prefetch_related('master','users','masterlevel').filter(master=pk ,ok=True).order_by('username')
        context = {"developers":developers,
                    }

        return render(request, 'list_user.html',context )




class ServiceView(View):
    def post(self,request):
        id = request.user.id
        c = create_service(request)
        return redirect(f'/{request.LANGUAGE_CODE}/profil/{id}/{request.user.username}')

class ServiceEditView(View):
    def post(self, request, pk):
        id = request.user.id
        edit_service(request,pk)
        return redirect(f'/{request.LANGUAGE_CODE}/profil/{id}/{request.user.username}')

def service_delete(request,pk):
    service =  Service.objects.get(id= int(pk))
    service.delete()
    messages.success(request, "service deleted !")
    return redirect(f'/{request.LANGUAGE_CODE}/profil/{request.user.id}/{request.user.username}')



class ProjectView(View):

    def post(self, request, pk):
        project_edit(request, pk)
        messages.success(request, "Project info changed !")
        return redirect(f'/{request.LANGUAGE_CODE}/profil/{request.user.id}/{request.user.username}')

class ProjectCreateView(View):
    def post(self, request):
        project =  project_create(request)
        if project == False:
            messages.success(request, "sizda projectlar soni max 6  !")
            return redirect(f'/{request.LANGUAGE_CODE}/profil/{request.user.id}/{request.user.username}')
        messages.success(request, "Created successfully !")
        return redirect(f'/{request.LANGUAGE_CODE}/profil/{request.user.id}/{request.user.username}')

def project_delete(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    messages.success(request, "The project has been deleted !") 
    return redirect(f'/{request.LANGUAGE_CODE}/profil/{request.user.id}/{request.user.username}')

def archive_resume (request):
    resume = Sped_resume.objects.all().order_by('id')
    return render(request,'archive_resume.html',{'resume':resume})



def handler_404(request,exception):
    return render(request, "404.html")

def handler_500(request):
    return render(request, "500.html")