from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import TodoForm

#Fetch all todos from the database and display them
def index(request):    
    form = TodoForm()
    all_todos = TodoItem.objects.order_by('id')
    context = {'all_todos':all_todos, 'form':form}
    return render(request, 'todo/index.html', context)

#Add a new todo and save it
def addTodo(request):
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return redirect('index')

#If todo is clicked, it will be marked as completed
def completeTodo(request, todo_id):
    item_completed = TodoItem.objects.get(pk=todo_id)
    item_completed.completed = True
    item_completed.save()
    return redirect('index')

#User can also deselect a todo
def deselectTodo(request, todo_id):
    item = TodoItem.objects.get(pk=todo_id)
    item.completed = False
    item.save()
    return redirect('index')

#Delete completed/selected items
def deleteCompleted(request):
    TodoItem.objects.filter(completed=True).delete()
    return redirect('index')