from django.contrib import admin
from .models import (
    MasterLevel,
    CustomUser,
    Yonalish,
    Service,
    Resume,
    Contact,
    Project,
    Master,
    Sped_resume
)
# Register your models here.


admin.site.register(MasterLevel)
admin.site.register(CustomUser)
admin.site.register(Yonalish)
admin.site.register(Service)
admin.site.register(Resume)
admin.site.register(Contact)
admin.site.register(Project)
admin.site.register(Master)
admin.site.register(Sped_resume)

# from django.utils.safestring import mark_safe

# @admin.register(Icon)
# class IconAdmin(admin.ModelAdmin):
#     list_display =  ['id','icon']
#     def get_image(self,obj):
#         return mark_safe(f"<img src = '{obj.image.url}' width = '150px' >")
