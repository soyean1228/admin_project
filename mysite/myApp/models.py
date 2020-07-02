from django.db import models

class Employee(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    position = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=20, blank=True, null=True)
    phone_num = models.CharField(max_length=20, blank=True, null=True)
    office_num = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'

class Authority(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    authority = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authority'
