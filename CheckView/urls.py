"""CheckView URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from polls2.views import index, generate_file, upload_file, formular
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^generate_file/$', generate_file, name='generate_file'),
    url(r'^upload_file/$', upload_file, name='upload_file'),
    url(r'^admin/', admin.site.urls),
    url(r'^formular/$', formular, name='formular'),
]

