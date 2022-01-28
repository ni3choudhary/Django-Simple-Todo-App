from django.shortcuts import render,redirect

# Create your views here.
from .models import Todo
from .forms import TodoForm

def index(request):
    todos = Todo.objects.all()
    form = TodoForm()
    if request.method =='POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'todos':todos,'form':form}
    return render(request,'todoapp/index.html',context)

def updateTask(request, pk):
    task = Todo.objects.get(id=pk)
    form = TodoForm(instance=task)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'todoapp/update_task.html',context)
    

def deleteTask(request, pk):
	item = Todo.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'todoapp/delete.html', context)