# Generated by Django 4.2.3 on 2023-10-18 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('description', models.TextField(verbose_name='描述')),
                ('hidden', models.BooleanField(default=False, verbose_name='隐藏')),
                ('auto_trigger', models.BooleanField(default=False, verbose_name='自动触发')),
                ('reward_points', models.PositiveIntegerField(default=0, verbose_name='奖励积分')),
            ],
            options={
                'verbose_name': '成就',
                'verbose_name_plural': '成就',
            },
        ),
        migrations.CreateModel(
            name='AchievementType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='名称')),
                ('description', models.TextField(blank=True, verbose_name='描述')),
                ('badge', models.ImageField(upload_to='achievement/badges/', verbose_name='徽章')),
                ('avatar', models.ImageField(upload_to='achievement/avatars/', verbose_name='图标')),
            ],
            options={
                'verbose_name': '成就类型',
                'verbose_name_plural': '成就类型',
            },
        ),
        migrations.CreateModel(
            name='AchievementUnlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='解锁时间')),
                ('private', models.BooleanField(default=False, verbose_name='不公开')),
                ('achievement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='achievement.achievement', verbose_name='解锁成就')),
            ],
            options={
                'verbose_name': '成就解锁记录',
                'verbose_name_plural': '成就解锁记录',
            },
        ),
    ]