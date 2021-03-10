from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, last_name, phone, password):
        # if not first_name:
        #     raise ValueError('Users must have "First Name"')
        if not last_name:
            raise ValueError('Users must have "Last Name"')
        # if not email:
        #     raise ValueError('Users must have "Email"')        
        if not phone:
            raise ValueError('Users must have "Phone"')

        # user = self.model(first_name=first_name, last_name=last_name, email=self.normalize_email(email), phone=phone)
        user = self.model(username=username, last_name=last_name, phone=phone)
        user.set_password(password)
        # user.groups = Group.objects.get(name='کاربران ساده')
        user.save(using=self._db)
        return user

    def create_superuser(self, username, last_name, phone, password):
        user = self.create_user(username, last_name, phone, password)
        user.is_admin = True
        user.save(using=self._db)
        return user