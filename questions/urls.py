from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.QuestionsView.as_view()),
    url(r'^(?P<pk>\d+)/$', views.QuestionsView.as_view())
]