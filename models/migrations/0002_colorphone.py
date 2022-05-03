# Generated by Django 4.0.4 on 2022-05-02 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('code', models.CharField(blank=True, max_length=200)),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.phone')),
            ],
        ),
    ]