# Generated by Django 2.0.3 on 2018-05-15 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedbap', '0006_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderId', models.IntegerField(primary_key=True, serialize=False)),
                ('orderDate', models.DateField(auto_now=True)),
                ('periodOption', models.CharField(default='F', max_length=1)),
                ('period', models.CharField(max_length=30, null=True)),
                ('quantity', models.FloatField()),
                ('totalPrice', models.FloatField(default=0.0)),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedbap.Product')),
                ('serialNum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedbap.User')),
            ],
        ),
    ]
