from django.contrib.auth.base_user import BaseUserManager


class Usermanager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, image, username, email, password=None, phone=None, **extra_fields):
        user = self.model(**extra_fields,
                            email = self.normalize_email(email),
                            username=username,
                            image=image,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, image, username, email, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)

        return self._create_user(email=email, image=image, username=username, phone=phone, password=password, **extra_fields)

    def create_superuser(self, image, username, email, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        return self._create_user(email=email, image=image, phone=phone, username=username, password=password, **extra_fields)