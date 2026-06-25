from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):

    def handle(self,*args,**kwargs):

        User.objects.get_or_create(email="admin@test.com",defaults={"is_staff": True,"is_superuser": True,})
        user = User.objects.get(email="admin@test.com")
        user.set_password("admin123")
        user.save()