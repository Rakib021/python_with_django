from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request,'./first_app/index.html',context ={"name":"I am  Rahim",
    "marks":86 ,"lst":[23,2,3,77],"blog":"Django Template Engine provides filters which are used to transform the values of variables and tag arguments.\
    We have already discussed majo"     })                                                      
                                        
                                        
                                     
        
        
        
        
