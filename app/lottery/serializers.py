from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Lottery
from django import forms


class LotterySerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Lottery
        fields = [
            'phone_number',
            'lottery_number',
            'name',
            'plate_number',
            'date'
        ]