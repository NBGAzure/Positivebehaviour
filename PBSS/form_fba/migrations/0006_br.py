# Generated by Django 2.2.4 on 2020-02-03 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '__first__'),
        ('form_fba', '0005_remove_fba_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Br',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Post')),
            ],
        ),
    ]
