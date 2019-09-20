from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from apis.accounts.serializers import UserCreateSerializer
from rest_framework import generics
from apis.news.serializers import NewsSerializer
from apis.news.models import News
from apis.accounts.models import User


# Create your views here.


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]


class ReporterNewsAPIView(generics.ListAPIView):
    serializer_class = NewsSerializer
    permission_classes = [permissions.AllowAny]
    # def get_queryset(self):
    #     reporter = self.kwargs['reporter']
    #     return News.objects.filter(news__reporter=reporter)
    def get_queryset(self):
        reporter = self.kwargs.get('reporter')
        return News.objects.filter(reporter=reporter)
    
