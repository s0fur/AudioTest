from django.shortcuts import render, HttpResponse
from rest_framework import generics
from .serializers import NoiseSerializer, ShorthandSerializer, AnswerNoiseSerializer, AnswerShorthandSerializer
from .models import Noise, AnswersNoise, Shorthand, AnswersShorthand
from rest_framework.views import APIView
import numpy as np
from rest_framework.response import Response

# Create your views here.
def test(request):
    return HttpResponse("Hello")

class NoiseGet(APIView):
    def get(self, request):
        queryset = Noise.objects.all()
        var = list(np.random.randint(queryset.first().pk,queryset.first().pk+len(list(queryset)),len(list(queryset))))
        queryset = queryset.filter(pk__in=var)
        return Response({'Audio': NoiseSerializer(queryset, many=True).data})
    
class AnswerNoisePost(generics.CreateAPIView):
    queryset = AnswersNoise
    serializer_class = AnswerNoiseSerializer
    
class ShorthandGet(generics.ListAPIView):
    def get(self, request):
        queryset = Shorthand.objects.all()
        var = list(np.random.randint(queryset.first().pk,queryset.first().pk+len(list(queryset)),len(list(queryset))))
        queryset = queryset.filter(pk__in=var)
        return Response({'Audio': ShorthandSerializer(queryset, many=True).data})
    
class AnswerShorthandPost(generics.CreateAPIView):
    queryset = AnswersShorthand
    serializer_class = AnswerShorthandSerializer