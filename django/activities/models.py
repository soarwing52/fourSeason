from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Activity(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    owner = models.ForeignKey('auth.User', related_name='activities', on_delete=models.CASCADE, blank=True, null=True)
    leaders = models.ManyToManyField(User, related_name='leaders')
    participants = models.ManyToManyField(User, related_name='participants')

    created_on = models.DateField(default=date.today)
    due_date = models.DateField(default=date.today)

    class Meta:
        db_table = 'activity'
        ordering = ['id']

    def get_leaders(self):
        return "\n".join([p.username for p in self.leaders.all()])

    def get_participants(self):
        return "\n".join([p.username for p in self.participants.all()])

    def __str__(self):
        return self.title