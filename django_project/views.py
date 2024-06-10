import requests
from django.shortcuts import render

def home (request):
  # USING APIS
  response = requests.get('https://dog.ceo/api/breeds/image/random')
  data = response.json()
  results = data['message']
  
  return render(request, 'templates/index.html', {'results': results})

