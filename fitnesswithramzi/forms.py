from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *

class UserInfo(UserCreationForm):
   
    email=forms.CharField(widget=forms.TextInput(attrs={
        "class":"inpt",
        "type":"email"
    }))
    
    
    class Meta:
        model=User
        fields=["username","email"]



class ContactInfo(forms.ModelForm):
    fullname=forms.CharField(widget=forms.TextInput(attrs={
        "class":"inpt",
        "type":"text"
    }))
    email=forms.CharField(widget=forms.TextInput(attrs={
        "class":"inpt",
        "type":"email"
    }))
    birthday=forms.CharField(widget=forms.TextInput(attrs={
        "class":"inpt",
        "type":"date"
    }))
    sexe_male=forms.CharField(required=False,widget=forms.TextInput(attrs={
        "id":"check0",
        "type":"checkbox"
    }))
    sexe_female=forms.CharField(required=False,widget=forms.TextInput(attrs={
        "id":"check1",
        "type":"checkbox"
    }))
    address=forms.CharField(widget=forms.TextInput(attrs={
        "class":"inpt",
        "type":"text"
    }))
    city=forms.CharField(widget=forms.TextInput(attrs={
        "class":"inpt",
        "type":"text"
    }))
    phone_number=forms.CharField(widget=forms.TextInput(attrs={
        "class":"inpt",
        "type":"number"
    }))
    subject=forms.Textarea()
    pull=forms.CharField(widget=forms.TextInput(attrs={
        "class":"inpt",
        "type":"number"
    }))
    push=forms.CharField(widget=forms.TextInput(attrs={
        "class":"inpt",
        "type":"number"
    }))
    squat=forms.CharField(widget=forms.TextInput(attrs={
        "class":"inpt",
        "type":"number"
    }))
    dlift=forms.CharField(widget=forms.TextInput(attrs={
        "class":"inpt",
        "type":"number"
    }))

    class Meta:
        model=Contact
        fields=["fullname","email","birthday","sexe_male","sexe_female","address","city","phone_number","subject","push","pull","squat","dlift"]

class ProfilInfoInputs(forms.ModelForm):
    image=forms.ImageField()
    
    weight=forms.CharField(widget=forms.TextInput(attrs={
   
        "type":"number"
    }))

    addAnyThing=forms.Textarea()

    class Meta:
        model=ProfilInfo
        fields=["image","weight","addAnyThing"]