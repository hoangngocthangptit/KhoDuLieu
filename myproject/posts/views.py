from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import ListView
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.views import APIView

from .models import Post, DepositorMst, OfficeMst, PaymentConditionRegistration
from .serlializers import DepositorMstSerializer, OfficeMstSerializer, PaymentConditionRegistrationSerializer
from rest_framework.response import Response

# class ListPostView(ListView):
#   model = Post
#   def get (self, request, *args, **kwargs):
#     template_name = 'posts/list-posts.html' # sẽ được tạo ở phần dưới
#     obj = {
#       'posts': Post.objects.all()
#     }
#     return render(request, template_name, obj)
class DepositorMstAPI(APIView):
    def get(self, request):
        mymodels = DepositorMst.objects.all()
        serializer = DepositorMstSerializer(mymodels, many=True)
        return Response(serializer.data)
class OfficeMstAPI(APIView):
    def get(self, request):
        mymodels = OfficeMst.objects.all()
        serializer = OfficeMstSerializer(mymodels, many=True)
        return Response(serializer.data)
class PaymentConditionRegistrationAPI(APIView):
    def post(self, request):
        serializer_class = PaymentConditionRegistrationSerializer
        queryset = PaymentConditionRegistration.objects.all()
        serializer = self.serializer_class(data=request.data)
        serializer.save()
        return Response({"status": "success", "note": serializer.data},status=None)
