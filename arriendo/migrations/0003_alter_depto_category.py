# Generated by Django 3.2.4 on 2021-06-21 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arriendo', '0002_auto_20210620_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depto',
            name='category',
            field=models.CharField(choices=[('VI', 'Viña del Mar'), ('SER', 'La Serena'), ('PUC', 'Pucon'), ('VIL', 'Villarrica'), ('VAL', 'Valdivia'), ('IQU', 'Iquique'), ('FRU', 'Frutillar')], default='Iquique', max_length=3),
        ),
    ]
