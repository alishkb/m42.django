from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    def handle(self, *args, **options):
        normal_user, normal_created = Group.objects.get_or_create(name='کاربران ساده')
        writer_user, writer_created = Group.objects.get_or_create(name='نویسندگان')
        editor_user, editor_created = Group.objects.get_or_create(name='ویراستاران')
        admin_user, admin_created = Group.objects.get_or_create(name='مدیران')
        if normal_created and writer_created and editor_created and admin_created:
            self.stdout.write(self.style.SUCCESS('Accounts Per created successfully'))
        else:
            self.stderr.write("Accounts Per created before. Can't to create them again")

        try:
            view_user = Permission.objects.get(codename='view_user')
            edit_user = Permission.objects.get(codename='change_user')
            add_user = Permission.objects.get(codename='add_user')
            delete_user = Permission.objects.get(codename='delete_user')
        except:
            self.stdout.write(self.style.ERROR("It's impossible to find permissions of User model"))
        else:
            admin_user.permissions.add(view_user)
            admin_user.permissions.add(edit_user)
            admin_user.permissions.add(add_user)
            admin_user.permissions.add(delete_user)
            
            self.stdout.write(self.style.SUCCESS('Permissions of User model added to groups successfully'))