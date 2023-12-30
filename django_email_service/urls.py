"""django_email_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('email_service/', include('email_service.urls')),
    path('email_service/token/auth', CustomAuthToken.as_view()),
    # path('users/create', CreateUserView.as_view()),
    # path('users/change-password/', ChangePasswordView.as_view(), name='change-password'),
]

# Add the following line for serving media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
