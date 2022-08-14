from django.urls import path
from . import views 
from django.conf.urls.static import static

urlpatterns = [
   path('register/', views.register, name='register'),  
   path('login/', views.login, name="login")
   #즉, 최종적인 url은 127~~~~:8000/user/register가 된다.
] 