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

class SalesContact(models.Model):
    sales_num = models.AutoField(primary_key=True)
    product_model_name = models.CharField(max_length=20, blank=True, null=True)
    decision_quantity = models.IntegerField(blank=True, null=True)
    decision_price = models.IntegerField(blank=True, null=True)
    sales_price = models.IntegerField(blank=True, null=True)
    beginning_purchase = models.IntegerField(blank=True, null=True)
    scheduled_delivery_date = models.DateTimeField(blank=True, null=True)
    recipient = models.CharField(max_length=20, blank=True, null=True)
    recipient_phone = models.CharField(max_length=20, blank=True, null=True)
    delivery_address = models.CharField(max_length=100, blank=True, null=True)
    contact_conclusion_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_contact'

class Sales(models.Model):
    sales_num = models.IntegerField(primary_key=True)
    samsung_code = models.IntegerField(blank=True, null=True)
    samsung_manager = models.CharField(max_length=20, blank=True, null=True)
    point = models.CharField(max_length=20, blank=True, null=True)
    sales_manager = models.CharField(max_length=20, blank=True, null=True)
    broker_name = models.CharField(max_length=20, blank=True, null=True)
    scm_manager = models.CharField(max_length=20, blank=True, null=True)
    customer_name = models.CharField(max_length=20, blank=True, null=True)
    payment_method = models.CharField(max_length=20, blank=True, null=True)
    sales_type = models.CharField(max_length=20, blank=True, null=True)
    demand = models.CharField(max_length=20, blank=True, null=True)
    billing_place = models.CharField(max_length=20, blank=True, null=True)
    oppty_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales'

class Broker(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    resident_registration_number = models.CharField(max_length=20, blank=True, null=True)
    addresss = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    fee = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'broker'


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


class Delivery(models.Model):
    order_num = models.IntegerField(primary_key=True)
    quantity = models.IntegerField(blank=True, null=True)
    delivery_date = models.IntegerField(blank=True, null=True)
    return_date = models.IntegerField(blank=True, null=True)
    balance = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delivery'


class Deposit(models.Model):
    customer_name = models.CharField(primary_key=True, max_length=20)
    deposit_amount = models.IntegerField(blank=True, null=True)
    balance = models.IntegerField(blank=True, null=True)
    payment_method = models.CharField(max_length=20, blank=True, null=True)
    deposit_date = models.DateTimeField(blank=True, null=True)
    order_num = models.IntegerField(blank=True, null=True)
    scheduled_shipping_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deposit'

class Approval(models.Model):
    sales_num = models.IntegerField(primary_key=True)
    product_model_name = models.CharField(max_length=20, blank=True, null=True)
    approval_quantity = models.IntegerField(blank=True, null=True)
    approval_price = models.IntegerField(blank=True, null=True)
    quote_num = models.IntegerField(blank=True, null=True)
    balance = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'approval'
