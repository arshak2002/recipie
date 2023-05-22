from django.urls import path
from .views import *

urlpatterns = [
    path('listcreate',ListCreate.as_view()),
    path('getitem/<int:id>/',GetItem.as_view()),
    path('search',Search.as_view()),
    path('favorite',MyFavorite.as_view()),
    path('comment/<int:id>/',RatingAndComment.as_view()),
]