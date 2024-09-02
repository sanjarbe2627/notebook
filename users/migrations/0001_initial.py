# Generated by Django 5.1 on 2024-09-02 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(help_text='User email field', max_length=255, unique=True)),
                ('first_name', models.CharField(blank=True, help_text='User name', max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, help_text='User lastname', max_length=30, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='users')),
                ('instagram', models.URLField(blank=True, help_text='User instagram link', null=True)),
                ('twitter', models.URLField(blank=True, help_text='User twitter link', null=True)),
                ('facebook', models.URLField(blank=True, help_text='User facebook link', null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is_staff')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Register')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Users',
                'ordering': ['-date_joined'],
            },
        ),
    ]