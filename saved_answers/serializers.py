from rest_framework import serializers
from saved_answers.models import Saved_answers, LANGUAGE_CHOICES, STYLE_CHOICES
import random
from random import randint
import json
import time


class Saved_answersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Saved_answers
        fields = ('seconds','pk','username','level','answer1','answer2','answer3','answer4','answer5','answer6','answer7','answer8','answer9','answer10','answer11','answer12','answer13','answer14','answer15','answer16','answer17','answer18','answer19','answer20')
        #write_only_fields = ('firstame', 'lastname')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        
        if(Saved_answers.objects.filter(username=validated_data.get('username'),level=validated_data.get('level')).exists()):
         objects=Saved_answers.objects.filter(username=validated_data.get('username'),level=validated_data.get('level')).update(seconds=validated_data.get('seconds'),answer1=validated_data.get('answer1'),answer2=validated_data.get('answer2'),answer3=validated_data.get('answer3'),answer4=validated_data.get('answer4'),answer5=validated_data.get('answer5'),answer6=validated_data.get('answer6'),answer7=validated_data.get('answer7'),answer8=validated_data.get('answer8'),answer9=validated_data.get('answer9'),answer10=validated_data.get('answer10'),answer11=validated_data.get('answer11'),answer12=validated_data.get('answer12'),answer13=validated_data.get('answer13'),answer14=validated_data.get('answer14'),answer15=validated_data.get('answer15'),answer16=validated_data.get('answer16'),answer17=validated_data.get('answer17'),answer18=validated_data.get('answer18'),answer19=validated_data.get('answer19'),answer20=validated_data.get('answer20'))
        else:
         objects=Saved_answers.objects.create(seconds=validated_data.get('seconds'),username=validated_data.get('username'),level=validated_data.get('level'),answer1=validated_data.get('answer1'),answer2=validated_data.get('answer2'),answer3=validated_data.get('answer3'),answer4=validated_data.get('answer4'),answer5=validated_data.get('answer5'),answer6=validated_data.get('answer6'),answer7=validated_data.get('answer7'),answer8=validated_data.get('answer8'),answer9=validated_data.get('answer9'),answer10=validated_data.get('answer10'),answer11=validated_data.get('answer11'),answer12=validated_data.get('answer12'),answer13=validated_data.get('answer13'),answer14=validated_data.get('answer14'),answer15=validated_data.get('answer15'),answer16=validated_data.get('answer16'),answer17=validated_data.get('answer17'),answer18=validated_data.get('answer18'),answer19=validated_data.get('answer19'),answer20=validated_data.get('answer20'))
        # print >> sys.stderr, objects
        return objects


    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """

        instance.username = validated_data.get('username', instance.username)
        instance.level = validated_data.get('level', instance.level)
        instance.answer1 = validated_data.get('answer1', instance.answer1)
        instance.answer2 = validated_data.get('answer2', instance.answer2)
        instance.answer3 = validated_data.get('answer3', instance.answer3)
        instance.answer4 = validated_data.get('answer4', instance.answer4)
        instance.answer5 = validated_data.get('answer5', instance.answer5)
        instance.answer6 = validated_data.get('answer6', instance.answer6)
        instance.answer7 = validated_data.get('answer7', instance.answer7)
        instance.answer8 = validated_data.get('answer8', instance.answer8)
        instance.answer9 = validated_data.get('answer9', instance.answer9)
        instance.answer10 = validated_data.get('answer10', instance.answer10)
        instance.answer11 = validated_data.get('answer11', instance.answer11)
        instance.answer12 = validated_data.get('answer12', instance.answer12)
        instance.answer13 = validated_data.get('answer13', instance.answer13)
        instance.answer14 = validated_data.get('answer14', instance.answer14)
        instance.answer15 = validated_data.get('answer15', instance.answer15)
        instance.answer16 = validated_data.get('answer16', instance.answer16)
        instance.answer17 = validated_data.get('answer17', instance.answer17)
        instance.answer18 = validated_data.get('answer18', instance.answer18)
        instance.answer19 = validated_data.get('answer19', instance.answer19)
        instance.answer20 = validated_data.get('answer20', instance.answer20)
        
        return instance


