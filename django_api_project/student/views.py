
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *

@api_view(['POST'])
def create_user(request):
    try:
        rno = request.data.get('rno')
        name = request.data.get('name')
        branch = request.data.get('branch')
        play_cricket = request.data.get('play_cricket')
        student = Student(rno=rno,name=name,branch=branch,play_cricket=play_cricket)
        student.save()
        return Response({"User Created"},status = 200)
    except Exception as e:
        return Response("{User Not Created}",status=200)


@api_view(['POST'])
def delete_user(request):
    try:
        rno = request.data.get('rno')
        student = Student.objects.get(rno=rno)
        student.delete()
        return Response({'User Deleted'},status=200)
    except Exception as e:
        return Response({"User Not Deleted"},status=200)

@api_view(['POST'])
def user_details(request):
    try:
        rno = request.data.get('rno')
        student = Student.objects.get(rno=rno)
        return Response({
            'Name':student.name,
            'Roll Number' : student.rno,
            'Branch' : student.branch,
            'Play Cricket': student.play_cricket
        },status=200)
    except Exception as e:
        return Response({"User Details not Found"},status=200)


@api_view(['GET'])
def user_details_from_get_request(request):

    try:
        roll_no = request.data.get('roll_no')
        roll_nos_from_query_set = Student.objects.values_list('roll_no',flat=True)
        li_rol_nos = list(roll_nos_from_query_set)
        if roll_no in li_rol_nos:
            student = Student.objects.get(roll_no = roll_no)
            #if student is None:
                #return Response({"User Not Found"},status=200)
            #else:
            return Response({
                "First Name": student.first_name,
                "Last Name": student.last_name,
                "Roll Number": student.roll_no,
                "Branch": student.branch,
                "Backlogs": student.backlogs,
                "Percentage": student.percentage,
                "Date Of Birth": student.dob,
                "Email Id": student.email,
                "Blood Group": student.blood_group
            }, status=200)
        else:
            return Response({"User Not Found"},status = 200)

    except Exception as e:
        return Response({"User not found"},status=200)



@api_view(['DELETE'])
def delete_user_from_delete_request(request):

    try:
        roll_no = request.data.get('roll_no')
        roll_nos_from_query_set = Student.objects.values_list('roll_no', flat=True)
        li_roll_nos = list(roll_nos_from_query_set)
        if roll_no in li_roll_nos:
            student = Student.objects.get(roll_no = roll_no)
            student.delete()
            return Response("User Deleted Successfully")
        else:
            return Response({"User Not Found"},status=200)

    except Exception as e:
        response = {"User":"User Not Found"}
        return Response(response,status=200)





