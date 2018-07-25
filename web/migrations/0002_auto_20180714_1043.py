# Generated by Django 2.0.7 on 2018-07-14 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='标题')),
                ('desc', models.CharField(blank=True, max_length=100, verbose_name='描述')),
                ('image_url', models.ImageField(upload_to='images/Site/%Y/%m/%d', verbose_name='图片')),
                ('true_url', models.URLField(blank=True, max_length=100, verbose_name='地址')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.SmallCategory', verbose_name='小分类')),
            ],
            options={
                'verbose_name': '站点',
                'verbose_name_plural': '站点',
                'ordering': ['created_time'],
            },
        ),
        migrations.RemoveField(
            model_name='guonei',
            name='category',
        ),
        migrations.RemoveField(
            model_name='haiwai',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='guonei',
            field=models.BooleanField(default=1),
        ),
        migrations.DeleteModel(
            name='Guonei',
        ),
        migrations.DeleteModel(
            name='Haiwai',
        ),
    ]