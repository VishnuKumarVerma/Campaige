from django.contrib import admin
from django.urls import path
from login import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login, name="login"),
    path('afs/',views.afs , name="afs"),
    path('profile/',views.profile , name="profile"),
    path('sign/',views.sign, name="sign"),
    path('', views.home_page, name="home_page"),
    path('groups/',views.groups, name="groups"),
    path('create_follow/',views.create_follow, name="create_follow"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'login.views.error_404'