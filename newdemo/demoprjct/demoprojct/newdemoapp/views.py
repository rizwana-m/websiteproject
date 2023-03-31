from django.http import HttpResponse
from django.shortcuts import render

from newdemoapp.models import Place, Teams


# Create your views here.
# def home(request):
#     return HttpResponse("welcome home")

# def about(request):
#     return render(request,"about.html")
#
# def contact(request):
#     return HttpResponse("hello am contact")
#
# def detail(request):
#     return render(request,"detail.html")
#
# def thanks(request):
#     return render(request,"thanks.html")





def demos(request):
    obj=Place.objects.all()
    ob=Teams.objects.all()

    return render(request, "index.html" ,{'result':obj,'res':ob})







#
# def operation(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     add = x + y
#     multi = x * y
#     div = x / y
#     sub = x - y
#     return render(request, "result.html", {'result1': add,'result2': multi,'result3': div,'result4': sub})













