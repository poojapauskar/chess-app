from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from saved_answers import views

urlpatterns = [
    url(r'^saved_answers/$', views.Saved_answersList.as_view()),
    url(r'^saved_answers/(?P<pk>[0-9]+)/$', views.Saved_answersDetail.as_view()),


    url(r'^update_details/$', views.Update_details.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)