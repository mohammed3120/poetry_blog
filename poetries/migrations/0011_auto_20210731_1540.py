# Generated by Django 3.2.5 on 2021-07-31 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('poetries', '0010_auto_20210731_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentiment',
            name='filterPostsType',
            field=models.CharField(choices=[('poetry', 'poetry'), ('reflection', 'reflection'), ('real_story', 'real_story'), ('I_read_you', 'I_read_you')], default='default_color_bg', max_length=20),
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_color', models.CharField(choices=[('default_color_bg', 'default_color_bg'), ('purple_color_bg', 'purple_color_bg')], default='default_color_bg', max_length=50)),
                ('theme_color', models.CharField(choices=[('default_colors_theme', 'default_colors_theme'), ('green_colors_theme', 'green_colors_theme'), ('golden_colors_theme', 'golden_colors_theme'), ('bold_brown_colors_theme', 'bold_brown_colors_theme'), ('light_blue_colors_theme', 'light_blue_colors_theme'), ('black_colors_theme', 'black_colors_theme'), ('light_green_colors_theme', 'light_green_colors_theme'), ('oily_colors_theme', 'oily_colors_theme'), ('blue_colors_theme', 'blue_colors_theme'), ('brown_colors_theme', 'brown_colors_theme')], default='default_color_bg', max_length=50)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]