"""bitchatapplication URL Configuration

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

from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('register.urls')),
    url(r'^', include('login.urls')),
    url(r'^', include('user_not_allowed_other_levels.urls')),
    url(r'^', include('saved_answers.urls')),
    url(r'^', include('check_user_active.urls')),
    url(r'^', include('inactivate_user.urls')),
    url(r'^', include('close_test.urls')),
    url(r'^', include('get_clock.urls')),
]
