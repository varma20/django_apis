from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

@api_view(['POST'])
def user_sign_in(request):
    name = request.data.get("request")
    password = request.data.get("password")

    if name == "Guna" and password == 1234:
        return Response({
           'message' : 'User have Signed In Successfully'
        },status=200)

    else:
        return Response({'message':'User Not Signed In'},status=200)