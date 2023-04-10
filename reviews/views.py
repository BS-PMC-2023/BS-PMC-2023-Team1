from django.shortcuts import render


# Create your views here.
def viewForm(request):
    return render(request, 'reviews/reviews.html', None)


def viewSubmitted(request):
    return render(request, 'reviews/submitted.html', None)
