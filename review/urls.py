from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reviews/new/', views.review_create, name='review_create'),
    path('reviews/',views.review_list, name='review_list'),
    path('', views.HomePage.as_view(), name='home'),
]
