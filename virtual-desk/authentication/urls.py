from django.urls import path
from . import views

urlpatterns = [
    path('signIn/', views.signIn, name="login"),
    path('postsign/', views.postsign),
    path('logout/', views.logout, name="log"),
    path('signup/', views.signUp, name="signup"),
    path('postsignup/', views.postsignup, name="postsignup"),

]
