from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework import views
from .models import Item
from .serializer import ItemSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import DjangoModelPermissions
from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.owner == request.user



class modelViewSet(viewsets.ModelViewSet):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer
    permission_classes = [IsOwnerOrAdmin]

from .serializer import UserSerializer
from .models import CustomUser
class RegisterUser(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer
 

from rest_framework.decorators import api_view
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status



