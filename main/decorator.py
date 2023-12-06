from PIL import Image
from .models import CustomUser
from django.shortcuts import redirect


def deco_is_authenticated(fun):
    def wrapper(self,request,*args,**kwarga):
        if request.user.is_authenticated:
            return redirect(f'/user/{request.user.username}')
        return fun(self,request,*args,**kwarga)
    return wrapper

def deco_user(fun):
    def wrapper(self,request,pk,username,*args,**kwargs):
        if request.user.pk == pk:
            return fun(self ,request ,pk,username,*args, **kwargs)
        return redirect(f'/user/{username}')
    return wrapper


def deco_edit(fun):
    def wrapper(self,request,pk,username,*args,**kwarga):
        if request.user.id == pk:
            return fun(self,request,pk,username=None,*args,**kwarga)
        return redirect('main:views')
    return wrapper



def deco_login(fun):
    def wrapper(self,request,pk,*args,**kwargs):
        user =  CustomUser.objects.get(id=pk)
        if request.user.is_authenticated and request.user == user :
            return fun(self, request, pk,*args, **kwargs)
        return redirect('main:views')
    return wrapper


def check_image(filename):
    if filename != False:
        img = Image.open(filename)
        print(img.format)
        if img.format.lower() in ['png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif']:
            return filename
    return False
import random
def create_verification_code():
    return "".join(random.sample([str(num) for num in range(0,10) ], 6 ))




