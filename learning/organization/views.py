from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Organization



@api_view(['POST'])
def create_organization(request):
    # get json data from request
    data = request.data

    params = request.query_params
    print(params)
    name = data.get('name')
    description = data.get('description')

    print(f"Received data: name={name}, description={description}")

    # Here you can add logic to save the organization to the database
    organization = Organization.objects.create(name=name, description=description)

    return JsonResponse({"message": "Organization created successfully."}, status=201)