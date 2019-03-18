from django.shortcuts import render


# Create your views here.
def err_404(request):
    return render(request, 'err/not_found_404.html')


def err_method(request):
    return render(request, 'err/wrong_method.html')


def err_no_right(request):
    return render(request, 'err/no_right.html')