from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST,
                                   HTTP_404_NOT_FOUND)

from .models import StudentModel
from .serializers import StudentModelSerializer


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
    result = {}
    result_status = HTTP_400_BAD_REQUEST

    try:
        student = StudentModel.objects.get(st_id=st_id)
    except StudentModel.DoesNotExist:
        result['success'] = False
        result['message'] = "Student ID is unknown"
        return Response(
            data=result, status=result_status
        )

    if request.method == "GET":
        serialized_student = StudentModelSerializer(student)
        result['success'] = True
        result['body'] = serialized_student.data
        result_status = HTTP_200_OK

        return Response(data=result, status=result_status)


@api_view(['POST'])
def addStudent(request):
    if request.method == "POST":
        student_serializer = StudentModelSerializer(data=request.data)

        result = {}
        result_status = HTTP_400_BAD_REQUEST

        if student_serializer.is_valid():
            student_serializer.save()

            result['success'] = True
            result['message'] = f"{student_serializer.data['name']} added successfully"
            result_status = HTTP_201_CREATED

        else:
            result['success'] = False
            result['message'] = student_serializer.errors["st_id"][0]

        return Response(data=result, status=result_status)


@api_view(["DELETE"])
def deleteStudent(request, st_id):

    if request.method == "DELETE":
        result = {}
        result_status = HTTP_400_BAD_REQUEST

        try:
            student = StudentModel.objects.get(st_id=st_id)

            if student.delete():
                result['success'] = True
                result['message'] = "student deleted successfully"
                result_status = HTTP_200_OK
            else:
                result['success'] = False
                result['message'] = "Student was not deleted"
                result_status = HTTP_400_BAD_REQUEST

        except StudentModel.DoesNotExist:
            result['success'] = False
            result['message'] = "Student ID is unknown"
            result_status = HTTP_404_NOT_FOUND

        return Response(data=result, status=result_status)


@api_view(['PUT'])
def updateStudent(request, st_id):
    if request.method == "PUT":
        result = {}
        result_status = HTTP_400_BAD_REQUEST

        try:
            student = StudentModel.objects.get(st_id=st_id)

            if student:
                studentSerializer = StudentModelSerializer(
                    student, request.data)

                if studentSerializer.is_valid():
                    student.save()
                    result['success'] = True
                    result['message'] = "student updated successfully"
                    result_status = HTTP_200_OK

                else:
                    result['success'] = False
                    result['message'] = StudentModelSerializer.errors
                    result_status = HTTP_400_BAD_REQUEST

            else:
                result['success'] = False
                result['message'] = "empty result set"
                result_status = HTTP_400_BAD_REQUEST

        except StudentModel.DoesNotExist:
            result['success'] = False
            result['message'] = "Student ID is unknown"
            result_status = HTTP_404_NOT_FOUND

        return Response(data=result, status=result_status)
