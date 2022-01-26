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
        Suburb = 'S', '近郊溪行程(Suburb)'
        Middle = 'M', '次高中游溪行程(Middle)'
        Alpine = 'A', '高山溪行程(Alpine)'

    activity_type = models.CharField(
        max_length=5,
        choices=ActivityTypes.choices,
        blank=True, null=True
    )


    class ActivityRequirements(models.TextChoices):
        NoRequirements = 'N', '不限基本資格'
        Member = 'Mem', '會員(巳繳納本年度會費者)'
        Experience = 'E', '溯溪體驗營結訓者'
        Basic = 'B', '會員且初級溯溪營結訓'
        Advanced = 'Adv', '會員且進階營結訓'
        Suburb = 'S', '近郊溪行程(Suburb)'
        Middle = 'M', '次高中游溪行程(Middle)'
        Alpine = 'A', '高山溪行程(Alpine)'
        Source = 'So', '溯源(Source)'
        Top = 'T', '溯源且登頂(Top)'

    activity_requirements = models.CharField(max_length=5, choices=ActivityRequirements.choices, blank=True, null=True)
    activity_requirements_count = models.IntegerField(blank=True, null=True)

    def get_leaders(self):
        return ",".join([p.last_name + p.first_name for p in self.leaders.all()])

    def get_participants(self):
        return ",".join([p.last_name + p.first_name for p in self.participants.all()])

    def __str__(self):
        return self.title