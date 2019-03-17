from django.shortcuts import render

# Create your views here.
def err_404(request):
    return render(request, 'err/not_found_404.html')