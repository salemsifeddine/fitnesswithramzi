from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from django.http import JsonResponse
import json
import time
from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from django.utils.translation import gettext as _
from googletrans import Translator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import Exmple

# Create your views here.



#base.html
def base(request):
    
    data={
        'object':"salem object"
    }
    return render(request, "pages/base.html", data)

class Login(LoginView):
    template_name="pages/base.html"

def home(request):
    trans= _('hello')
    translator = Translator()
    translation =translator.translate("Hi every one I hope you are doing well", dest='ar')
    print(f'{translation.origin} is in {translation.src} ==> {translation.text}  [{translation.dest}]')


    if request.method == "POST":
        print("yess post")
   
    images_slide = SlideImages.objects.all()
    images=[]
    for image in images_slide:
        images.append(image.image.url)
        
    data={
        
        "images":images,
        "stylesheet":"static/css/home.css",
        "title":"Home",
        'trans':trans
        
    }
    return render(request, "pages/home.html",data)

def program(request):
    program=ProgramsWorkoutForPub.objects.all()
    data={
        "stylesheet":"static/css/program.css",
        "title":"Program",
        "program":program,
        "programstype":ProgramType.objects.all()
    }
    return render(request, "pages/program.html", data)


def programwktpublicDet(request,pk):   
    arrwkt=[]
    prgrms=[]
    i=1

    for ob in ProgramsWorkoutForPub.objects.filter(id=pk):
        objectwkt= ProgramsWorkoutForPubDet.objects.filter(program=ob.id)
        for obj in objectwkt:
            if objectwkt.filter(day=i):
                objectprogram={
                "day":i,
                "data":objectwkt.filter(day=i)
                    }
                arrwkt.append(objectprogram)
            i=i+1
        
    data={
        "object":arrwkt,
        "title":"Profile-Workout"
    }
    

    

        
    return render(request,"pages/publicWktProgDet.html",data)

def exercises(request):
    exercisesforpub=ExercisesForPublic.objects.all()
    muscles=ExercisesMuscles.objects.all()
    objarr=[]
    for muscle in muscles:
        obj={
            "muscle":muscle,
            "exercises":ExercisesForPublic.objects.filter(musclePart=muscle.id)
        }
        objarr.append(obj)
   
    data={
        "title":"Exercises",
        "exercises":objarr,
        
    }
    return render(request, "pages/exercises.html",data)

def exercisesPublicDet(request,pk):
    muscles=ExercisesMuscles.objects.all()
    arrwkt=[]
    prgrms=[]
    i=1

    for ob in ExercisesForPublic.objects.filter(id=pk):

        objectwkt= ExercisesForPublicDet.objects.filter(exBelongsTo=ob.id)
        print(objectwkt)
        for obj in objectwkt:
            #objectprogram={
            #"day":i,
            #"data":objectwkt.filter(day=i)
            #}
            arrwkt.append(obj)
            #i=i+1
    
  
    
    data={
        "title":"Exercises",
        "exercises":arrwkt,
        "muscles":muscles
    }
    return render(request, "pages/exercisesdetail.html",data)

def nutrition(request):
    nutritiontype=ProgramType.objects.all()
    nutritionp=ProgramsNutForPub.objects.all()
    

    data={
        "nutritiontype":nutritiontype,
        "nutritionp":nutritionp,
        "title":"Nutrition"
    }
    return render(request, "pages/nutrition.html",data)

def advices(request):
    advices=Advices.objects.all()
    data={
        "advices":advices,
        "title":"Advices"
    }
    return render(request, "pages/advices.html",data)


def about(request):

    about=About.objects.all()
    story=Story.objects.all()
    competitions=Comprtitions.objects.all()
    tableinfos=AtheteTable.objects.all()
    courtsey=Courtsey.objects.all()
    data={
        "title":"About",
        "about":about,
        "story":story,
        "competitions":competitions,
        "tableinfos":tableinfos,
        "courtsey":courtsey,
    }
    return render(request, "pages/about.html",data)

def gallery(request):
    data={
        "images":Gallery.objects.all(),
        "title":"Gallery",
    }
    return render(request, "pages/gallery.html",data)



