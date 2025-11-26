from datetime import date

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import TodoForm
from .models import Todo


def todo_list(request):
    """Display todo items with simple status filtering."""

    status_filter = request.GET.get('status', 'all')
    todos = Todo.objects.all()
    if status_filter == 'pending':
        todos = todos.filter(is_completed=False)
    elif status_filter == 'completed':
        todos = todos.filter(is_completed=True)

    return render(
        request,
        'todos/todo_list.html',
        {
            'todos': todos,
            'status_filter': status_filter,
            'today': date.today(),
        },
    )


def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Todo created.')
        return redirect('todos:list')

    return render(request, 'todos/todo_form.html', {'form': form, 'heading': 'New Todo'})


def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        messages.success(request, 'Todo updated.')
        return redirect('todos:list')

    return render(
        request,
        'todos/todo_form.html',
        {
            'form': form,
            'heading': 'Edit Todo',
        },
    )


def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        messages.success(request, 'Todo removed.')
        return redirect('todos:list')

    return render(request, 'todos/todo_confirm_delete.html', {'todo': todo})


def todo_toggle(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.is_completed = not todo.is_completed
        todo.save(update_fields=['is_completed', 'updated_at'])
        messages.success(
            request,
            f"Marked '{todo.title}' as {'done' if todo.is_completed else 'pending'}.",
        )
    return redirect(request.GET.get('next') or reverse('todos:list'))
