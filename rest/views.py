from .serializers import UserSerializer
from admission.backend import Backend
from django.shortcuts import redirect, render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User

#class View(CreateAPIView):
#    serializer_class = UserSerializer
#    def post(self, request):
#        print(request.data)
#        return super().post(request)

class ViewOneObject(APIView):
    def get(self, request, iden):
        try:
            obj = UserSerializer(Backend().get_user(iden))
        except:
            return redirect('/rest/create')
        return Response(obj.data)

class ViewCreateObject(CreateAPIView):
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return redirect('/rest/{}'.format(User.objects.last().id))