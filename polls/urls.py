from polls.views import IndexView, DetailView, vote,ResultsView
from django.urls import path
# from . import views
app_name = "polls"


# urlpatterns = [
#     path('', index, name = "index"),
#     path("<int:question_id>/", detail, name="detail"),
#     path("<int:question_id>/results/", result, name="results"),
#     path("<int:question_id>/vote/", vote, name="vote"),
 
# ] 


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<int:pk>/", DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", vote, name="vote"),
]