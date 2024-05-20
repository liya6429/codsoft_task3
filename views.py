from django.shortcuts import render
from .models import Generate
import random

# Create your views here.
def home(request):
    if(request.method =='POST'):
        length=int(request.POST.get('password'))
        characters="!@#$%^&**()_+"
        numbers = '1234567890'
        lower_case = "qwertyuioplkjhgfdsazxcvbnm"
        upper_case = "QWERTYUIOPASDFGHJKLMNBVCXZ"
        join=characters + lower_case + numbers + upper_case
        data=''.join(random.choice(join) for _ in range(length))
        return render(request,'result.html',{'data':data})
    else:
        return render(request,'home.html')


    