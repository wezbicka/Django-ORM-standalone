import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    passcards = Passcard.objects.all()
    for card in passcards:
        print("owner_name:", card.owner_name)
        print("passcode:", card.passcode)
        print("created_at:", card.created_at)
        print("is_active:", card.is_active)
        
    print(passcards[99].owner_name)
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
