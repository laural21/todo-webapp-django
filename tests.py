from django.test import TestCase
from django.urls import reverse
from .models import TodoItem
from .forms import TodoForm

def create_todo(todo_text, c):
  TodoItem.objects.create(content=todo_text, completed=c)

class TodoItemModelTests(TestCase):
  def setUp(self):
    TodoItem.objects.create(content="test")
    
  def test_isCompleted(self):
    """Item is initialized as non-complete"""
    test_todo = TodoItem.objects.get(content="test")
    self.assertEqual(test_todo.completed, False)
    

class TodoFormFormTests(TestCase):
  def test_todo_form_valid_entry(self):
    """If the user has entered some text, the form is valid"""
    form = TodoForm(data={'content':'test'})
    self.assertTrue(form.is_valid())
    
  def test_todo_form_no_entry(self):
    """If the textbox is empty, the form is valid"""
    form = TodoForm(data={})
    self.assertFalse(form.is_valid())
   
class TodoItemIndexViewTests(TestCase):
  def test_all_todos_show(self):
    """All todos are shown regardless of their completion state"""
    create_todo("Todo1", True)
    create_todo("Todo2", False)
    test_form = TodoForm()
    response = self.client.post(reverse('todo/index'))
    self.assertQuerysetEqual(response.context['<TodoItem: Todo1>', '<TodoItem: Todo2>'],[test_form])
    
class TodoItemAddTodoViewTests(TestCase):
  def test_add_new_todo(self):
    """
    Check that the content entered is added to the todo list
    Also check that the length of the todo list indeed increased
    """
    test_form = TodoForm()
    new_todo = test_form.content
    num_items = TodoItem.objects.all().length()
    response = self.client.post(reverse('todo/add'))
    self.assertEqual(TodoItem.objects.all().length(), num_items+1)
    self.assertIn(new_todo, response.context)
  
class TodoItemCompleteTodoViewTest(TestCase):
  def test_complete_todo(self):
    """When a non-complete todo item is clicked, its state changes to completed"""
    create_todo("Todo1", False)
    test_todo = TodoItem.objects.get(content="test")
    self.client.post(reverse('todo/complete/'+test_todo.id))
    self.assertEqual(test_todo.completed, True)
  
class TodoItemDeselectTodoViewTest(TestCase):
  def test_deselect_todo(self):
      """When a completed todo item is clicked, it is deselected"""
      create_todo("Todo1", True)
      test_todo = TodoItem.objects.get(content="test")
      self.client.post(reverse('todo/deselect/'+test_todo.id))
      self.assertEqual(test_todo.completed, False)
      
class TodoItemDeleteCompletedViewTest(TestCase):
  def test_delete_todo(self):
    """Currently selected items will be deleted from the database and won't be displayed"""
    create_todo("Todo1", True)
    create_todo("Todo2", False)
    test_form = TodoForm()
    response = self.client.post(reverse('todo/deleteCompleted'))
    self.assertQuerysetEqual(response.context['<TodoItem: Todo2>'],[test_form])