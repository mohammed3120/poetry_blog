# Generated by Django 3.2.5 on 2021-07-31 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poetries', '0007_sentiment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentiment',
            name='action',
            field=models.CharField(choices=[('checked', 'checked'), ('', '')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='sentiment',
            name='happy',
            field=models.CharField(choices=[('checked', 'checked'), ('', '')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='sentiment',
            name='normal',
            field=models.CharField(choices=[('checked', 'checked'), ('', '')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='sentiment',
            name='romance',
            field=models.CharField(choices=[('checked', 'checked'), ('', '')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='sentiment',
            name='sad',
            field=models.CharField(choices=[('checked', 'checked'), ('', '')], default='', max_length=20),
        ),
    ]
