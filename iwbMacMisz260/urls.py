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
from iwbMacMisz260.views import hello, signup, startpage
from django.urls.conf import include, re_path
from django.contrib.auth import views as auth_views
from iwbMacMisz260 import settings
import private_storage
from private_storage.views import PrivateStorageDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("witaj/", hello),
    path("service/", include("service.urls")),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", signup, name="signup"),
    path("start/", startpage, name = "startpage")]
#   path("private-media/<int:pk>/", NoticePrivateDownloadView.as_view(), name= "private-media")]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
