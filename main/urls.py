from django.urls import path , include
from .fun_ajax import  (
                        delete_yonalish,
                        edit_yonalish,
                        get_yonalish,
                        edit_resume,
                        get_resume,
                        )
from .help_views import (
                        logout_ ,
                        RegisterView ,
                        EditProfilView,

                         )
from .views import (
    ProfilUserView,
    ViewsView,
    DevelopersView,
    ServiceView,
    ServiceEditView,
    ProjectView,
    ProjectCreateView,
    service_delete,
    project_delete,
    archive_resume

)

from .help import post_technology, user_ ,Password_reset,ver_code , edit_password
from .pdf import downland_pdf , sped_downland_pdf ,downland_archive_resume
app_name = 'main'


urlpatterns =[

    path('',ViewsView.as_view() , name = 'views'),
    path('user/<str:username>',user_,name='user'),
    path('profil/<int:pk>/<str:username>',ProfilUserView.as_view() , name = 'profil'),
    path('editprofil/<int:pk>',EditProfilView.as_view(),name = 'editprofil'),
    path('developers/<int:pk>',DevelopersView.as_view() , name = 'developers'),
    path('accounts/signup/',RegisterView.as_view() , name = 'register'),
    path('accounts/logout/',logout_, name = 'logout'),

    path('service/<int:pk>',ServiceEditView.as_view() , name = 'service_edit'),
    path('service',ServiceView.as_view() , name = 'service'),
    path('service_delete/<int:pk>',service_delete , name = 'service_delete'),

    path('project/<int:pk>', ProjectView.as_view(), name = 'edit_project'),
    path('project/create', ProjectCreateView.as_view(), name = 'project_create'),
    path('project/delete/<int:pk>', project_delete, name = 'project_delete'),

    path('technology',post_technology , name = 'technology_create'),
    path('get/yonalish',get_yonalish , name = 'get_yonalish'),
    path('delete/yonalish',delete_yonalish , name = 'delete_yonalish'),
    path('edit/yonalish',edit_yonalish , name = 'edit_yonalish'),
    path('pdf',downland_pdf,name='pdf'),
    path('sped_pdf',sped_downland_pdf,name='sped_pdf'),

    path('edit/resume',edit_resume, name='edit_resume'),
    path('get/resume',get_resume, name='get_resume'),
    path('archive_resume',archive_resume, name='archive_resume'),
    path('downland_archive_resume',downland_archive_resume, name='downland_archive_resume'),

    path('password-reset',Password_reset.as_view(), name='password_reset'),
    path('ver-code',ver_code, name='ver_code'),
    path('edit_password',edit_password, name='edit_password'),
]
