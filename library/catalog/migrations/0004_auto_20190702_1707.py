# Generated by Django 2.2.3 on 2019-07-02 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_publisher_authors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='genre',
            name='catalog',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='catalog.Catalog'),
            preserve_default=False,
        ),
    ]
