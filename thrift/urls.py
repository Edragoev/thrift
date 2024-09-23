from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("signup", views.signup, name='signup'),
    path("login_user", views.login_user, name='login_user'),
    path("purpose", views.purpose, name='purpose'),
    path("upload_item", views.upload_item, name='upload_item'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
