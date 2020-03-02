from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from form.serializers import RegistrationSerializer,LoginSerializer


@api_view(['POST'])
def registration_view(request):

	if request.method == 'POST':
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			account = serializer.save()
			data['response'] = 'successfully registered new user.'
		else:
			data = serializer.errors
		return Response(data)

@api_view(['POST'])
def login_view(request):
	if request.method == 'POST':
		serializer = LoginSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			account = serializer.authentication()
			if account == True :
				data['response'] = 'User successfully Login'

			else:
				data['response'] = 'You have entered an invalid username or password'
		return Response(data)
