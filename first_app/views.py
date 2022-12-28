from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .class_ts import Prediction

# initialize class
obj = Prediction()

# Create your views here.
def index(request):
    return HttpResponse("Hello world!")

@csrf_exempt
def predict(request):
    if request.method == 'POST':
       
        input_text = request.POST['input']
        result = obj.process(input_text)
        output_json = {"input" : input_text, "output":result}
        # print(output_json)
        return HttpResponse(f'{output_json}')
        
        



    