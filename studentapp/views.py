from django.shortcuts import render
from .models import StudentModel
from .serializers import StudentModelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_201_CREATED


# Create your views here.
@api_view(['GET'])
def getStudents(request):
    try:
        students = StudentModel.objects.all()
    except StudentModel.EmptyResultSet:
        return Response(status=HTTP_204_NO_CONTENT)

    if request.method == "GET":
        serialized_students = StudentModelSerializer(students, many=True)

        return Response(serialized_students.data)


@api_view(['GET'])
def getStudentBy_st_id(request, st_id):
    try:
        students = StudentModel.objects.filter(st_id=st_id)
    except StudentModel.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serialized_students = StudentModelSerializer(students, many=True)
        result = {}
        result['success'] = True
        result['body'] = serialized_students.data

        return Response(data=result)


@api_view(['POST'])
def addStudent(request):
    if request.method == "POST":
        student_serializer = StudentModelSerializer(data=request.data)

        if student_serializer.is_valid():
            student_serializer.save()
            result = {}
            result['success'] = True
            result['message'] = f"{student_serializer.data['name']} add successfully"
            return Response(data=result, status=HTTP_201_CREATED)
        return Response(student_serializer.errors, status=HTTP_400_BAD_REQUEST)

    # delete
