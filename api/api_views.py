from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.models import Salaries
from api.serializers import SalariesSerializer
from django.http.response import HttpResponse


class SalariesAPIView(GenericAPIView):
    queryset = Salaries.objects.all()
    serializer_class = SalariesSerializer

    def get(self, request, *args, **kwargs):
        
        name = request.query_params.get('name')  
        if name:  
           self.queryset= self.queryset.filter(name__contains=name)
        
        queryset = self.paginate_queryset(queryset=self.queryset)
        serializer = SalariesSerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)
    
    
    def post(self, request , *args, **kwargs):
        data_valid = SalariesSerializer(request.data)
        print (request.data)
        if data_valid.is_valid() :
                data_valid.save()
                return response(data_valid.data)
        else:
            return HttpResponse(status=404)
    
    def put(self, request, pk, *args, **kwargs):
        
        print (pk)
        data_salaries= Salaries.objects.filter(pk=pk)
        print (data_salaries)
        if data_salaries:
            print (request.data)
            data_salaries.salary=request.data.get('salary')
            data_salaries.save
            print (data_salaries)
            object = SalariesSerializer(data_salaries)
            return Response(object.data)
        return HttpResponse(status=404)
        
