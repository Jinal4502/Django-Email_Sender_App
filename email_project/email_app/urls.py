from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('signup', views.signup, name="signup"),
    path('about', views.about, name="about")
]