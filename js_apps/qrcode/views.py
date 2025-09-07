from django.shortcuts import render

# Create your views here.

def qrcode(request):
    return render(request, 'qrcode/qrcode.html')