from django.urls import path 
from . import views

app_name = 'polls'

urlpatterns = [
        # path('', views.index, name='index'),
        path('', views.Index.as_view(), name='index'),
        # path('<int:question_id>/', views.detail, name='detail'),
        path('<int:pk>/', views.Detail.as_view(), name='detail'),
        # # path('<int:question_id>/results/', views.results, name='results'),
        path('<int:pk>/results/', views.Results.as_view(), name='results'),
        path('<int:question_id>/vote/', views.vote, name='vote'),
        path('createquestion/', views.CreateQuestion.as_view(), name='create_question'),
        path('deletequestion/<int:pk>/', views.DeleteQuestion.as_view(), name='delete_question'),
        #path('<int:pk>/createchoice/', views.Vote.as_view(), name='vote'),
        #path('<int:pk>/updatechoice/'),
        #path('<int:pk>/deletechoice/'),
]