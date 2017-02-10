"""learn_models URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from people.views import login,checkLogin,register,registerUI,index,login_Out,student_List,show_Password,detail,delete,detailUI

urlpatterns = [
	url(r'^detailUI/(?P<aid>\d+)/', detailUI, name="detailUI"),
	url(r'^detail/(?P<aid>\d+)/', detail, name="detail"),
	url(r'^delete/(?P<aid>\d+)/', delete, name="delete"),
	url(r'^show_Password/(?P<aid>\d+)/', show_Password, name="show_Password"),
	url(r'^student_List/', student_List, name="student_List"),
	url(r'^login_Out/', login_Out, name="login_Out"),
	url(r'^registerUI/', registerUI, name="registerUI"),
	url(r'^checkLogin/', checkLogin, name="checkLogin"),
	url(r'^register/', register, name="register"),
	url(r'^index/', index, name="index"),
	url(r'^login/', login, name="login"),
    url(r'^admin/', admin.site.urls),
]
