from django.db import models
import time
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.core.validators import RegexValidator

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
import random
from random import randint

from django.contrib.postgres.fields import ArrayField

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

owner = models.ForeignKey('auth.User', related_name='questions')
highlighted = models.TextField()

# from django.conf import settings
# from django.core.files.storage import FileSystemStorage
# fs = FileSystemStorage(location=settings.STATIC_ROOT)

class Saved_answers(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, blank=True,default='')
    level = models.CharField(max_length=100, blank=True,default='')
    seconds = models.CharField(max_length=100, blank=True,default='')
    answer1 = models.TextField(blank=True,default='',null=True)
    answer2 = models.TextField(blank=True,default='',null=True)
    answer3 = models.TextField(blank=True,default='',null=True)
    answer4 = models.TextField(blank=True,default='',null=True)
    answer5 = models.TextField(blank=True,default='',null=True)
    answer6 = models.TextField(blank=True,default='',null=True)
    answer7 = models.TextField(blank=True,default='',null=True)
    answer8 = models.TextField(blank=True,default='',null=True)
    answer9 = models.TextField(blank=True,default='',null=True)
    answer10 = models.TextField(blank=True,default='',null=True)
    answer11= models.TextField(blank=True,default='',null=True)
    answer12 = models.TextField(blank=True,default='',null=True)
    answer13 = models.TextField(blank=True,default='',null=True)
    answer14 = models.TextField(blank=True,default='',null=True)
    answer15 = models.TextField(blank=True,default='',null=True)
    answer16 = models.TextField(blank=True,default='',null=True)
    answer17 = models.TextField(blank=True,default='',null=True)
    answer18 = models.TextField(blank=True,default='',null=True)
    answer19 = models.TextField(blank=True,default='',null=True)
    answer20 = models.TextField(blank=True,default='',null=True)
    
   
    class Meta:
        ordering = ('created',)

