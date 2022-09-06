"""anliproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls import include
from anli import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name="home"),
    path('user/', include('user.urls')),
    path('detail/<str:id>', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('deposit/<str:id>', views.deposit, name="deposit"),
    path('mypage/', views.mypage, name="mypage"),
    path('payment/<str:id>', views.payment, name="payment"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('message/', views.message, name="message"),
    path('search/', views.search, name="search")
    #127.0.0.1:8000/user/ 이하의 url들은 user폴더의 urls파일에서 관리한다. 라는 설정
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
