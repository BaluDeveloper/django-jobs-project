"""jobsProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from jobsApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
    #url(r'^hydjobs/',views.hyd_jobs),
    #url(r'^punejobs/',views.pune_jobs),
    #url(r'^delhijobs/',views.delhi_jobs),
    url(r'^hydjobs/',views.jobs),
    url(r'^punejobs/',views.jobs),
    url(r'^delhijobs/',views.jobs),

]
