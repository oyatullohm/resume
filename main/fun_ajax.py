from django.http import JsonResponse
from django.shortcuts import redirect
from django.db.models import Q
from .models import Yonalish , Service , Resume   #Contact
from django.contrib import messages

def edit_yonalish(request):
    id =  request.GET.get('id')
    y = Yonalish.objects.get(id=id)
    technology = request.GET.get('technology')
    percentage = request.GET.get('percentage')
    if technology:
        pass
    else:
        technology = y.technology
    if percentage:
        pass
    else:
        percentage = y.percentage
    y.technology = technology
    y.percentage = percentage
    y.save()
    return JsonResponse({'status':'ok','percentage':y.percentage,'technology':y.technology})

def delete_yonalish(request):
    id =  request.GET.get('id')
    Yonalish.objects.filter(id=id).delete()
    return JsonResponse({'status':'ok'})

def get_yonalish(request):
    id = request.GET.get('id')
    yonalish =  Yonalish.objects.get(id=int(id))
    return JsonResponse({'status':'ok','technology':yonalish.technology,'percentage':yonalish.percentage,'id':yonalish.id})


def edit_resume(request):
    print(000000)
    print(000000)
    print(000000)
    print(000000)
    print(000000)
    print(000000)
    user = request.user
    education = request.GET.get('education',None)
    skills = request.GET.get('skills')
    experience = request.GET.get('experience',None)
    about = request.GET.get('about',None)
    hobbies = request.GET.get('hobbies',None)
    resume = user.resumes.all()
    if resume:
        print(1)
        print(1)
        print(1)
        print(1)
        index = len(resume)
        resume = resume[index-1]
        resume.education = education
        resume.skills = skills
        resume.experience = experience
        resume.hobbies = hobbies
        resume.about = about
        resume.save()
        # messages.success(request, "edit resume !")
        return JsonResponse({'status': 'ok'})
    Resume.objects.create(
        user=user,education=education,
        skills=skills,hobbies=hobbies,
        about=about
    )
    print(2)
    print(2)
    print(2)
    print(2)
    # messages.success(request, "resume created !")
    return JsonResponse({'status': 'ok'})

def get_resume(request):
    print(3333)
    print(3333)
    print(3333)
    print(3333)
    user= request.user
    resume = user.resumes.all()
    if resume:
        index = len(resume)
        r = resume[index-1]
        resume = {'education':r.education,
                  'skills':r.skills,
                  'experience':r.experience,
                  'hobbies':r.hobbies,
                  'about':r.about
                  }

        return JsonResponse({'status': 'ok','resume':resume})
    print(4444)
    return JsonResponse({'status': 'ok'})



# def edit_msg_status(request, pk):
#     msg = Contact.objects.get(id=pk)
#     resp = request.GET.get('msg_status')
#     if resp == "true":
#         msg.status = True
#         msg.save()
#         return JsonResponse({"msg":"True"})
#     elif resp == "false":
#         msg.status = False
#         msg.save()
#         return JsonResponse({"msg":"False"})
#     else:
#         return JsonResponse({"msg":"not valid"})

