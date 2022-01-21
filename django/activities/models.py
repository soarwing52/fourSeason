from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create the Task class to describe the model.
class Activity(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    owner = models.ForeignKey('auth.User', related_name='activities', on_delete=models.CASCADE, blank=True, null=True)
    leaders = models.ManyToManyField(User, related_name='leaders')
    participants = models.ManyToManyField(User, related_name='participants')

    # Date the task was created.
    created_on = models.DateField(default=date.today)

    # Due date.
    due_date = models.DateField(default=date.today)

    # Meta data about the database table.
    class Meta:
        # Set the table name.
        db_table = 'activity'

        # Set default ordering
        ordering = ['id']

    def get_leaders(self):
        return "\n".join([p.username for p in self.leaders.all()])

    def get_participants(self):
        return "\n".join([p.username for p in self.participants.all()])

    # Define what to output when the model is printed as a string.
    def __str__(self):
        return self.title