def coaching(request):
    
    if request.method != 'POST':
        form=ContactInfo()
    else:
        form = ContactInfo(data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank')
            
    data={
        "form":form,
        "title":"Online Coaching"
    }
    
    return render(request, "pages/coaching.html",data)


def thank(request):
    return render(request,"pages/thank.html",{})


@login_required
def profil(request):
    
    if request.method == 'POST':
        form = ProfilInfoInputs(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("home")

        
    else:
        form= ProfilInfoInputs()
    
    Profilinfo =ProfilInfo.objects.all()
    
    profilobjectarr=[]
    i=0;
    for info in Profilinfo:
        if request.user == info.user:
            profilobject={
                "image":info.image,
                "weight":info.weight,
                "week":i
            }
            profilobjectarr.append(profilobject)
        i=i+1
    
   
    data={
        "form":form,
        "title":"Profil",
        "dataprofil":profilobjectarr
    }
    return render(request,"pages/profil.html",data)

@login_required
def Programwrktpers(request):
    programdata=[]
    for programday in ProgramPersonalWorkout.objects.all():
        if request.user.is_authenticated:
            if programday.clientProgram.ClientUser == request.user:
                if programday.image:
                    image =programday.image
                programobject = {
                    "day":programday.clientProgram.day,
                    "desc":programday.description,
                    "image":image,
                    "url":programday.urlYoutubeVedio
                }
                programdata.append(programobject)
    
        else:
            print("User Not Logged In")
    data={
        
        "title":"Program Personal",
        "programwrk":programdata,
    }

  
    return render(request, "pages/prgrmwrktpers.html",data)

@login_required
def persAdvice(request):

    
    advices=[]
    for advice in PersonalAdvice.objects.all():
        if advice.user == request.user:
            adviceobject={
                "title":advice.title,
                "content":advice.content,
                "image":advice.image,
                "url":advice.url,
                }
            advices.append(adviceobject)

    data={
        "advices":advices,
        "title":"Profile-Advices"
    }
    return render(request,"pages/personalAdvice.html",data)

@login_required
def persNutrition(request):

    nutritions=[]
  
    for nutrition in PersonalNutrition.objects.all():
        if nutrition.userProgram.user == request.user:

            nutritionobject={
                "repanum":nutrition.repaNumber,
                "content":nutrition.desc,
                "image":nutrition.image,
                }

            nutritions.append(nutritionobject)
    
    aimingfor=""
    for prog in UserPointProgramType.objects.all():
        if prog.user == request.user:
            aimingfor=prog.programType
    

    data={
        "aimingfor":aimingfor,
        "nutritions":nutritions,
        "title":"Profile-Nutrition"
    }
    return render(request,"pages/personalNutProg.html",data)

@login_required
def persWktProg(request):

    workouts=[]
  
    for workout in ProgramPersonalWorkout.objects.all():
        if workout.clientProgram.ClientUser == request.user:
            workoutobject={
                "day":workout.clientProgram.day,
                "content":workout.description,
                "image":workout.image,
                "wkt":workout
                }

            workouts.append(workoutobject)
    
    data={

        "program":DayUserWorkout.objects.filter(ClientUser=request.user).order_by("day"),
        "title":"Profile-Workout"
    }
    return render(request,"pages/personalWktProg.html",data)



@login_required
def persWorkoutDet(request,pk):
    arrwkt=[]
    prgrms=[]
    for ob in DayUserWorkout.objects.filter(ClientUser=request.user, day=pk):
        
        objectwkt= ProgramPersonalWorkout.objects.filter(clientProgram=ob)
        datawkt={
            "day":pk,
            "program":objectwkt
        }
        arrwkt.append(datawkt)


    data={
        "object":arrwkt,
        "title":"Profile-Workout"
    }

    return render(request,"pages/personalWktProgDet.html",data)


def api(request):
    data=Object()
    objct={}
    for entdata in ProgramType.objects.all():
        arr=[]
        filteredarray =ProgramsWorkoutForPub.objects.filter(programType=entdata)
        for dt in filteredarray:
            arr.append(dt)
            
        objct[f"entdata"] = arr
        
    dataobj={
        "obj":objct
    }
    return JsonResponse(dataobj,safe=False)

    ##مزالك public detail
    ##لكل واحد

def detailviewapi(request):
    task=ProgramsNutForPub.objects.all()
    serializer=Exmple(task,many=True)
    return Response(serializer)