from django.db import models

class Employee(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    team = models.CharField(max_length=20, blank=True, null=True)
    position = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=20, blank=True, null=True)
    resident_registration_number = models.CharField(max_length=20, blank=True, null=True)
    rate = models.CharField(max_length=20, blank=True, null=True)
    phone_num = models.CharField(max_length=20, blank=True, null=True)
    office_num = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    charge = models.CharField(max_length=20, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    passwd = models.CharField(max_length=20, blank=True, null=True)
    authority = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'

class SamsungCode(models.Model):
    samsung_code = models.IntegerField(primary_key=True)
    manager = models.CharField(max_length=20)
    department = models.CharField(max_length=20, blank=True, null=True)
    phone_num = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'samsung_code'
        unique_together = (('samsung_code', 'manager'),)

class Product(models.Model):
    productno = models.CharField(primary_key=True, max_length=50)
    main_category = models.CharField(max_length=20, blank=True, null=True)
    middle_category = models.CharField(max_length=20, blank=True, null=True)
    sub_category = models.CharField(max_length=20, blank=True, null=True)
    professionalism_fee_rate = models.CharField(max_length=20, blank=True, null=True)
    potential_fee_rate = models.CharField(max_length=20, blank=True, null=True)
    additional_fee1 = models.CharField(max_length=20, blank=True, null=True)
    additional_fee2 = models.CharField(max_length=20, blank=True, null=True)
    additional_fee3 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'

class Broker(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    resident_registration_number = models.CharField(max_length=30, blank=True, null=True)
    addresss = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    fee = models.CharField(max_length=20, blank=True, null=True)
    team = models.CharField(max_length=20, blank=True, null=True)
    manager = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'broker'

class Customer(models.Model):
    customer_name = models.CharField(max_length=20, blank=True, null=True)
    company_registration_number = models.CharField(primary_key=True, max_length=20)
    representative = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    opening_date = models.DateTimeField(blank=True, null=True)
    field1 = models.CharField(max_length=20, blank=True, null=True)
    field2 = models.CharField(max_length=20, blank=True, null=True)
    field3 = models.CharField(max_length=20, blank=True, null=True)
    purchasing_manager = models.CharField(max_length=20, blank=True, null=True)
    purchasing_contact_number1 = models.CharField(max_length=20, blank=True, null=True)
    purchasing_contact_number2 = models.CharField(max_length=20, blank=True, null=True)
    purchasing_email = models.CharField(max_length=20, blank=True, null=True)
    settlement_manager = models.CharField(max_length=20, blank=True, null=True)
    settlement_contact_number = models.CharField(max_length=20, blank=True, null=True)
    settlement_email = models.CharField(max_length=20, blank=True, null=True)
    sales_manager = models.CharField(max_length=20, blank=True, null=True)
    scm_manager = models.CharField(max_length=20, blank=True, null=True)
    rate = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'

class TeamManager(models.Model):
    manager = models.CharField(primary_key=True, max_length=20)
    team = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_manager'

class Proposal(models.Model):
    contact_conclusion_date = models.DateTimeField(blank=True, null=True)
    samsung_code = models.IntegerField(blank=True, null=True)
    samsung_sales_manager = models.CharField(max_length=20, blank=True, null=True)
    point = models.CharField(max_length=20, blank=True, null=True)
    sales_manager = models.CharField(max_length=20, blank=True, null=True)
    broker = models.CharField(max_length=20, blank=True, null=True)
    scm_manager = models.CharField(max_length=20, blank=True, null=True)
    customer_name = models.CharField(max_length=20, blank=True, null=True)
    payment_method = models.CharField(max_length=20, blank=True, null=True)
    sales_type = models.CharField(max_length=20, blank=True, null=True)
    demand = models.CharField(max_length=20, blank=True, null=True)
    billing_place = models.CharField(max_length=20, blank=True, null=True)
    oppty_num = models.CharField(primary_key=True, max_length=20)
    productno = models.CharField(max_length=50, blank=True, null=True)
    buy_place = models.CharField(max_length=20, blank=True, null=True)
    decision_quantity = models.IntegerField(blank=True, null=True)
    decision_unit = models.IntegerField(blank=True, null=True)
    decision_price = models.IntegerField(blank=True, null=True)
    sales_unit = models.IntegerField(blank=True, null=True)
    sales_price = models.IntegerField(blank=True, null=True)
    delivery_request_date = models.DateTimeField(blank=True, null=True)
    recipitent = models.CharField(max_length=20, blank=True, null=True)
    recipient_phone1 = models.CharField(max_length=20, blank=True, null=True)
    recipient_phone2 = models.CharField(max_length=20, blank=True, null=True)
    delivery_address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proposal'

class Authority(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    authority = models.CharField(max_length=20, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'authority'

class Sales(models.Model):
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
    oppty_num = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'sales'

class CoSalesman(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    resident_registration_number = models.CharField(max_length=20, blank=True, null=True)
    addresss = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    fee = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'co_salesman'

class CustomerPurchasing(models.Model):
    customer_purchasing_manager = models.CharField(primary_key=True, max_length=20)
    company_registration_number = models.CharField(max_length=20, blank=True, null=True)
    contact_number1 = models.CharField(max_length=20, blank=True, null=True)
    contact_number2 = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_purchasing'


class CustomerSettlement(models.Model):
    customer_settlement_manager = models.CharField(primary_key=True, max_length=20)
    company_registration_number = models.CharField(max_length=20, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_settlement'

class SalesContent(models.Model):
    oppty_num = models.OneToOneField(Sales, models.DO_NOTHING, db_column='oppty_num', primary_key=True)
    product_model_name = models.CharField(max_length=20, blank=True, null=True)
    decision_quantity = models.IntegerField(blank=True, null=True)
    decision_price = models.IntegerField(blank=True, null=True)
    sales_price = models.IntegerField(blank=True, null=True)
    beginning_purchase = models.CharField(max_length=20, blank=True, null=True)
    delivery_request_date = models.DateTimeField(blank=True, null=True)
    recipient = models.CharField(max_length=20, blank=True, null=True)
    recipient_phone = models.CharField(max_length=20, blank=True, null=True)
    delivery_address = models.CharField(max_length=100, blank=True, null=True)
    contact_conclusion_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_content'
    
    # def number():
    #     num = SalesContent.objects.count()
    #     if num == None:
    #         return 1
    #     else:
    #         return num + 1

class CoSalesman(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    resident_registration_number = models.CharField(max_length=20, blank=True, null=True)
    addresss = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    fee = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'co_salesman'

class CustomerPurchasing(models.Model):
    customer_purchasing_manager = models.CharField(primary_key=True, max_length=20)
    company_registration_number = models.CharField(max_length=20, blank=True, null=True)
    contact_number1 = models.CharField(max_length=20, blank=True, null=True)
    contact_number2 = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_purchasing'

class CustomerSettlement(models.Model):
    customer_settlement_manager = models.CharField(primary_key=True, max_length=20)
    company_registration_number = models.CharField(max_length=20, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_settlement'


class Delivery(models.Model):
    order_num = models.OneToOneField('OrderData', models.DO_NOTHING, db_column='order_num', primary_key=True)
    quantity = models.IntegerField(blank=True, null=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    return_date = models.DateTimeField(blank=True, null=True)
    balance = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delivery'


class Deposit(models.Model):
    customer_name = models.CharField(max_length=20, blank=True, null=True)
    deposit_amount = models.IntegerField(blank=True, null=True)
    balance = models.IntegerField(blank=True, null=True)
    payment_method = models.CharField(max_length=20, blank=True, null=True)
    deposit_date = models.DateTimeField(blank=True, null=True)
    order_num = models.OneToOneField('OrderData', models.DO_NOTHING, db_column='order_num', primary_key=True)
    scheduled_shipping_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deposit'

class Approval(models.Model):
    quote_num = models.IntegerField(primary_key=True)
    oppty_num = models.ForeignKey('Sales', models.DO_NOTHING, db_column='oppty_num', blank=True, null=True)
    product_model_name = models.CharField(max_length=20, blank=True, null=True)
    approval_quantity = models.IntegerField(blank=True, null=True)
    approval_price = models.IntegerField(blank=True, null=True)
    balance = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'approval'
        
class OrderData(models.Model):
    order_num = models.IntegerField(primary_key=True)
    oppty_num = models.ForeignKey('Sales', models.DO_NOTHING, db_column='oppty_num', blank=True, null=True)
    product_model_name = models.CharField(max_length=20, blank=True, null=True)
    order_quantity = models.IntegerField(blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    quote_num = models.IntegerField(blank=True, null=True)
    scheduled_delivery_date = models.DateTimeField(blank=True, null=True)
    assignment = models.CharField(max_length=20, blank=True, null=True)
    recipient = models.CharField(max_length=20, blank=True, null=True)
    recipient_phone = models.CharField(max_length=20, blank=True, null=True)
    delivery_address = models.CharField(max_length=100, blank=True, null=True)
    balance = models.IntegerField(blank=True, null=True)
    order_close = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_data'

class UploadOrderFileModel(models.Model):
    title = models.TextField(default='')
    file = models.FileField(null=True)

class Scm(models.Model):
    oppty_num = models.CharField(max_length=20,primary_key=True)
    samsung_code = models.IntegerField(blank=True, null=True)
    samsung_manager = models.CharField(max_length=20, blank=True, null=True)
    sales_manager = models.CharField(max_length=20, blank=True, null=True)
    scm_manager = models.CharField(max_length=20, blank=True, null=True)
    customer_name = models.CharField(max_length=20, blank=True, null=True)
    recipient = models.CharField(max_length=20, blank=True, null=True)
    delivery_address = models.CharField(max_length=100, blank=True, null=True)
    recipient_phone = models.CharField(max_length=20, blank=True, null=True)
    product_model_name = models.CharField(max_length=20, blank=True, null=True)
    beginning_purchase = models.CharField(max_length=20, blank=True, null=True)
    order_quantity = models.IntegerField(blank=True, null=True)
    approval_price = models.IntegerField(blank=True, null=True)
    sales_price = models.IntegerField(blank=True, null=True)
    quote_num = models.IntegerField(blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    order_num = models.IntegerField(blank=True, null=True)
    delivery_request_date = models.DateTimeField(blank=True, null=True)
    scheduled_delivery_date = models.DateTimeField(blank=True, null=True)
    assignment = models.CharField(max_length=20, blank=True, null=True)
    billing_place = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scm'