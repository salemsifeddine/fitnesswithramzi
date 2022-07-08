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
        "class":"form-control",
        "type":"text",
        "placeholder":"Full name",
        "id":"name",
        "data-validation-required-message":"Please enter your name"
    }))
    email=forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "type":"email",
        "placeholder":"email",
        "id":"email",
        "data-validation-required-message":"Please enter your email"
    }))
    birthday=forms.CharField(widget=forms.TextInput(attrs={
       "class":"form-control",
        "type":"date",
        "placeholder":"birthday date",
        "id":"birthday",
        "data-validation-required-message":"Please enter your birthday date"

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
        "class":"form-control",
        "type":"text",
        "placeholder":"address",
        "id":"address",
        "data-validation-required-message":"Please enter your address"
    }))
    city=forms.CharField(widget=forms.TextInput(attrs={
         "class":"form-control",
        "type":"text",
        "placeholder":"city",
        "id":"city",
        "data-validation-required-message":"Please enter your city"
    }))
    phone_number=forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "type":"number",
        "placeholder":"phone N°",
        "id":"phone",
        "data-validation-required-message":"Please enter your phone N°"
    }))
    subject=forms.CharField(widget=forms.Textarea( attrs={
        "class":"form-control",
        
        "placeholder":"subject",
        "id":"subject",
        "data-validation-required-message":"Please enter your subject"
    }))
    pull=forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "type":"number",
        "placeholder":"pull maximum weight",
        "id":"pull",
        "data-validation-required-message":"Please enter your max weight in pull"
    }))
    push=forms.CharField(widget=forms.TextInput(attrs={
         "class":"form-control",
        "type":"number",
        "placeholder":"push maximum weight",
        "id":"push",
        "data-validation-required-message":"Please enter your max weight in push"
    }))
    squat=forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "type":"number",
        "placeholder":"squat maximum weight",
        "id":"squat",
        "data-validation-required-message":"Please enter your max weight in squat"
    }))
    dlift=forms.CharField(widget=forms.TextInput(attrs={
       "class":"form-control",
        "type":"number",
        "placeholder":"dead lift maximum weight",
        "id":"pull",
        "data-validation-required-message":"Please enter your max weight in dead lift"
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