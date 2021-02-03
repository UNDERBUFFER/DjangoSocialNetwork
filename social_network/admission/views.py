from . import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response


class Admission(CreateAPIView):
    serializer_class = serializers.POSTAdmission
    act = None

    def post(self, request, *args, **kwargs):
        if self.act == 'registration':
            data = super().post(request, *args, **kwargs).data
            system = True
        else:
            data = request.data
            system = False
        try:
            user = authenticate(
                email=data['email'], password=data['password'], system=system)
            if user is None:
                return Response()
        except:
            return Response()
        token, _ = Token.objects.get_or_create(user=user)
        url = '/user/{}'.format(user.id)
        return Response({'token': token.key, 'url': url})
