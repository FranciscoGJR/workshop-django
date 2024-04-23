import datetime

from django.http import HttpResponse, JsonResponse

def get_datetime(request):
    return HttpResponse(datetime.datetime.utcnow())
