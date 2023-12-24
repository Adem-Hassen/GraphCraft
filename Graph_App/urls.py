from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home,name='home'),
    path("user_login/",views.user_login,name='user_login'),
    path("plot/",views.plot,name='plot'),
]
