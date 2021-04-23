
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('results/<int:pk>', views.ResultsView.as_view(), name='results'),
    path('vote/<int:question_id>/', views.vote, name='vote'),
]




#urlpatterns = [
#    path('hello/', views.index, name='index'),
#    path('<int:question_id>/', views.detail, name='detail'),
#    # ex: /polls/5/results/
#    path('results/<int:question_id>/', views.results, name='results'),
#    # ex: /polls/5/vote/
#    path('vote/<int:question_id>/', views.vote, name='vote'),
#]
