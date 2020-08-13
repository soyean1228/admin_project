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
    email = models.CharField(max_length=50, blank=True, null=True)
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
        
class Proposal(models.Model):
    contact_conclusion_date = models.DateTimeField(blank=True, null=True)
    samsung_code = models.IntegerField(blank=True, null=True)
    samsung_sales_manager = models.CharField(max_length=20, blank=True, null=True)
    team = models.CharField(max_length=20, blank=True, null=True)
    sales_manager = models.CharField(max_length=20, blank=True, null=True)
    broker = models.CharField(max_length=20, blank=True, null=True)
    scm_manager = models.CharField(max_length=20, blank=True, null=True)
    customer_name = models.CharField(max_length=20, blank=True, null=True)
    company_registration_number = models.CharField(max_length=20, blank=True, null=True)
    payment_method = models.CharField(max_length=20, blank=True, null=True)
    sales_type = models.CharField(max_length=20, blank=True, null=True)
    demand = models.CharField(max_length=20, blank=True, null=True)
    billing_place = models.CharField(max_length=20, blank=True, null=True)
    oppty_num = models.CharField(primary_key=True, max_length=20)
    productno = models.CharField(max_length=50)
    buy_place = models.CharField(max_length=20, blank=True, null=True)
    decision_quantity = models.IntegerField(blank=True, null=True)
    decision_unit = models.IntegerField(blank=True, null=True)
    decision_price = models.IntegerField(blank=True, null=True)
    sales_unit = models.IntegerField(blank=True, null=True)
    sales_price = models.IntegerField(blank=True, null=True)
    delivery_request_date = models.DateTimeField(blank=True, null=True)
    recipient = models.CharField(max_length=20)
    recipient_phone1 = models.CharField(max_length=20, blank=True, null=True)
    recipient_phone2 = models.CharField(max_length=20, blank=True, null=True)
    delivery_address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proposal'
        unique_together = (('oppty_num', 'productno', 'recipient'),)
        
class OrderData(models.Model):
    order_num = models.IntegerField(primary_key=True)
    quote_num = models.IntegerField()
    oppty_num = models.CharField(max_length=20)
    productno = models.CharField(max_length=50)
    recipient = models.CharField(max_length=20)
    order_date = models.DateTimeField(blank=True, null=True)
    assignment = models.CharField(max_length=20, blank=True, null=True)
    order_quantity = models.IntegerField(blank=True, null=True)
    scheduled_delivery_date = models.DateTimeField(blank=True, null=True)
    order_balance = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_data'
        unique_together = (('order_num', 'productno', 'recipient', 'oppty_num', 'quote_num'),) 

