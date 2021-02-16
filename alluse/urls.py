from django.urls import path
from .import views
app_name ='alluse'
urlpatterns = [
    path('change-password',views.changePassword , name = "changePassword"),
]
