# Generated by Django 3.0.8 on 2020-09-12 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streams', '0002_auto_20200912_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobrole',
            name='notes',
            field=models.TextField(default='\n        All related notes and materials are available at:\n\n<br>\n<a width="80%"   target="_blank"  href="paste drive link here" >Click Here</a>\n        '),
        ),
    ]
