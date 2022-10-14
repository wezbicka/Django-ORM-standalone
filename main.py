import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    passcards = Passcard.objects.all()
    print(passcards)
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
