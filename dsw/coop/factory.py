from django.contrib.auth.models import BaseUserManager

class PlayerFactory(BaseUserManager):
    def create_user(self, form):
        player = form.save()
        player.set_password(player.password)
        player.save()

    def create_superuser(self, form):
        player = form.save()
        player.set_password(player.password)
        player.save()