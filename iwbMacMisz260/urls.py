"""iwbMacMisz260 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from iwbMacMisz260.views import hello, signup, startpage, profile
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from iwbMacMisz260 import settings
import private_storage.urls
from service.views import NoticePrivateDownloadView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("witaj/", hello),
    path("service/", include("service.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path("signup/", signup, name="signup"),
    path("", startpage, name = "startpage"),
    path("profile", profile, name = "profile"),
    path("private-media/<int:pk>/", NoticePrivateDownloadView.as_view(), name="private-media")
    ]
    
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
