# Generated by Django 2.1.5 on 2019-01-30 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20190130_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applybanner',
            name='useTwolines',
            field=models.BooleanField(default=True, help_text='If Show Two Lines of Text Bellow'),
        ),
    ]
