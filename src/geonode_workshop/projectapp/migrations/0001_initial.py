# Generated by Django 3.2.23 on 2023-11-28 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0088_auto_20231019_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkshopModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('data', models.DateField(null=True)),
                ('description', models.TextField()),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.resourcebase')),
            ],
        ),
    ]
