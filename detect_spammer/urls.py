from django.urls import path
from . import views  

urlpatterns = [
    path('', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('mark_spam/<str:phone_number>/', views.mark_spam, name='mark_spam'),
    path('search/', views.search, name='search'),
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
]


