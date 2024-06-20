# Generated by Django 5.0.3 on 2024-03-26 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paymentdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=200)),
                ('order_no', models.IntegerField()),
                ('total_cost', models.FloatField(default=0.0)),
                ('payment_status', models.CharField(default='paid', max_length=50)),
                ('useremail', models.CharField(default=None, max_length=50)),
            ],
        ),
    ]
