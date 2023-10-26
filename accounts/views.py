from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

User = get_user_model()

@api_view(['POST'])
def register(request):
    email = request.data.get('email')
    password = request.data.get('password')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')

    if email and password and first_name and last_name:
        user = User.objects.create_user(email, password, first_name=first_name, last_name=last_name)
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

    return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
