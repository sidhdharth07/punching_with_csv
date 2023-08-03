from django.contrib import admin
from django.urls import path,include
from .views import Register_view,clockin_view,clockout_view,exportApI
urlpatterns = [
   path('in/<int:id>',clockin_view.as_view()),
   path('out/<int:id>',clockout_view.as_view()),
   path('register/',Register_view.as_view()),
   path('csv/',exportApI.as_view())
]