
from django.contrib import admin
from django.urls import path,include ,re_path
from django.conf import settings
from django.conf.urls.static import static 

from django.views.static import serve as mediaserve

from django.conf.urls import handler404,handler500
from main.views import handler_404,handler_500
from django.conf.urls.i18n import i18n_patterns
from main.views import ViewsView
urlpatterns = [
    path('',ViewsView.as_view(),name='views'),
    path('/i18n/',include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('',include('main.urls',namespace='main')),
    path('accounts/', include('allauth.urls')),

)


if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls'))
    ]


urlpatterns += [
        re_path(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$', mediaserve, {'document_root': settings.MEDIA_ROOT}),
        re_path(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$', mediaserve, {'document_root': settings.STATIC_ROOT}),
    ]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404=handler_404
handler500=handler_500