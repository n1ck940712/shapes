from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from .models import Shape
from .serializers import AppSerializer
from .permissions import IsOwnerOrReadOnly

import math

def get_area_perimeter(shape_type, shape_height, shape_width):
    if shape_type == 'rectangle':
        area = shape_width*shape_height
        perimeter = (shape_width*2)+(shape_height*2)
    elif shape_type == 'triangle':
        area = (shape_width*shape_height)/2
        perimeter = shape_width+math.sqrt((shape_height**2)+((shape_width/2)**2))*2
    elif shape_type == 'diamond':
        area = (shape_width*shape_height)/2
        perimeter = math.sqrt((shape_height/2)**2+(shape_width/2)**2)*4
    elif shape_type == 'square':
        area = (shape_width*shape_height)
        perimeter = (shape_width*2)+(shape_height*2)
    else:
        area = 0
        perimeter = 0
    return round(area, 4), round(perimeter,4)

class ListShapeDetailsAPIView(ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = AppSerializer
    def get_queryset(self):
        queryset = Shape.objects.filter(id=self.kwargs['pk'])
        return queryset
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if len(queryset):
            data = self.get_serializer(queryset, many=True).data[0]
            if not data['user'] == self.request.user.pk:
                return Response({'detail': 'You do not have permission to this shape object.'}, status=status.HTTP_403_FORBIDDEN , content_type = 'application/json' ) 
            else:
                data['area'], data['perimeter'] = get_area_perimeter(data['type'], data['height'], data['width'])
        else:
            data = {}
            data['detail'] = 'No shapes with id %s found.' % self.kwargs['pk']
        return Response(data, status=status.HTTP_200_OK, content_type = 'application/json' ) 


class ListShapeAPIView(ListAPIView):
    serializer_class = AppSerializer
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        permission_classes = (IsAuthenticated,)
        queryset = Shape.objects.filter(user=self.request.user.pk)
        return queryset


class CreateShapeAPIView(CreateAPIView):
    serializer_class = AppSerializer
    permission_classes = (IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    queryset = Shape.objects.all()


class UpdateShapeAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Shape.objects.all()
    serializer_class = AppSerializer


class DeleteShapeAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Shape.objects.all()
    serializer_class = AppSerializer