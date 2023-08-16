from django.shortcuts import render,redirect
from first_app.forms import TaskStoreForm
from first_app.models import TaskModel

# Create your views here.



def add_task(request):
    if request.method =='POST':
        task = TaskStoreForm(request.POST)
        if task.is_valid():
            task.save()
            # print(task.cleaned_data)
            return redirect('showTask')
    else:
        task = TaskStoreForm()
            
            
    return render(request,'add_task.html',{'form':task})


def show_task(request):
    task = taskModel.objects.all()
    # print(task)
    return render(request,'show_task.html',{'data': task})

def edit_task(request,id):
    task = taskModel.objects.get(pk = id)
    form = taskStoreForm(instance = task)
    if request.method =='POST':
        task = taskStoreForm(request.POST,instance=task)
        if task.is_valid():
            task.save()
            # print(task.cleaned_data)
            return redirect('showtask')
    return render(request,'add_task.html',{'form': form})


def delete_task(request,id):
     task = taskModel.objects.get(pk = id).delete()
     return redirect('showtask')
    