class Scm(models.Model):
    contact_conclusion_date = models.DateTimeField(blank=True, null=True)
    samsung_code = models.IntegerField(blank=True, null=True)
    samsung_sales_manager = models.CharField(max_length=20, blank=True, null=True)
    team = models.CharField(max_length=20, blank=True, null=True)
    sales_manager = models.CharField(max_length=20, blank=True, null=True)
    broker = models.CharField(max_length=20, blank=True, null=True)
    scm_manager = models.CharField(max_length=20, blank=True, null=True)
    customer_name = models.CharField(max_length=20, blank=True, null=True)
    company_registration_number = models.CharField(max_length=20, blank=True, null=True)
    payment_method = models.CharField(max_length=20, blank=True, null=True)
    sales_type = models.CharField(max_length=20, blank=True, null=True)
    demand = models.CharField(max_length=20, blank=True, null=True)
    billing_place = models.CharField(max_length=20, blank=True, null=True)
    oppty_num = models.CharField(max_length=20)
    productno = models.CharField(max_length=50)
    buy_place = models.CharField(max_length=20, blank=True, null=True)
    decision_quantity = models.IntegerField(blank=True, null=True)
    decision_unit = models.IntegerField(blank=True, null=True)
    decision_price = models.IntegerField(blank=True, null=True)
    sales_unit = models.IntegerField(blank=True, null=True)
    sales_price = models.IntegerField(blank=True, null=True)
    delivery_request_date = models.DateTimeField(blank=True, null=True)
    recipient = models.CharField(max_length=20)
    recipient_phone1 = models.CharField(max_length=20, blank=True, null=True)
    recipient_phone2 = models.CharField(max_length=20, blank=True, null=True)
    delivery_address = models.CharField(max_length=100, blank=True, null=True)
    approval_quantity = models.IntegerField(blank=True, null=True)
    quote_num = models.IntegerField(blank=True, null=True)
    approval_unit = models.IntegerField(blank=True, null=True)
    approval_price = models.IntegerField(blank=True, null=True)
    order_num = models.IntegerField(blank=True, null=True)
    order_date = models.DateTimeField(blank=True, null=True)
    order_quantity = models.IntegerField(blank=True, null=True)
    assignment = models.CharField(max_length=20, blank=True, null=True)
    scheduled_delivery_date = models.DateTimeField(blank=True, null=True)
    in_date = models.DateTimeField(blank=True, null=True)
    in_amount = models.IntegerField(blank=True, null=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    billing_date = models.DateTimeField(blank=True, null=True)
    billing_amount = models.IntegerField(blank=True, null=True)
    scm_num = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scm'
    
    def get_num(self):
        data = Scm.objects.all()
        max = 0
        for i in data: 
            if(i.scm_num >= max):
                max = i.scm_num
        return max

class Approval(models.Model):
    quote_num = models.IntegerField(primary_key=True)
    oppty_num = models.CharField(max_length=20)
    productno = models.CharField(max_length=50)
    recipient = models.CharField(max_length=20)
    approval_quantity = models.IntegerField(blank=True, null=True)
    approval_unit = models.IntegerField(blank=True, null=True)
    approval_price = models.IntegerField(blank=True, null=True)
    approval_balance = models.IntegerField(blank=True, null=True)
    total_approval_balance = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'approval'
        unique_together = (('quote_num', 'oppty_num', 'productno', 'recipient'),)
        

class Deposit(models.Model):
    customer_name = models.CharField(max_length=20, blank=True, null=True)
    company_registration_number = models.CharField(primary_key=True, max_length=20)
    deposit_number = models.IntegerField()
    transaction_date = models.DateTimeField(blank=True, null=True)
    transaction_content = models.CharField(max_length=100, blank=True, null=True)
    in_amount = models.IntegerField(blank=True, null=True)
    out_amount = models.IntegerField(blank=True, null=True)
    deposit_balance = models.IntegerField(blank=True, null=True)
    order_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deposit'
        unique_together = (('company_registration_number', 'deposit_number'),)

class Delivery(models.Model):
    order_num = models.IntegerField(primary_key=True)
    company_registration_number = models.CharField(max_length=20)
    deposit_number = models.IntegerField()
    in_date = models.DateTimeField(blank=True, null=True)
    in_amount = models.IntegerField(blank=True, null=True)
    etc = models.CharField(max_length=50, blank=True, null=True)
    delivery_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delivery'
        unique_together = (('order_num', 'company_registration_number', 'deposit_number'),)

class Settlement(models.Model):
    order_num = models.IntegerField(primary_key=True)
    quote_num = models.IntegerField()
    oppty_num = models.CharField(max_length=20)
    productno = models.CharField(max_length=50)
    recipient = models.CharField(max_length=20)
    billing_date = models.DateTimeField(blank=True, null=True)
    billing_amount = models.IntegerField(blank=True, null=True)
    settlement_month = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settlement'
        unique_together = (('order_num', 'quote_num', 'oppty_num', 'productno', 'recipient'),) 
            
class CustomerDepositBalance(models.Model):
    company_registration_number = models.CharField(primary_key=True, max_length=20)
    deposit_balance = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_deposit_balance'
