# Generated by Django 2.2.1 on 2019-05-15 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masjidaidsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masjid',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='masjids_uploaded', to='masjidaidsapp.User'),
        ),
    ]