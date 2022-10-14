import datetime

from django.utils import timezone
from django.db import models


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
    
    def get_duration(self):

        ''' Рассчитывает длительность визита. Она возвращает объект datetime.timedelta '''

        entry_time = timezone.localtime(self.entered_at)
        if self.leaved_at:
            exit_time = timezone.localtime(self.leaved_at)
            delta = exit_time - entry_time
        else:
            now = datetime.datetime.now(timezone.utc)
            now_moscow = timezone.localtime(now)
            delta = now_moscow - entry_time
        return delta

    def is_visit_long(self, minutes=60):
        """Определяет, подозрителен визит или нет. 
        minutes - ограничение, сверх этого времени визит считать долгим"""
        duration = self.get_duration()
        minutes_inside = int(duration.seconds) // 60
        is_strange = True if minutes_inside > minutes else False
        return is_strange