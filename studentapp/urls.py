from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.getStudents),
    path("add/", views.addStudent),
    path("<int:st_id>", views.getStudentBy_st_id),
]


""" 
{
"name":"Hassan Carpenter",
"st_id":12312312,
"level":100,
"program":"CS",
"type":"C"
}
 """
