from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def calculator(request):
    num1 = int(request.data.get("num1"))
    num2 = int(request.data.get("num2"))
    choice = request.data.get("choice")
    result = 0


    try:
        if choice == 'sum':
            result = num1 + num2
            return Response({"Sum of the numbers is: ":result},status=200)

        elif choice == 'sub':
            result = num1 - num2
            return Response({"difference of the numbers is: ": result}, status=200)

        elif choice == 'mul':
            result = num1 * num2
            return Response({"Multiplication of the numbers is: ": result}, status=200)

        elif choice == 'div':
            if num2 == 0:
                return Response("Cannot Divide a number with Zero")
            else:
                result = num1 / num2
                return Response({"Division of the numbers is: ":result},status= 200)

        elif choice == 'pow':
            result = num1 ** num2
            return Response({" Number1 to the power of Number2 is:": result}, status=200)
        else:
            return Response("you have given an Invalid Operation")

    except(ZeroDivisionError,ValueError) as e:
        return Response("Please check your Operation")

def index_view(request):
    return render(request,'testapp/index.html')

