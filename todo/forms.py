from django import forms


class UserForm(forms.Form):
    first_name = forms.CharField(label='Your name', max_length=30)
    last_name = forms.CharField(label='Your surname', max_length=30)


class TasksForm(forms.Form):
    task_title = forms.Field(label='Task title')
    tasks = forms.Field(label='Tasks')
    state = forms.BooleanField(default='false')

    class Meta:
        model = List
        fields = ('title', 'text',)


class Username(forms.Form):
    user = forms.CharField(widget=forms.NameInput())
    password = forms.CharField(widget=forms.PasswordInput())

