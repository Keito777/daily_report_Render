from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    '''AbstractUser(AbstractBaseUser, PermissionMixin)の全フィールドを継承
    |id|AbstractUser|
    |username|AbstractUser|
    |first_name|AbstractUser|
    |last_name|AbstractUser|
    |email|AbstractUser|
    |is_staff|AbstractUser|
    |is_active|AbstractUser|
    |date_joined|AbstractUser|
    |password|AbstractBaseUser|
    |last_login|AbstractBaseUser|
    |is_superuser|PermissionMixin|
    |groups|PermissionMixin|
    |user_permissions|PermissionMixin|
    ----------------------------------------
    <detail>
    
    |AbstractUser|
    id
    username = models.CharField(_("username"), max_length=150, unique=True, help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."), validators=[username_validator], error_messages={"unique": _("A user with that username already exists."),},)
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True)
    is_staff = models.BooleanField(_("staff status"), default=False, help_text=_("Designates whether the user can log into this admin site."),)
    is_active = models.BooleanField(_("active"), default=True, help_text=_("Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."),)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    |AbstractBaseUser|
    password = models.CharField(_("password"), max_length=128)
    last_login = models.DateTimeField(_("last login"), blank=True, null=True)

    |PermissionMixin|
    is_superuser = models.BooleanField(_("superuser status"), default=False, help_text=_("Designates that this user has all permissions without " "explicitly assigning them."),)
    groups = models.ManyToManyField(Group, verbose_name=_("groups"), blank=True, help_text=_("The groups this user belongs to. A user will get all permissions " "granted to each of their groups."), related_name="user_set", related_query_name="user",)
    user_permissions = models.ManyToManyField(Permission, verbose_name=_("user permissions"), blank=True, help_text=_("Specific permissions for this user."), related_name="user_set", related_query_name="user",)
    '''
    pass