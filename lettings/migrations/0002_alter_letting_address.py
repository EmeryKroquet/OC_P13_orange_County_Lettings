# Generated by Django 4.2.7 on 2023-11-08 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letting',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lettings.address'),
        ),
    ]