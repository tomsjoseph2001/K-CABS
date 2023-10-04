from django.urls import path
from .import views


urlpatterns = [
    path('', views.showhello),
    path('signup/', views.signup,name='signup'),
    path('signin/', views.signin,name='signin'),
    path('logout/', views.user_logout,name='logout'),
    path('home/', views.home,name='home')

]