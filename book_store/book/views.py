from django.shortcuts import render,redirect
from book.forms import BookStoreForm
from book.models import BookModel

# Create your views here.

def home(request):
    return render(request,'store_book.html')

def store_book(request):
    if request.method =='POST':
        book = BookStoreForm(request.POST)
        if book.is_valid():
            book.save()
            print(book.cleaned_data)
            return redirect('showbook')
    else:
        book = BookStoreForm()
            
            
    return render(request,'store_book.html',{'form':book})


def show_books(request):
    book = BookModel.objects.all()
    print(book)
    return render(request,'show_book.html',{'data': book})

def edit_book(request,id):
    book = BookModel.objects.get(pk = id)
    form = BookStoreForm(instance = book)
    if request.method =='POST':
        book = BookStoreForm(request.POST,instance=book)
        if book.is_valid():
            book.save()
            # print(book.cleaned_data)
            return redirect('showbook')
    return render(request,'store_book.html',{'form': form})


# def edit_boo(request,id):
#     book = BookModel.objects.get(pk=id)
#     form = BookStoreForm(instance=book)
#     if request.method =="POST":
#         book = BookStoreForm(request.POST,instance=book)
#         if book.is_valid():
#             book.save()
#             return redirect("showbook")
#     return render (doc) 
def delete_book(request,id):
     book = BookModel.objects.get(pk = id).delete()
     return redirect('showbook')
    