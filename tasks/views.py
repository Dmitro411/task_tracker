from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks import models
from tasks import forms

class TaskListView(ListView):
    model = models.Task
    context_object_name = 'tasks'
    template_name = 'tasks/tasks_list.html'
    ordering = ['-created_at']

class TasksCreateView(LoginRequiredMixin, CreateView):
    model = models.Task
    form_class = forms.TaskForm
    template_name = 'tasks/tasks_create.html'
    success_url = reverse_lazy("tasks-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TasksUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Task
    form_class = forms.TaskForm
    template_name = 'tasks/tasks_update.html'
    success_url = reverse_lazy("tasks-list")

class TasksDetailView(DeleteView):
    model = models.Task
    context_object_name = 'task'
    template_name = 'tasks/tasks_detail.html'

class TasksDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Task
    context_object_name = 'tasks/tasks_detail.html'
    success_url = reverse_lazy("tasks-list")