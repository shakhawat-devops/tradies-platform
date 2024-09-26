from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
  
    def create_user(self, email, password, first_name, last_name, **exargs):
    
        if not email or not password or not first_name or not last_name:
            raise ValueError("The submitted new user is missing required information")

        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            **exargs
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    # def create_user(self, email, password, **exargs):
    #     """
    #     Overridden method in the BaseUserManager class to create a user.
    #     """

    #     exargs.setdefault("is_superuser", False)
    #     return self.create_new_user(email, password, **exargs)

    def create_superuser(self, email, password, first_name, last_name, **exargs):
        """
        Overridden method in the BaseUserManager class to create a super user.
        """

        exargs.setdefault("is_superuser", True)
        return self.create_user(email, password, first_name, last_name, **exargs)
