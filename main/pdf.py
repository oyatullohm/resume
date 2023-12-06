from .models import CustomUser
from django.http import HttpResponse
from io import BytesIO
from django.shortcuts import render
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from .models import CustomUser , Resume ,Sped_resume


def render_to_pdf(template_src,context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    return None




def downland_pdf(request):
    user_id = request.POST.get('user_id')
    resume_id = request.POST.get('resume_id')
    user = CustomUser.objects.get(id=user_id)
    resume = Resume.objects.get(id=resume_id)
    data =  {
        'name':user.username,
        'phone':user.phone,
        'email':user.email,
        'birthday':user.birthday,
        'about':resume.about,
        'education':resume.education,
        'skills':resume.skills,
        'experience':resume.experience,
        'hobbies':resume.hobbies
    }
    pdf = render_to_pdf('pdf.html',data)
    response = HttpResponse(pdf,content_type='application/pdf')
    filename = "Invoice_%s.pdf" %("12341231")
    content = "attachment; filename='%s'"%(filename)
    response["Content-Dispositon"] = content
    return response

def sped_downland_pdf(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    address = request.POST.get('addres')
    birthday = request.POST.get('birthday')
    education = request.POST.get('education')
    skills = request.POST.get('skills')
    experience = request.POST.get('experience')
    about = request.POST.get('about')
    hobbies = request.POST.get('hobbies')

    sped_resume = Sped_resume.objects.get_or_create(
        name=name,
        phone=phone,
        email=email,
        addres=address,
        birthday=birthday,
        education=education,
        skills=skills,
        experience=experience,
        about=about,
        hobbies=hobbies
    )
    data =  {
        'id' :sped_resume[0].id,
        'name':name,
        'phone':phone,
        'email':email,
        'addres':address,
        'birthday':birthday,
        'education':education,
        'skills':skills,
        'experience':experience,
        'about':about,
        'hobbies':hobbies
    }
    pdf = render_to_pdf('pdf.html',data)
    response = HttpResponse(pdf,content_type='application/pdf')
    filename = "Invoice_%s.pdf" %("12341231")
    content = "attachment; filename='%s'"%(filename)
    response["Content-Dispositon"] = content
    return response


def downland_archive_resume(request):
    id = request.GET.get('id')
    resume = Sped_resume.objects.get(id=int(id))
    data =  {
        'id' :resume.id,
        'name':resume.name,
        'phone':resume.phone,
        'email':resume.email,
        'addres':resume.addres,
        'birthday':resume.birthday,
        'education':resume.education,
        'skills':resume.skills,
        'experience':resume.experience,
        'about':resume.about,
        'hobbies':resume.hobbies
    }

    pdf = render_to_pdf('pdf.html',data)
    response = HttpResponse(pdf,content_type='application/pdf')
    filename = "Invoice_%s.pdf" %("12341231")
    content = "attachment; filename='%s'"%(filename)
    response["Content-Dispositon"] = content
    return response