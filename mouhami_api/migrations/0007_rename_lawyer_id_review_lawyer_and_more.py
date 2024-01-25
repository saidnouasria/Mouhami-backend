# Generated by Django 5.0 on 2024-01-25 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mouhami_api', '0006_lawyer_wilaya_alter_lawyer_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='lawyer_id',
            new_name='lawyer',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='reviewer_id',
            new_name='reviewer',
        ),
        migrations.RemoveField(
            model_name='lawyer',
            name='reviews',
        ),
    ]