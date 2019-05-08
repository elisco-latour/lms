# Generated by Django 2.1.5 on 2019-03-27 06:44

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20190327_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='last_activity',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 27, 6, 44, 20, 360684, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='reg_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 27, 6, 44, 20, 360606, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='department',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 27, 6, 44, 20, 359867, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email_token',
            field=models.CharField(default='pbkdf2:sha256:50000$XX8uCB4L$c11b584e574dc8767ec274e363a3266aa19a4ab02988db878e3dc803f2f29744', max_length=1000),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='adminRemarkDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 27, 6, 44, 20, 448216, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='fromDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 27, 6, 44, 20, 448378, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='postingDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 27, 6, 44, 20, 448411, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='toDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 27, 6, 44, 20, 448438, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leavetype',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 27, 6, 44, 20, 447612, tzinfo=utc), null=True),
        ),
    ]