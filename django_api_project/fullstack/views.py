from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Employee


# Create your views here.

#@api_view(['POST'])
def index_view(request):
    return render(request,'fullstack/index.html')

@api_view(['POST'])
def create_user(request):
    try:

        name = request.data.get("name")
        roll_no = request.data.get("roll_no")
        email = request.data.get("email")

        employee = Employee(name=name,roll_no=roll_no,email=email)
        employee.save()

        if employee is not None:
            return Response({
                'message' : 'User Created'
            },status=200)

        else:
            return Response({
                'message':'User Not Created'
            },status=200)

    except Exception as e:
        return Response({
            'message':'User Not Created'
        },status=200)

@api_view(['GET'])
def get_details(request):

        roll_no = request.data.get("roll_no")
        roll_nos = Employee.objects.values_list('roll_no',flat=True)
        li_roll_nos = list(roll_nos)

        if roll_no in li_roll_nos:
            employee = Employee.objects.get(roll_no=roll_no)

            return Response({
                'name' : employee.name,
                'roll_no' : employee.roll_no,
                'email' : employee.email
            },status=200)

        else:
            return Response({
                'error':'User Not Found'
            },status=200)

