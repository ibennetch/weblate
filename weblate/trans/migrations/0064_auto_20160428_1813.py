# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 18:13
from __future__ import unicode_literals

from django.db import migrations, models
import weblate.trans.validators


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0063_whiteboardmessage_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='subproject',
            name='add_message',
            field=models.TextField(default='Added translation using Weblate (%(language_name)s)\n\n', help_text='You can use format strings for various information, please check documentation for more details.', validators=[weblate.trans.validators.validate_commit_message], verbose_name='Commit message when adding translation'),
        ),
        migrations.AddField(
            model_name='subproject',
            name='delete_message',
            field=models.TextField(default='Deleted translation using Weblate (%(language_name)s)\n\n', help_text='You can use format strings for various information, please check documentation for more details.', validators=[weblate.trans.validators.validate_commit_message], verbose_name='Commit message when removing translation'),
        ),
        migrations.AlterField(
            model_name='subproject',
            name='commit_message',
            field=models.TextField(default='Translated using Weblate (%(language_name)s)\n\nCurrently translated at %(translated_percent)s%% (%(translated)s of %(total)s strings)', help_text='You can use format strings for various information, please check documentation for more details.', validators=[weblate.trans.validators.validate_commit_message], verbose_name='Commit message when translating'),
        ),
        migrations.AlterField(
            model_name='whiteboardmessage',
            name='category',
            field=models.CharField(choices=[(b'info', 'Info (light blue)'), (b'warning', 'Warning (yellow)'), (b'danger', 'Danger (red)'), (b'success', 'Success (green)'), (b'primary', 'Primary (dark blue)')], default=b'info', help_text='Category defines color used for the message.', max_length=25, verbose_name='Category'),
        ),
    ]