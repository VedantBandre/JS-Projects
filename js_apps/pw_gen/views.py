from django.shortcuts import render

# Create your views here.

def pw_gen(request):
    return render(request, 'pw_gen/pw_gen.html')