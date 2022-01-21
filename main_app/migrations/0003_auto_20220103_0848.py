# Generated by Django 3.2.9 on 2022-01-03 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_fueling'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
                ('finish', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='fueling',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='fueling',
            name='date',
            field=models.DateField(verbose_name='fueling date'),
        ),
    ]
