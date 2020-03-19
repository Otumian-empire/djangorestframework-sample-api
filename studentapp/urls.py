from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.getStudents),
    path("<int:st_id>/", views.getStudentBy_st_id),
    path("add/", views.addStudent),
    path("<int:st_id>/delete/", views.deleteStudent),
    path("<int:st_id>/update/", views.updateStudent),
]
