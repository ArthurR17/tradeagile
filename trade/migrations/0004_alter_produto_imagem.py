# Generated by Django 5.0.7 on 2024-07-30 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_alter_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(default='media/trade.agile.png', upload_to='static/media/'),
        ),
    ]
