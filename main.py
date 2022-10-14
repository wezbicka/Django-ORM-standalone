import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    passcards = Passcard.objects.all()
    active_passcards = []
    for card in passcards:
        if card.is_active:
            active_passcards.append(card)
        
    print("Активных пропусков", len(active_passcards))
    print(active_passcards)
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
