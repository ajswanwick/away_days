from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reviews/<int:pk>/edit/', views.review_update, name='review_update'),
    path('reviews/<int:pk>/delete/', views.review_delete, name='review_delete'),
    path('reviews/new/', views.review_create, name='review_create'),
    path('reviews/', views.review_list, name='review_list'),
    path('', views.HomePage.as_view(), name='home'),
]
