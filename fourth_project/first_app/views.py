from django.shortcuts import render

def home(request):
    return render(request,'./first_app_temp/home.html',{"name" :"i am rahim","marks":86,
                  "courses":[
                      {
                          "id":1,
                          "course":"DBMS",
                          "teacher":"kawshik"
                      },
                      {
                          "id":2,
                          "course":"DSA",
                          "teacher":"SAHA"
                      },
                      {
                          "id":3,
                          "course":"DIP",
                          "teacher":"Tahmina"
                      },
                      {
                          "id":4,
                          "course":"Computer",
                          "teacher":"Meherab"
                      }
                  ]
                  
                  })
def about(request):
        return render(request,'./first_app_temp/about.html')
    
