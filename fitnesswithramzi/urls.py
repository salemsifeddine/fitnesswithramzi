from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from . import views
#from .views import PersWorkoutDet
from django.conf import settings
from .models import *
from django.conf.urls.static import static
from django.contrib.auth import views as view

urlpatterns = [
   
    path('',views.home, name="home"),
    path('program/',views.program, name="program"),
    path('program/Workout/<int:pk>/',views.programwktpublicDet,name="programwktpublicDet"),
    path('program/exercises/',views.exercises, name="exercises"),
    path('program/exercises/<int:pk>/',views.exercisesPublicDet,name="programexpublicDet"),
    path('program/nutrition/',views.nutrition, name="nutrition"),
    path('about/',views.about, name="about"),
    path('gallery/',views.gallery, name="gallery"),
    path('advices/',views.advices, name="advices"),
    path('coaching/',views.coaching, name="coaching"),
    path('login/',view.LoginView.as_view(template_name="pages/login.html"), name="login"),
    path('logout/',view.LogoutView.as_view(template_name="pages/home.html"), name="logout"),
    path('coaching/thanks/',views.thank, name="thank"),
    path('profil/',views.profil,name="profil"),
    path('profil/program/workout/',views.Programwrktpers,name="profilworkout")  ,
    path('profil/Advices/',views.persAdvice,name="persAdvice"),
    path('profil/program/nutrition/',views.persNutrition,name="persNutrition"), 
    path('profil/Workout/',views.persWktProg,name="persWorkout"),
    path('profil/program/Workout/Day/<int:pk>/',views.persWorkoutDet,name="persWorkoutDet"),
  
    path('api/',views.api,name="api"),
    path('api2/',views.detailviewapi,name="api2"),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

