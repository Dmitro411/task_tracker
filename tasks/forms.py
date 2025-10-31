from django.forms import ModelForm, Form, TextInput, Textarea, Select, DateField, DateInput, FileInput, ChoiceField
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

class TasksFIlterForm(Form):
    STATUS_CHOISES = [
        ("all", "Всі"),
        ("todo", "TO DO"),
        ("in_progress", "IN PROGRESS"),
        ("done", "DONE"),
    ]
    PRIORITY_CHOICES = [
        ("all", "Всі"),
        ("low", "LOW"),
        ("medium", "MEDIUM"),
        ("high", "HIGH"),
    ]

    status = ChoiceField(choices=STATUS_CHOISES, required=False, label="Статус", initial="all", widget=Select(attrs={"class": "form-control"}))
    priority = ChoiceField(choices=PRIORITY_CHOICES, required=False, label="Пріоритет", initial="all", widget=Select(attrs={"class": "form-control"}))
