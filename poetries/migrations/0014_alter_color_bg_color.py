# Generated by Django 3.2.5 on 2021-07-31 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poetries', '0013_alter_color_bg_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='bg_color',
            field=models.CharField(choices=[('css/default_color_bg.css', 'css/default_color_bg.css'), ('css/purple_color_bg.css', 'css/purple_color_bg.css')], default='default_color_bg', max_length=50),
        ),
    ]
