from django.shortcuts import render

# Create your views here.
# request API and get JSON back

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import test
from . serializers import testSerializer

# now create test class to inherit api view

class testList(APIView):
	# read and get data
	def get(self, request):
		test1 = test.objects.all()
		# now serialize and convert to JSON
		serializer = testSerializer(test1, many=True)

		return Response(serializer.data)
	# go to url file 
	def post(self):
		pass