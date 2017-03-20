from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.generate_question_paper, name='generate_question_paper'),
    url(r'^$', views.regenerate, name='regenerate_paper'),
    url(r'^$', views.print_paper, name='print_paper'),
    url(r'^$', views.approve_paper, name='approve_paper'),
    url(r'^$', views.reject_paper, name='reject_paper'),
    url(r'^$', views.save_paper, name='save'),

]
