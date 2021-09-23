from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.

#images for the slider


class ProgramType(models.Model):
    name=models.CharField(max_length=70)
    def __str__(self):
        return f'{self.name}'


class SlideImages(models.Model):
    image = models.ImageField(upload_to="slide_images", null=True)
    date= models.DateTimeField(auto_now_add=True)

class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery_images", null=True)
    place=models.CharField(max_length=30)
    token= models.CharField(max_length=4)

  
class Contact(models.Model):
    fullname=models.CharField(max_length=20)
    email=models.EmailField()
    birthday=models.DateField()
    sexe_male=models.CharField(max_length=5)
    sexe_female=models.CharField(max_length=5)
    address=models.CharField(max_length=25)
    city=models.CharField(max_length=25)
    phone_number=models.IntegerField()
    subject=models.TextField()
    pull=models.IntegerField()
    push=models.IntegerField()
    squat=models.IntegerField()
    dlift=models.IntegerField()

class ProfilInfo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(blank=False,upload_to= "clients_images")
    weight=models.IntegerField()
    addAnyThing=models.TextField(blank=True)

class ExercisesMuscles(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"

class ExcercisesMusclesPart(models.Model):
    muscle=models.ForeignKey(ExercisesMuscles, on_delete=models.CASCADE)
    part=models.CharField(max_length=50)
    def __str__(self):
        return f'{self.part} of {self.muscle}'

class ExercisesForPublic(models.Model):
    musclePart=models.ForeignKey(ExcercisesMusclesPart, on_delete=models.CASCADE)
    exerciseName=models.CharField(max_length=80)
    image=models.ImageField(upload_to="exercisespublic",blank=True)
    url=models.TextField(blank=True)

    def __str__(self):
        return f'{self.exerciseName}'

class ExercisesForPublicDet(models.Model):
    exBelongsTo=models.ForeignKey(ExercisesForPublic, on_delete=models.CASCADE)
    day=models.IntegerField(default=1)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to="exercisespublicDet",blank=True)
    url=models.TextField(blank=True)

    def __str__(self):
        return f'{self.exBelongsTo}'


class DayUserWorkout(models.Model):
    day=models.IntegerField(default=1)
    ClientUser=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    image=models.ImageField(upload_to="imagesofdayuserwrkt",blank=True)
    def __str__(self):
        return f'{self.ClientUser} Day {self.day}'

class ProgramsWorkoutForPub(models.Model):
    programType=models.ForeignKey(ProgramType, on_delete=models.CASCADE)
    programName=models.CharField(max_length=80)
    image=models.ImageField(upload_to="programswktpublic",blank=True)
    desc=models.CharField(max_length=1000)
    def __str__(self):
        return f'{self.programName}'

class ProgramsWorkoutForPubDet(models.Model):
    program=models.ForeignKey(ProgramsWorkoutForPub, on_delete=models.CASCADE)
    day=models.IntegerField(default=1)
    exerciseName=models.CharField(max_length=80)
    desc=models.TextField()
    image=models.ImageField(blank=True,upload_to="programWkt_public_images")

    def __str__(self):
        return f"Program Workout"



class ProgramPersonalWorkout(models.Model):
    clientProgram=models.ForeignKey(DayUserWorkout,on_delete=models.CASCADE)
    exerciseName=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(blank=True,upload_to="programWkt_client_images")
    urlYoutubeVedio=models.TextField(blank=True)

    def __str__(self):
        return f"{self.clientProgram.ClientUser} Program Workout"

class Program_Nutrition(models.Model):
    Client=models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.TextField()
    listNutrition=models.CharField(blank=True,max_length=100)
    image=models.ImageField(blank=True,upload_to="programNut_client_images")

    def __str__(self):
        return f"{self.Client} Program Nutrition"
        




class ProgramsNutForPub(models.Model):
    programType=models.ForeignKey(ProgramType, on_delete=models.CASCADE)
    programName=models.CharField(max_length=80)
    image=models.ImageField(upload_to="programswktpublic",blank=True)
    desc=models.TextField(blank=True)

    def __str__(self):
        return f'{self.programName}'

class About(models.Model):
    mainImage=models.ImageField(upload_to="aboutPics",blank=False)
    imagedate=models.IntegerField()
    informationsAboutYou=models.TextField(blank=False)

class Story(models.Model):
    mainImage=models.ImageField(upload_to="aboutPics",blank=False)
    imagedate=models.IntegerField()
    description=models.TextField(blank=False)


class Comprtitions(models.Model):
    competitionName=models.CharField(blank=False,max_length=50)
    competitions=models.ImageField(upload_to="aboutPics/competitions",blank=True)
    imagedate=models.IntegerField()
    competitionsText=models.TextField(blank=False)

class AtheteTable(models.Model):
    key=models.CharField(blank=False,max_length=50)
    value=models.CharField(blank=False, max_length=30)

class Courtsey(models.Model):
    description=models.TextField(blank=True)
    SocielMediaPost=models.CharField(max_length=1000, blank=True)
    image=models.ImageField(upload_to="courtsey_images",blank=True)

class Advices(models.Model):
    advicesFor=models.CharField(max_length=100)
    adviceContent=models.TextField()
    adviceImage=models.ImageField(upload_to="advicesimages",blank=True)
    url=models.CharField(blank=True, max_length=1000)

class PersonalAdvice(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.TextField()
    image=models.ImageField(upload_to="PersonalAdvicesImages",blank=True)
    url=models.CharField(max_length=1000,blank=True)


class UserPointProgramType(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    programType=models.ForeignKey(ProgramType, on_delete=models.CASCADE)
    def __str__(self):
            return f'{self.user}'

class PersonalNutrition(models.Model):
    userProgram=models.ForeignKey(UserPointProgramType, on_delete=models.CASCADE)
    repaNumber=models.IntegerField()
    url=models.TextField(blank=True)
    image=models.ImageField(upload_to="programsNutPers",blank=True)
   

    def __str__(self):
        return f'{self.userProgram.user} repa  {self.repaNumber}'


