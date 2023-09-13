from django.shortcuts import render,redirect
from book.forms import BookStoreForm
from book.models import BookModel
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import FormView,CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse

# Create your views here.
#functional base views
# def home(request):
#     return render(request,'store_book.html')


#now we learn to class base view

class MyTemplateView(TemplateView):
    template_name ='home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'name':'Rahim','age' :21}
        context.update(kwargs)
        print(kwargs)
        return context
    


# def store_book(request):
#     if request.method =='POST':
#         book = BookStoreForm(request.POST)
#         if book.is_valid():
#             book.save()
#             print(book.cleaned_data)
#             return redirect('showbook')
#     else:
#         book = BookStoreForm()
            
            
#     return render(request,'store_book.html',{'form':book})

# class BookFromView(FormView):
#     template_name ='store_book.html'
#     form_class = BookStoreForm

#     def form_valid(Self,form):
#         print(form.cleaned_data)
#         form.save()
#         return redirect('showbook')

class BookFromView(CreateView):
    model = BookModel
    template_name ='store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('showbook')


# def show_books(request):
#     book = BookModel.objects.all()
#     print(book)
#     return render(request,'show_book.html',{'data': book})

#class base view

class BookListView(ListView):
    model = BookModel
    template_name ='show_book.html'
    context_object_name ='data'
    # def get_queryset(self):
    #     return BookModel.objects.filter()
    
    # def get_context_data(self, **kwargs):
    #      context = super().get_context_data(**kwargs)
    #      context = {'rakib': BookModel.objects.all().order_by('genre')}
    #      return context
    
    ordering =['-id']
    
    
class BookDetailsView(DetailView):
        model = BookModel
        template_name ='book_detail.html'
        context_object_name ='items'
        pk_url_kwarg ='id'
    

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
    