from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group


class Event(models.Model):
    """
    A events can created by user
    This model links to the Django auth User model to manage access permissions.
    """
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='users')
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField(default=timezone.now)
    participants = models.ManyToManyField(User, through='Participant', related_name="partcipating", blank=True)

    def __str__(self):
    	return self.title


class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s at %s" % (self.user, self.event)
