from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Polls(models.Model):
    OPTIONS_CHOICES = (
                      ("Option1", "Вариант 1"),
                      ("Option2", "Вариант 2"),
                      ("Option3", "Вариант 3")
    )

    title = models.CharField(max_length=255)
    options = models.CharField(max_length=100, choices=OPTIONS_CHOICES, default="Option1")


class Categories(models.Model):
    name = models.CharField(max_length=255)


class Moderators(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=100)


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=100)
    approved_by = models.ForeignKey("Moderators", on_delete=models.DO_NOTHING)


class AppealAnswer(models.Model):
    SCORE_CHOICES = (
                    (1, 1),
                    (2, 2),
                    (3, 3),
                    (4, 4),
                    (5, 5)
    )

    appeal_id = models.ForeignKey("Appeal", on_delete=models.DO_NOTHING)
    text = models.TextField
    score = models.IntegerField(choices=SCORE_CHOICES, default=None)
    to_user_id = models.ForeignKey("Users", on_delete=models.DO_NOTHING)
    from_service_id = models.ForeignKey("Service", on_delete=models.DO_NOTHING)
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)


class AddressService(models.Model):
    category_id = models.ForeignKey("Categories", on_delete=models.DO_NOTHING)
    service_id = models.ForeignKey("Service", on_delete=models.DO_NOTHING)


class Appeal(models.Model):
    STATUS_CHOICES = (
                     ("REGISTERED", "Зарегестрированно"),
                     ("ACCEPTED", "Принято"),
                     ("IN PROGRESS", "На рассмотрении"),
                     ("CONFIRMED", "Подтверждено"),
                     ("REJECTED", "Отклонено")
    )

    text = models.TextField
    author_id = models.ForeignKey("Users", on_delete=models.DO_NOTHING)
    address_id = models.ForeignKey("AddressService", on_delete=models.DO_NOTHING)
    category_id = models.ForeignKey("Categories", on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    phone_regexp = RegexValidator(regex=r'^\+?1?\d{11}$')
    phone_number = models.CharField(validators=[phone_regexp], max_length=12, blank=True)
    email = models.EmailField(max_length=255)
    approved_by = models.ForeignKey("Moderators", on_delete=models.DO_NOTHING)
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="NULL")


class Users(models.Model):
    name = models.TextField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=100)
    rating = models.FloatField()


class Comments(models.Model):
    user_id = models.ForeignKey("Users", on_delete=models.DO_NOTHING)
    text = models.TextField
    post_id = models.ForeignKey("Posts", on_delete=models.DO_NOTHING)
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)


class Posts(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField
    author_id = models.ForeignKey("Service", on_delete=models.DO_NOTHING)
    category_id = models.ForeignKey("Categories", on_delete=models.DO_NOTHING)
    picture = models.ImageField()
    poll_id = models.ForeignKey("Polls", on_delete=models.DO_NOTHING)
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    approved_by = models.ForeignKey("Moderators", on_delete=models.DO_NOTHING)
