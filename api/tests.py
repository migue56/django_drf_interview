from django.test import TestCase

# Create your tests here.

from django.test import ( TestCase,
                            Client )



from .models import Salaries



class Build(TestCase):
    def setUp(self):
        for i in range(6):
            sal= Salaries()
            sal.name = 'name%i'%i
            sal.position  = 'position%i'%i
            sal.department  = 'department%i'%i
            sal.salary  = '%i'%i
            sal.save()
            print (sal)
            
        i=86
        sal= Salaries()
        sal.name = 'FULGIAM HUDSON,  DOMINIQUE'
        sal.position  = 'position%i'%i
        sal.department  = 'department%i'%i
        sal.salary  = '%i'%i
        #sal.save()
        print (sal)
            
class SalariesTest(Build):

    def test_get(self):
        
        name = 'HUDSON'
        url= '/api/salarie/?name=%s'%name
        response = self.client.get(url)
        
        self.assertEqual(response.status_code,200)
        
        self.assertContains(response, 'FULGIAM HUDSON,  DOMINIQUE')
    
    def test_put(self):
        id=1
        data = {"salary": "$100" }
        url = '/api/salarie/%i'%id
        response = self.client.put(url,data )
        self.assertEqual(response.status_code,200)
        self.assertContains(response, '$100')
        
        
    def test_post(self):
        data =  {
            "name": "FULGIAM HUDSON,  DOMINIQUE",
            "position": "CLERK IV",
            "department": "HEALTH",
            "salary": "$100"}
        
        url = '/api/salarie/'
        response = self.client.post(url, data)  
        self.assertEqual(response.status_code,200)
        self.assertContains(response, '$100')
        
     