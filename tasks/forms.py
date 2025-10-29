from django.forms import ModelForm, TextInput, Textarea, Select, DateField, DateInput, FileInput
from tasks.models import Task, Comment

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "status", "priority", "due_date"]

        widgets = {
            "name": TextInput(attrs={"class": "form-control", "placeholder": "Назва задачі", "required": True}), 
            "description": Textarea(attrs={"class": "form-control", "placeholder": "Опис задачі", "required": True}),
            "status": Select(attrs={"class": "form-control", "required": True}),
            "priority": Select(attrs={"class": "form-control", "required": True}),
            "due_date": DateInput(attrs={"class": "form-control", "required": False, "type": "date"})
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["content", "media"]
        widgets = {
            "content": Textarea(attrs={"class": "form-control", "placeholder": "Введіть коментар", "required": True}),
            "media": FileInput(),
        }