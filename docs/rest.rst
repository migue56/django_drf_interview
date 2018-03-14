===================
REQUEST SAlARIES
==================

Method
=======


When you use this api can see three options:


  Get
  Put
  Post


* To use Get, you can send a name

   url: http://localhost:8000/api/salarie/?name=AARON



* To  use Put, you can send a salary value on the post data:

    url: http://localhost:8000/api/salarie/
    data: {  "salary": "$100" }


* To use Post, you can send all the fields models.

    url: http://localhost:8000/api/salarie/
    data: {
            "name": "FULGIAM HUDSON,  DOMINIQUE",
            "position": "CLERK IV",
            "department": "HEALTH",
            "salary": "$63708.00"
        }


