



from django.http import HttpResponse


def home(equest):
    return HttpResponse("hello")