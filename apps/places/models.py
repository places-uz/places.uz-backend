from django.db import models
from users.models import User

THEMES = (
    ("orange", "orange"),
    ("sky", "sky"),
    ("fuchsia", "fuchsia"),
    ("blue", "blue"),
    ("dark", "dark"),
    ("teal", "teal"),
    ("rose", "rose"),
    ("indigo", "indigo"),
    ("cyan", "cyan"),
    ("slate", "slate"),
)

CURRENCIES = (
    ("USD", "Usd"),
    ("SOUM", "Soum"),
)


class Place(models.Model):
    owner = models.ForeignKey(
        User, related_name="places", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255, unique=True)
    currency = models.CharField(
        choices=CURRENCIES, null=True, blank=True, default="SOUMS", max_length=255)
    main_language = models.CharField(null=True, blank=True, max_length=255)
    logo = models.ImageField(null=True, blank=True)
    cover = models.ImageField(null=True, blank=True)
    phone = models.CharField(max_length=255)
    wifi_password = models.CharField(null=True, blank=True, max_length=255)
    address = models.TextField()
    information = models.TextField(null=True, blank=True)
    work_hours_from = models.TextField(null=True, blank=True)
    work_hours_to = models.TextField(null=True, blank=True)
    theme = models.TextField(choices=THEMES, null=True,
                             blank=True, default="orange")

    def __str__(self):
        return self.name
