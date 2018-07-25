# Generated by Django 2.0.6 on 2018-07-16 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20180714_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='name',
            field=models.CharField(max_length=20, verbose_name='站点名'),
        ),
        migrations.AlterField(
            model_name='smallcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Category', verbose_name='大分类'),
        ),
        migrations.AlterField(
            model_name='smallcategory',
            name='name',
            field=models.CharField(max_length=100, verbose_name='小分类'),
        ),
    ]