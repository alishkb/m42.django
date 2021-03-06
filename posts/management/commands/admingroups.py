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
            view_like_post = Permission.objects.get(codename='view_like_post')
            edit_like_post = Permission.objects.get(codename='change_like_post')
            add_like_post = Permission.objects.get(codename='add_like_post')
            delete_like_post = Permission.objects.get(codename='delete_like_post')
        except:
            self.stdout.write(self.style.ERROR("It's impossible to find permissions of like post model"))
        else:
            normal_user.permissions.add(view_like_post)
            normal_user.permissions.add(add_like_post)

            writer_user.permissions.add(view_like_post)
            writer_user.permissions.add(add_like_post)

            editor_user.permissions.add(view_like_post)
            editor_user.permissions.add(add_like_post)

            admin_user.permissions.add(view_like_post)
            admin_user.permissions.add(edit_like_post)
            admin_user.permissions.add(add_like_post)
            admin_user.permissions.add(delete_like_post)

            self.stdout.write(self.style.SUCCESS('Permissions of like post model added to groups successfully'))

        try:
            view_dislike_post = Permission.objects.get(codename='view_dislike_post')
            edit_dislike_post = Permission.objects.get(codename='change_dislike_post')
            add_dislike_post = Permission.objects.get(codename='add_dislike_post')
            delete_dislike_post = Permission.objects.get(codename='delete_dislike_post')
        except:
            self.stdout.write(self.style.ERROR("It's impossible to find permissions of dislike post model"))
        else:
            normal_user.permissions.add(view_dislike_post)
            normal_user.permissions.add(add_dislike_post)

            writer_user.permissions.add(view_dislike_post)
            writer_user.permissions.add(add_dislike_post)

            editor_user.permissions.add(view_dislike_post)
            editor_user.permissions.add(add_dislike_post)

            admin_user.permissions.add(view_dislike_post)
            admin_user.permissions.add(edit_dislike_post)
            admin_user.permissions.add(add_dislike_post)
            admin_user.permissions.add(delete_dislike_post)

            self.stdout.write(self.style.SUCCESS('Permissions of dislike post model added to groups successfully'))

        try:
            view_like_comment = Permission.objects.get(codename='view_like_comment')
            edit_like_comment = Permission.objects.get(codename='change_like_comment')
            add_like_comment = Permission.objects.get(codename='add_like_comment')
            delete_like_comment = Permission.objects.get(codename='delete_like_comment')
        except:
            self.stdout.write(self.style.ERROR("It's impossible to find permissions of like comment model"))
        else:
            normal_user.permissions.add(view_like_comment)
            normal_user.permissions.add(add_like_comment)

            writer_user.permissions.add(view_like_comment)
            writer_user.permissions.add(add_like_comment)

            editor_user.permissions.add(view_like_comment)
            editor_user.permissions.add(add_like_comment)

            admin_user.permissions.add(view_like_comment)
            admin_user.permissions.add(edit_like_comment)
            admin_user.permissions.add(add_like_comment)
            admin_user.permissions.add(delete_like_comment)

            self.stdout.write(self.style.SUCCESS('Permissions of like comment model added to groups successfully'))

        try:
            view_dislike_comment = Permission.objects.get(codename='view_dislike_comment')
            edit_dislike_comment = Permission.objects.get(codename='change_dislike_comment')
            add_dislike_comment = Permission.objects.get(codename='add_dislike_comment')
            delete_dislike_comment = Permission.objects.get(codename='delete_dislike_comment')
        except:
            self.stdout.write(self.style.ERROR("It's impossible to find permissions of dislike comment model"))
        else:
            normal_user.permissions.add(view_dislike_comment)
            normal_user.permissions.add(add_dislike_comment)

            writer_user.permissions.add(view_dislike_comment)
            writer_user.permissions.add(add_dislike_comment)

            editor_user.permissions.add(view_dislike_comment)
            editor_user.permissions.add(add_dislike_comment)

            admin_user.permissions.add(view_dislike_comment)
            admin_user.permissions.add(edit_dislike_comment)
            admin_user.permissions.add(add_dislike_comment)
            admin_user.permissions.add(delete_dislike_comment)

            self.stdout.write(self.style.SUCCESS('Permissions of dislike comment model added to groups successfully'))

        try:
            approve_post = Permission.objects.get(codename='approve_post')
        except:
            self.stdout.write(self.style.ERROR("It's impossible to find permissions of accept post"))
        else:
            editor_user.permissions.add(approve_post)
            admin_user.permissions.add(approve_post)
            self.stdout.write(self.style.SUCCESS('Permissions of approve post added to groups successfully'))

        try:
            active_post = Permission.objects.get(codename='active_post')
        except:
            self.stdout.write(self.style.ERROR("It's impossible to find permissions of active post"))
        else:
            writer_user.permissions.add(active_post)
            editor_user.permissions.add(active_post)
            admin_user.permissions.add(active_post)
            self.stdout.write(self.style.SUCCESS('Permissions of active post added to groups successfully'))

        try:
            approve_comment = Permission.objects.get(codename='approve_comment')
        except:
            self.stdout.write(self.style.ERROR("It's impossible to find permissions of accept comment"))
        else:
            editor_user.permissions.add(approve_comment)
            admin_user.permissions.add(approve_comment)
            self.stdout.write(self.style.SUCCESS('Permissions of approve comment added to groups successfully'))
