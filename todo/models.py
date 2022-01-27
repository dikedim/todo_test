from django.db import models


class USER(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __init__(self, arg):
        super(USER, self).__init__()
        self.arg = arg


class List(models.Model):
    title = models.CharField(max_length=250)


class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    assigned_to = models.ManyToManyField(USER)
    creation_date = models.DateField(auto_now=True)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    #parent_task = models.ForeignKey('self')
    #list = models.ForeignKey(List)



