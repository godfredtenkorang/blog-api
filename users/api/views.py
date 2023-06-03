from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.api.serializers import RegistrationSerializer

@api_view(['POST'])
def register_view(requset):
    if requset.method == 'POST':
        serializer = RegistrationSerializer(data=requset.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'successful registered a new user'
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)