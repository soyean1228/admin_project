# Generated by Django 3.0.6 on 2020-07-03 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_approval_delivery_deposit_sales_salescontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderData',
            fields=[
                ('order_num', models.IntegerField(primary_key=True, serialize=False)),
                ('sales_num', models.IntegerField(blank=True, null=True)),
                ('product_model_name', models.CharField(blank=True, max_length=20, null=True)),
                ('order_qunatity', models.IntegerField(blank=True, null=True)),
                ('order_date', models.DateTimeField(blank=True, null=True)),
                ('quote_num', models.IntegerField(blank=True, null=True)),
                ('scheduled_delivery_date', models.DateTimeField(blank=True, null=True)),
                ('assignment', models.CharField(blank=True, max_length=20, null=True)),
                ('recipient', models.CharField(blank=True, max_length=20, null=True)),
                ('recipient_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('delivery_address', models.CharField(blank=True, max_length=100, null=True)),
                ('balance', models.IntegerField(blank=True, null=True)),
                ('order_close', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'order_data',
                'managed': False,
            },
        ),
    ]
