from django.shortcuts import render
from .serializers import registe_serializers,timing_serializers
from .models import timing_model,RegisterModel
from rest_framework.response import Response
import csv
from rest_framework import status
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
# Create your views here.

class Register_view(APIView):
      def post(self,request):
        serializer=registe_serializers(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

class clockin_view(APIView):
    def post(self,request,id):
        try:
            time_record=RegisterModel.objects.get(id=id)
        except RegisterModel.DoesNotExist:
            return Response({"error":"time record does not exist"},status=status.HTTP_400_BAD_REQUEST)
        request.data['emp_id'] = time_record
        serializer=timing_serializers(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            new_record= timing_model.objects.get(id=serializer.data.get('id'))
            new_record.emp = time_record
            new_record.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            # new_record['emp_id'] = time_record
            # user =RegisterModel.objects.get(id=emp_id)
            # serializer.data['emp_id'] = user
            # time_record.save()    
    
class clockout_view(APIView):
    def put(self,request,id):
        try:
            time_record=timing_model.objects.get(id=id)
        except timing_model.DoesNotExist:
            return Response({"error":"time record does not exist"},status=status.HTTP_400_BAD_REQUEST)
        if time_record:
            clock_out = request.data.get('clock_out')
            d1 = datetime.strptime(clock_out, "%Y-%m-%d %H:%M:%S%z")
            time = d1 - time_record.clock_in
            # time1 = str(time)
            # -================================================================
            time_record.durations = str(time)
            print (time_record.durations)
            time_record.clock_out = str(clock_out)
            time_record.save()
            return Response(f"{time, time_record}")
        return Response("serializer.errors",status=status.HTTP_400_BAD_REQUEST)
    
    
class exportApI(APIView):

    def get(request,*args):
        queryset = timing_model.objects.all()
        serializer = timing_serializers(queryset, many=True)
        response = HttpResponse(content_type='text/csv')  
        response['Content-Disposition'] = 'attachment; filename="file.csv"'  
        writer = csv.writer(response)  
        writer.writerow(['emp','clock_in','clock_out','durations'])  
        for i in serializer.data:
            print(i['emp']["id"])
            writer.writerow([i['emp']["id"],i['clock_in'],i['clock_out'],i['duration']])  
        return response
    