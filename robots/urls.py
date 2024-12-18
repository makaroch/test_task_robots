from django.urls import path

from robots import views

app_name = 'robots'

urlpatterns = [
    path("add-robot/", views.add_robot, name="add_robot"),
]
