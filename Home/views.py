from django.shortcuts import render

# Create your views here.
from django.http  import JsonResponse , response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import generics
from .models import USERdata
from .serializers import simpleModelserilizer




@csrf_exempt
def data_page(request):
    method = request.method.lower()
    if method == 'get':
        return JsonResponse({"method" : ['sam', 'kaka', 'tunde']})
    elif method == 'post':
        return JsonResponse({"data" : "Update"})

    return JsonResponse({"method": request.method})


# def home (request):

#     return render(request, 'index.html')
class simple_one(APIView):
 
    def get(self, request):
        content = USERdata.objects.all()
        return  JsonResponse({"data": simpleModelserilizer(content, many=True).data})

        


    # # pass

class DataListView(generics.ListAPIView):
    queryset  = USERdata.objects.all()
    serializer_class  = simpleModelserilizer

class DataOne(generics.RetrieveAPIView):
    queryset  = USERdata.objects.all()
    serializer_class  = simpleModelserilizer


class CreateData(generics.CreateAPIView):
    queryset  = USERdata.objects.all()
    serializer_class  = simpleModelserilizer


class UpdateData(generics.UpdateAPIView):
    queryset  = USERdata.objects.all()
    serializer_class  = simpleModelserilizer
    


