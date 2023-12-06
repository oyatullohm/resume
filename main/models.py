from django.db import models
from django.contrib.auth.models import AbstractUser


from django.conf import settings



class Master(models.Model):
    """ user mutahasisligini belglovchi klass  buni ozimiz oldindan bazaga saqlaymiz  """
    img = models.ImageField(upload_to = 'master_images',null = True, blank = True)
    name = models.CharField('category',max_length=55)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    phone = models.CharField("Telefoni",max_length=14)
    instagram = models.CharField('instagramlink',max_length=318,null = True, blank = True)
    linkedin = models.CharField('linkedinlink',max_length=318,null = True, blank = True)
    github = models.CharField('githublink',max_length=155,null = True, blank = True)
    birthday = models.CharField(max_length=15,null=True,blank=True)
    telegram = models.CharField('telegram url manzili',max_length=255,null = True, blank = True)
    img = models.ImageField(upload_to = 'user_images',null = True, blank = True)
    ok = models.BooleanField(default=False,null = True, blank = True)
    master = models.ForeignKey(Master, related_name='masters', on_delete = models.PROTECT,null = True, blank = True)
    masterlevel = models.ForeignKey('MasterLevel', on_delete = models.PROTECT,null = True, blank = True,related_name = 'masterlevel')


class MasterLevel(models.Model):
    level = models.CharField('masterni darajasi ',max_length=50)
    def __str__(self):
        return self.level



class Yonalish(models.Model):
    """  tehnalogyani qay darajada bladi shuni anig'lovchi class    """
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE,related_name='users')
    technology = models.CharField('texnalogiya nomi ',max_length=155)
    percentage = models.PositiveIntegerField('bilim darajasi   maximum 100 ',default = 0 )
    def __str__(self):
        return self.technology


class Service(models.Model):
    """ developer qanaqa  xizmat ko'rsata  oladi  """
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE,related_name='services')
    icon = models.CharField(max_length=55)
    name = models.CharField('hizmat turi ',max_length=55)
    text = models.TextField('batafsil malumot')
    def __str__(self):
        return self.text


class Project(models.Model):
    """developer ni  portfolio   qilgan ishlaridan namuna """
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE,related_name='projects')
    image = models.ImageField("poroject rasmi",upload_to="project_images")
    name = models.CharField(max_length=55)
    title =  models.TextField()
    github = models.CharField('url manzili  gitgub manzili' ,max_length=255,null=True,blank=True)
    live_link = models.CharField('live preview manzili' ,max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name


class Resume(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE,related_name='resumes')
    addres =  models.CharField('addres',max_length=255,null=True,blank=True)
    education =  models.CharField('unversitet',max_length=255,null=True,blank=True)
    skills = models.TextField('Konikma',null=True, blank=True)
    experience = models.TextField('Tajriba',null=True, blank=True)
    hobbies = models.CharField('qiziqish',max_length=500,null=True,blank=True)
    about = models.TextField('about',null=True, blank=True)
    def __str__(self):
         return self.hobbies

class Sped_resume(models.Model):
    name = models.CharField('name',max_length=55)
    phone = models.CharField('phone',max_length=55)
    email = models.CharField('email',max_length=155)
    addres =  models.CharField('addres',max_length=155)
    birthday = models.DateField()
    education =  models.CharField('unversitet',max_length=155)
    skills = models.TextField('Konikma')
    experience = models.TextField('Tajriba')
    hobbies = models.CharField('qiziqish',max_length=500)
    about = models.TextField('about')
class Contact(models.Model):
    first_name = models.CharField('mijoz ismi ',max_length=55)
    last_name = models.CharField('mijoz familyasi ',max_length=55)
    email = models.EmailField('email')
    message = models.TextField('habar matni ')
    status = models.BooleanField(default=False,null=True, blank=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "contactlar"

    def __str__(self):
        return self.first_name
