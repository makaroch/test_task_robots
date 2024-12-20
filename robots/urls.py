from django.urls import path

from robots import views

app_name = 'robots'

urlpatterns = [
    path("add-robot/", views.post, name="add_robot"),
    path("download-report/", views.download_robot_report, name="download_report"),
]
