# Generated by Django 2.1.5 on 2019-03-27 09:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20190327_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='last_activity',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 27, 9, 5, 21, 368202, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='reg_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 27, 9, 5, 21, 368130, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='department',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 27, 9, 5, 21, 367415, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email_token',
            field=models.CharField(default='pbkdf2:sha256:50000$bPssmaj2$21852d89ec5d0acc977c3d3f4689b24c9b05a9d2054e5c6bbcc10f2dc8914d7b', max_length=1000),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='adminRemarkDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 27, 9, 5, 21, 450226, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='fromDate',
            field=models.DateField(default=datetime.datetime(2019, 3, 27, 9, 5, 21, 450400, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='postingDate',
            field=models.DateField(default=datetime.datetime(2019, 3, 27, 9, 5, 21, 450432, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='toDate',
            field=models.DateField(default=datetime.datetime(2019, 3, 27, 9, 5, 21, 450459, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leavetype',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 27, 9, 5, 21, 449515, tzinfo=utc), null=True),
        ),
    ]
