from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    def handle(self, *args, **options):
        normal_user, normal_created = Group.objects.get_or_create(name='کاربران ساده')
        writer_user, writer_created = Group.objects.get_or_create(name='نویسندگان')
        editor_user, editor_created = Group.objects.get_or_create(name='ویراستاران')
        admin_user, admin_created = Group.objects.get_or_create(name='مدیران')
        if normal_created and writer_created and editor_created and admin_created:
            self.stdout.write(self.style.SUCCESS('Groups created successfully'))
        else:
            self.stderr.write("Groups created before. Can't to create them again")

        try:
            view_comment = Permission.objects.get(codename='view_comment')
            edit_comment = Permission.objects.get(codename='change_comment')
            add_comment = Permission.objects.get(codename='add_comment')
            delete_comment = Permission.objects.get(codename='delete_comment')
        except:
            self.stdout.write(self.style.ERROR("It's impossible to find permissions of comment model"))
        else:
            normal_user.permissions.add(view_comment)
            normal_user.permissions.add(add_comment)

            writer_user.permissions.add(view_comment)
            writer_user.permissions.add(edit_comment)
            writer_user.permissions.add(add_comment)
            writer_user.permissions.add(delete_comment)

            editor_user.permissions.add(view_comment)
            editor_user.permissions.add(edit_comment)
            editor_user.permissions.add(add_comment)
            editor_user.permissions.add(delete_comment)

            admin_user.permissions.add(view_comment)
            admin_user.permissions.add(edit_comment)
            admin_user.permissions.add(add_comment)
            admin_user.permissions.add(delete_comment)
            
            self.stdout.write(self.style.SUCCESS('Permissions of comment model added to groups successfully'))

        try:
            view_post = Permission.objects.get(codename='view_post')
            edit_post = Permission.objects.get(codename='change_post')
            add_post = Permission.objects.get(codename='add_post')
            delete_post = Permission.objects.get(codename='delete_post')
        except:
            self.stdout.write(self.style.ERROR("It's impossible to find permissions of post model"))
        else:
            normal_user.permissions.add(view_post)

            writer_user.permissions.add(view_post)
            writer_user.permissions.add(edit_post)
            writer_user.permissions.add(add_post)
            writer_user.permissions.add(delete_post)

            editor_user.permissions.add(view_post)
            editor_user.permissions.add(edit_post)
            editor_user.permissions.add(add_post)
            editor_user.permissions.add(delete_post)

            admin_user.permissions.add(view_post)
            admin_user.permissions.add(edit_post)
            admin_user.permissions.add(add_post)
            admin_user.permissions.add(delete_post)

            self.stdout.write(self.style.SUCCESS('Permissions of post model added to groups successfully'))
        
        try:
            view_category = Permission.objects.get(codename='view_category')
            edit_category = Permission.objects.get(codename='change_category')
            add_category = Permission.objects.get(codename='add_category')
            delete_category = Permission.objects.get(codename='delete_category')
        except:
            self.stdout.write(self.style.ERROR("It's impossible to find permissions of category model"))
        else:
            normal_user.permissions.add(view_category)
            writer_user.permissions.add(view_category)
            editor_user.permissions.add(view_category)

            admin_user.permissions.add(view_category)
            admin_user.permissions.add(edit_category)
            admin_user.permissions.add(add_category)
            admin_user.permissions.add(delete_category)

            self.stdout.write(self.style.SUCCESS('Permissions of category model added to groups successfully'))

        try:
            view_tag = Permission.objects.get(codename='view_tag')
            edit_tag = Permission.objects.get(codename='change_tag')
            add_tag = Permission.objects.get(codename='add_tag')
            delete_tag = Permission.objects.get(codename='delete_tag')
        except:
            self.stdout.write(self.style.ERROR("It's impossible to find permissions of tag model"))
        else:
            normal_user.permissions.add(view_tag)
            normal_user.permissions.add(add_tag)

            writer_user.permissions.add(view_tag)
            writer_user.permissions.add(add_tag)

            editor_user.permissions.add(view_tag)
            editor_user.permissions.add(edit_tag)
            editor_user.permissions.add(add_tag)
            editor_user.permissions.add(delete_tag)

            admin_user.permissions.add(view_tag)
            admin_user.permissions.add(edit_tag)
            admin_user.permissions.add(add_tag)
            admin_user.permissions.add(delete_tag)

            self.stdout.write(self.style.SUCCESS('Permissions of tag model added to groups successfully'))

        try:
            accept_post = Permission.objects.get(codename='accept_post')
        except:
            self.stdout.write(self.style.ERROR("It's impossible to find permissions of accept post"))
        else:
            editor_user.permissions.add(accept_post)
            admin_user.permissions.add(accept_post)
            self.stdout.write(self.style.SUCCESS('Permissions of accept post added to groups successfully'))

        try:
            accept_comment = Permission.objects.get(codename='accept_comment')
        except:
            self.stdout.write(self.style.ERROR("It's impossible to find permissions of accept comment"))
        else:
            editor_user.permissions.add(accept_comment)
            admin_user.permissions.add(accept_comment)
            self.stdout.write(self.style.SUCCESS('Permissions of accept comment added to groups successfully'))
