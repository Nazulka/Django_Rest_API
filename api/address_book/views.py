from django.http import JsonResponse


def apiOverview(request):
    return JsonResponse("API Base Point", safe=False)