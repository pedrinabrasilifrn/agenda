# Generated by Django 3.2.8 on 2023-01-17 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='imagem',
            field=models.ImageField(null=True, upload_to='contatos/'),
        ),
    ]