# Generated by Django 3.0.6 on 2020-07-03 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_auto_20200702_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('sales_num', models.IntegerField(primary_key=True, serialize=False)),
                ('product_model_name', models.CharField(blank=True, max_length=20, null=True)),
                ('approval_quantity', models.IntegerField(blank=True, null=True)),
                ('approval_price', models.IntegerField(blank=True, null=True)),
                ('quote_num', models.IntegerField(blank=True, null=True)),
                ('balance', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'approval',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('order_num', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('delivery_date', models.IntegerField(blank=True, null=True)),
                ('return_date', models.IntegerField(blank=True, null=True)),
                ('balance', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'delivery',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('customer_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('deposit_amount', models.IntegerField(blank=True, null=True)),
                ('balance', models.IntegerField(blank=True, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=20, null=True)),
                ('deposit_date', models.DateTimeField(blank=True, null=True)),
                ('order_num', models.IntegerField(blank=True, null=True)),
                ('scheduled_shipping_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'deposit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('sales_num', models.IntegerField(primary_key=True, serialize=False)),
                ('samsung_code', models.IntegerField(blank=True, null=True)),
                ('samsung_manager', models.CharField(blank=True, max_length=20, null=True)),
                ('point', models.CharField(blank=True, max_length=20, null=True)),
                ('sales_manager', models.CharField(blank=True, max_length=20, null=True)),
                ('broker_name', models.CharField(blank=True, max_length=20, null=True)),
                ('scm_manager', models.CharField(blank=True, max_length=20, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=20, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=20, null=True)),
                ('sales_type', models.CharField(blank=True, max_length=20, null=True)),
                ('demand', models.CharField(blank=True, max_length=20, null=True)),
                ('billing_place', models.CharField(blank=True, max_length=20, null=True)),
                ('oppty_num', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sales',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SalesContact',
            fields=[
                ('sales_num', models.AutoField(primary_key=True, serialize=False)),
                ('product_model_name', models.CharField(blank=True, max_length=20, null=True)),
                ('decision_quantity', models.IntegerField(blank=True, null=True)),
                ('decision_price', models.IntegerField(blank=True, null=True)),
                ('sales_price', models.IntegerField(blank=True, null=True)),
                ('beginning_purchase', models.IntegerField(blank=True, null=True)),
                ('scheduled_delivery_date', models.DateTimeField(blank=True, null=True)),
                ('recipient', models.CharField(blank=True, max_length=20, null=True)),
                ('recipient_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('delivery_address', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_conclusion_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sales_contact',
                'managed': False,
            },
        ),
    ]
