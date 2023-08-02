from django.shortcuts import render
# from django.shortcuts import render

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
     if request.method =='POST':
            print(request.POST)
            name = request.POST.get('username')
            email = request.POST.get('useremail')
            select = request.POST.get('select')
            return render (request,'./first_app_temp/about.html',{'name':name,'email':email,'select':select})
     else:
            return render (request,'./first_app_temp/about.html')


def submit_form(request):
    return render (request,'./first_app_temp/form.html')
    
