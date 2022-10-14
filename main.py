import os

import datetime
from django.utils import timezone
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402
from datacenter.models import Visit


def find_time_in_storage():
    now = datetime.datetime.now(timezone.utc)
    now_moscow = timezone.localtime(now)
    for visit in visits_inside:
        then = timezone.localtime(visit.entered_at)
        print('Зашёл в хранилище, время по Москве:', then, sep="\n")
        delta = now_moscow - then
        print('Находится в хранилище:', delta, sep="\n")
        print(visit.passcard)


if __name__ == '__main__':
    # Программируем здесь
    active_passcards = Passcard.objects.filter(is_active = True)
    # print("Активных пропусков", len(active_passcards))
    # print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    # visits_inside = Visit.objects.filter(leaved_at=None)
    # print(visits_inside[0].passcard.owner_name)
    # find_time_in_storage()
    visits_passcard = Visit.objects.filter(passcard=active_passcards[0])

    print(visits_passcard)
 
