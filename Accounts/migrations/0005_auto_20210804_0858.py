# Generated by Django 3.2.4 on 2021-08-04 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0003_rename_movie_song_album'),
        ('Accounts', '0004_alter_playlist_song'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='song',
        ),
        migrations.AddField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(blank=True, to='UserApp.Song'),
        ),
        migrations.CreateModel(
            name='PlaylistSongs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.song')),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.playlist')),
            ],
            options={
                'db_table': 'PlaylistSongs',
            },
        ),
    ]