from django.contrib.auth.models import User

from rest_framework import generics

from .serializers import UserSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveUpdateDestoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(pk=self.kwargs['pk'])
