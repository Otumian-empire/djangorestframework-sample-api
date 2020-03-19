from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.getStudents),
    path("add/", views.addStudent),
    path("<int:st_id>/", views.getStudentBy_st_id),
    path("<int:st_id>/", views.deleteStudent),
]
