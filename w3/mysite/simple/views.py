from django.shortcuts import render

def index(request):
    return render(request, 'simple/index.html')

def result(request):
    ten = request.POST.get('ten')
    context={
            'ten': ten,}
    return render(request,'simple/result.html', context)
# Create your views here.
