# Generated by Django 4.0.1 on 2022-01-15 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_shape_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shape',
            old_name='length',
            new_name='height',
        ),
        migrations.AddField(
            model_name='shape',
            name='width',
            field=models.FloatField(default=5),
            preserve_default=False,
        ),
    ]
