from django.http import JsonResponse


def homepage(request):
    print("Home page")
    list =[
        'rakib',
        'sakib',
        'makib'
    ]
    
    return JsonResponse(list,safe=False)