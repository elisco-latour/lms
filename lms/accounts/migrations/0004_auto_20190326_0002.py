# Generated by Django 2.1.5 on 2019-03-26 00:02

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190326_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='emp_dept', to='accounts.Department'),
        ),
        migrations.AddField(
            model_name='leaves',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Employee'),
        ),
        migrations.AddField(
            model_name='leaves',
            name='leavetype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.LeaveType'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_activity',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 26, 0, 2, 20, 578755, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='reg_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 26, 0, 2, 20, 578691, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='department',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 26, 0, 2, 20, 577969, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email_token',
            field=models.CharField(default='pbkdf2:sha256:50000$7RkGEJJM$a1f897c785800a3801699bfb616342511a4938085c5dc4df216a22d3ef76b9f3', max_length=1000),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='adminRemarkDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 26, 0, 2, 20, 660370, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='fromDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 26, 0, 2, 20, 660527, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='toDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 26, 0, 2, 20, 660559, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leavetype',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 26, 0, 2, 20, 659759, tzinfo=utc), null=True),
        ),
    ]