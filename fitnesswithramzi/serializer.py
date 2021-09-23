from rest_framework import serializers
from .models import *

class Exmple(serializers.ModelSerializer):
    class Meta:
        model=ProgramsNutForPub
        fields='__all__'