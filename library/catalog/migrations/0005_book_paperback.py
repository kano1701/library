# Generated by Django 2.2.3 on 2019-07-02 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20190702_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='paperback',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]