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
    authority = models.CharField(max_length=20, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'authority'

class Product(models.Model):
    productno = models.IntegerField(db_column='ProductNo', primary_key=True)  # Field name made lowercase.
    main_category = models.CharField(max_length=20, blank=True, null=True)
    middle_category = models.CharField(max_length=20, blank=True, null=True)
    sub_category = models.CharField(max_length=20, blank=True, null=True)
    professionalism_fee_rate = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    potential_fee_rate = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    additional_fee1 = models.IntegerField(blank=True, null=True)
    additional_fee2 = models.IntegerField(blank=True, null=True)
    additional_fee3 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'

class CoSalesman(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    resident_registration_number = models.CharField(max_length=20, blank=True, null=True)
    addresss = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    fee = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'co_salesman'


class Customer(models.Model):
    customer_name = models.CharField(primary_key=True, max_length=20)
    company_registration_number = models.IntegerField(blank=True, null=True)
    representative = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    opening_date = models.DateTimeField(blank=True, null=True)
    field1 = models.CharField(max_length=20, blank=True, null=True)
    field2 = models.CharField(max_length=20, blank=True, null=True)
    field3 = models.CharField(max_length=20, blank=True, null=True)
    sales_manager = models.CharField(max_length=20, blank=True, null=True)
    scm_manager = models.CharField(max_length=20, blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class CustomerPurchasing(models.Model):
    customer_purchasing_manager = models.CharField(primary_key=True, max_length=20)
    company_registration_number = models.IntegerField(blank=True, null=True)
    contact_number1 = models.CharField(max_length=20, blank=True, null=True)
    contact_number2 = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_purchasing'


class CustomerSettlement(models.Model):
    customer_settlement_manager = models.CharField(primary_key=True, max_length=20)
    company_registration_number = models.IntegerField(blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_settlement'

class Broker(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    resident_registration_number = models.CharField(max_length=20, blank=True, null=True)
    addresss = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    fee = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'broker'