from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Activity(models.Model):
    class Meta:
        db_table = 'activity'
        ordering = ['id']

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    owner = models.ForeignKey('auth.User', related_name='activities', on_delete=models.CASCADE, blank=True, null=True)
    leaders = models.ManyToManyField(User, related_name='leaders')
    participants = models.ManyToManyField(User, related_name='participants')

    created_on = models.DateField(default=date.today)
    
    register_date_start = models.DateField(default=date.today)
    register_date_due = models.DateField(null=True, blank=True)

    trip_date_start = models.DateField(null=True, blank=True)
    trip_date_end = models.DateField(null=True, blank=True)

    class ActivityTypes(models.TextChoices):
        Suburb = 'S', 'Suburb'
        Middle = 'M', 'Middle'
        Alpine = 'A', 'Alpine'

    activity_type = models.CharField(
        max_length=5,
        choices=ActivityTypes.choices,
        blank=True, null=True
    )


    class ActivityRequirements(models.TextChoices):
        NoRequirements = 'N', 'NoRequirements'
        Member = 'Mem', 'Member'
        Experience = 'E', 'Experience'
        Basic = 'B', 'Basic'
        Suburb = 'S', 'Suburb'
        Middle = 'M', 'Middle'
        Alpine = 'A', 'Alpine'
        Source = 'So', 'Source'
        Top = 'T', 'Top'

    activity_requirements = models.CharField(max_length=5, choices=ActivityRequirements.choices, blank=True, null=True)
    activity_requirements_count = models.IntegerField(blank=True, null=True)

    def get_leaders(self):
        return "\n".join([p.username for p in self.leaders.all()])

    def get_participants(self):
        return "\n".join([p.username for p in self.participants.all()])

    def __str__(self):
        return self.title