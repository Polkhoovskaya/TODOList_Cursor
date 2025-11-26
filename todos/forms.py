from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    due_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text='Optional, helps prioritize upcoming work.',
    )

    class Meta:
        model = Todo
        fields = ('title', 'description', 'due_date', 'is_completed')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

