from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.models import Salaries
from api.serializers import SalariesSerializer
from django.http.response import HttpResponse


class SalariesAPIView(GenericAPIView):
    queryset = Salaries.objects.all()
    serializer_class = SalariesSerializer

    def get(self, request, *args, **kwargs):
        """
        Return a list of all the existing of Salaries, with the  param name  contain
              url: http://localhost:8000/api/salarie/?name=AARON
        """
        name = request.query_params.get('name')  
        if name:  
           self.queryset= self.queryset.filter(name__contains=name)
        
        queryset = self.paginate_queryset(queryset=self.queryset)
        serializer = SalariesSerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)
    
    
    def post(self, request , *args, **kwargs):
        """
        post:
        Create a new insance of Salies.
            url: http://localhost:8000/api/salarie/
            data: {
                    "name": "FULGIAM HUDSON,  DOMINIQUE",
                    "position": "CLERK IV",
                    "department": "HEALTH",
                    "salary": "$63708.00"
                }

 
        """
        data_valid = SalariesSerializer(data=request.data)
        if data_valid.is_valid():
            data_valid.save()
            return Response(data_valid.data)
        else:
            return HttpResponse(status=404)
    
    def put(self, request, pk, *args, **kwargs):
        """
        put:
        Change the values on data json of request
            url: http://localhost:8000/api/salarie/<id>
            data: {  "salary": "$100" }

        """
        data_salaries= Salaries.objects.get(pk=pk)
        data_valid = SalariesSerializer(data_salaries,data=request.data)
        if data_valid.is_valid():
            data_valid.save
            return Response(data_valid.data)
        return HttpResponse(status=404)
        
