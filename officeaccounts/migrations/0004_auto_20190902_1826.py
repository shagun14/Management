# Generated by Django 2.2.4 on 2019-09-02 18:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('officeaccounts', '0003_auto_20190902_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=models.CharField(default=uuid.uuid4, max_length=50, unique=True),
        ),
    ]