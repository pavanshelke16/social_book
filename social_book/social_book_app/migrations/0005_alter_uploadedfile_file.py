# Generated by Django 5.0.2 on 2024-02-22 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_book_app', '0004_remove_uploadedfile_user_alter_customuser_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='file',
            field=models.FileField(upload_to='media/'),
        ),
    ]