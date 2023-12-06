from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from .models import Master , MasterLevel ,CustomUser,Yonalish
from .help import register_ , edit_ ,post_technology #login_ , 

from .decorator import deco_is_authenticated ,deco_user,deco_edit

class RegisterView(View):
    @deco_is_authenticated
    def get(self, request):
        masters = Master.objects.all()
        return render(request,'account/sign-up.html', {"masters":masters,})
    @deco_is_authenticated
    def post(self, request):
        register = register_(request)
        if register:
            return redirect(f'/{request.LANGUAGE_CODE}/')
        return redirect(f'/{request.LANGUAGE_CODE}/register')



def logout_(request):
    logout(request)
    return redirect(f'/{request.LANGUAGE_CODE}/')

class EditProfilView(View):
    # @deco_edit
    # def get(self, request,pk):
    #     masterlevel = MasterLevel.objects.all().prefetch_related('masterlevel').order_by('id')
    #     master =  Master.objects.prefetch_related('masters').all()
    #     return render(request,'edit-profil_user.html',{"masterlevel":masterlevel,'master':master})


    # @deco_edit
    def post(self,request,pk):
        edit = edit_(request,pk)
        return redirect(f'/{request.LANGUAGE_CODE}/profil/{int(pk)}/{request.user.username}')





# class LoginView(View):
#     @deco_is_authenticated
#     def get(self, request):
#         return render(request,'users/login.html')
#     @deco_is_authenticated
#     def post(self, request):
#         login = login_(request)
#         if login:
#             return redirect('/')
#         return render(request,'users/login.html')