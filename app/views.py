from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.http import *
# Create your views here.

class CategoryViews(APIView):

    def get(self,request,pk=None):

        if pk:
            catgory = Category.objects.filter(pk=pk)
            if catgory:
                serializer = CategorySerializer(catgory[0])
            else:
                return Response({"message":"Please enter valid id"},status=status.HTTP_404_NOT_FOUND)
        else:  
            categories = Category.objects.all()
            serializer = CategorySerializer(categories,many=True) 
            print("Serializer : ",serializers)
        return Response({'data':serializer.data,'success':True,'message':"Data is fetched"})

    def post(self,request):
        data = request.data
        print("Data : ",data)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def put(self,request,pk):
        try:
            category = Category.objects.get(pk=pk)
            data = request.data
            serializer = CategorySerializer(category,data=data,partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'data':data,'success':True,'message':"Data Updated"})

        except Category.DoesNotExist:
            return Http404

    def delete(self,request,pk):
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return Response({'message':"Data Deleted"})

        except Category.DoesNotExist:
            return Http404
