from django.http import HttpResponse
from django.shortcuts import render
import requests
from .models import *
import requests
import json
from .forms import *
# Create your views here.
def index(request):
    return render(request,'Detection\index.html')
# def add_pic(request):
#     if request.method=='POST':
#         form=Selectpic(request.POST,request.FILES)
#         if form.is_valid():
#             Image=form.save(commit=True)
#     else:
#         form=Selectpic()
#     return render(request,'Detection\input.html',{'form':form})

# def upload_image(request):
#     if request.method == 'POST':
#         form = Selectpic(request.POST, request.FILES)
#         if form.is_valid():
#             # Get the uploaded image file from the form
#             uploaded_file = request.FILES['image']
#             image_bytes = uploaded_file.read()
#             # server_key = form.cleaned_data['server_key']
            
#             # Process the uploaded file, for example, you can pass it to the FastAPI app for prediction
#             response = requests.post('http://localhost:8001/predict', data=image_bytes)
#             # response = requests.post('http://localhost:8001/predict', files={'file': uploaded_file})
#             prediction_result = response.json()

#             # Pass the prediction results to the template for rendering
#             return render(request,'Detection\result.html', {'prediction_result': prediction_result})
#     else:
#         form = Selectpic()
#     return render(request, 'Detection\input.html', {'form': form})



def upload_image(request):
    if request.method == 'POST':
        form = Selectpic(request.POST, request.FILES)
        if form.is_valid():
            Image=form.save(commit=True)
    else:
        form=Selectpic()
    return render(request, 'Detection\input.html',{'form':form})
    