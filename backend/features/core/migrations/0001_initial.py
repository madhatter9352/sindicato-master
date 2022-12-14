# Generated by Django 4.1.2 on 2022-10-25 00:52

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Act',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('type', models.CharField(max_length=45, verbose_name='Type')),
                ('date', models.DateField(verbose_name='Date')),
                ('attendance_percentage', models.FloatField(verbose_name='Attendance percentage')),
                ('place', models.CharField(max_length=255, verbose_name='Percentage')),
                ('start_time', models.TimeField(verbose_name='Start time')),
                ('end_time', models.TimeField(verbose_name='End time')),
                ('direct', models.CharField(max_length=255, verbose_name='Direct')),
                ('guest', models.CharField(max_length=255, verbose_name='Guest')),
                ('order_gives', models.TextField(verbose_name='Order gives')),
                ('body', models.TextField(verbose_name='Body')),
            ],
            options={
                'verbose_name': 'Act',
                'verbose_name_plural': 'Acts',
                'db_table': 'tbl_act',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Affiliate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('high_date', models.DateField(verbose_name='High Date')),
                ('low_date', models.DateField(verbose_name='Low Date')),
                ('salary', models.FloatField(verbose_name='Salary')),
                ('monthly_quota', models.FloatField(verbose_name='Monthly quota')),
                ('annual_quota', models.FloatField(verbose_name='Annual quota')),
                ('contribution_commitment', models.FloatField(verbose_name='Contribution commitment')),
                ('month_contribution', models.CharField(max_length=255, verbose_name='Month contribution')),
            ],
            options={
                'verbose_name': 'Affiliate',
                'verbose_name_plural': 'Affiliates',
                'db_table': 'tbl_affiliate',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
                'db_table': 'tbl_area',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='InitialState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('total_number_workers', models.IntegerField(verbose_name='Total number workers')),
                ('total_number_affiliates', models.IntegerField(verbose_name='Total number affiliates')),
                ('gross_potential', models.FloatField(verbose_name='Gross potential')),
                ('net_potential', models.FloatField(verbose_name='Net potential')),
                ('accumulated_ten_percent', models.FloatField(verbose_name='Accumulated ten percent')),
                ('fully_committed', models.IntegerField(verbose_name='Fully committed')),
                ('amount', models.FloatField(verbose_name='Fully committed')),
                ('year', models.IntegerField(verbose_name='Fully committed')),
            ],
            options={
                'verbose_name': 'Initial State',
                'verbose_name_plural': 'Initials State',
                'db_table': 'tbl_initial_state',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='UnionSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.area')),
                ('initial_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.initialstate')),
            ],
            options={
                'verbose_name': 'UnionSection',
                'verbose_name_plural': 'UnionSections',
                'db_table': 'tbl_union_section',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.area')),
            ],
            options={
                'verbose_name': 'Donation',
                'verbose_name_plural': 'Donations',
                'db_table': 'tbl_donation',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='DepositFinance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('date', models.DateField(verbose_name='Date')),
                ('total_number_workers', models.IntegerField(verbose_name='Total number workers')),
                ('total_number_affiliates', models.IntegerField(verbose_name='Total number affiliates')),
                ('al_da', models.IntegerField(verbose_name='Al da')),
                ('unlisted', models.IntegerField(verbose_name='Unlisted')),
                ('with_arrears', models.IntegerField(verbose_name='With arrears')),
                ('liquidated_year', models.IntegerField(verbose_name='Liquidated year')),
                ('high', models.FloatField(verbose_name='High')),
                ('low', models.FloatField(verbose_name='Low')),
                ('to_quote', models.FloatField(verbose_name='To quote')),
                ('quoted', models.FloatField(verbose_name='Quoted')),
                ('earring', models.FloatField(verbose_name='Earring')),
                ('ten_percent', models.FloatField(verbose_name='Ten percent')),
                ('net_quoted', models.FloatField(verbose_name='Net quoted')),
                ('ten_percent_accumulated', models.FloatField(verbose_name='Ten percent accumulated')),
                ('reduction', models.FloatField(verbose_name='Reduction')),
                ('total_balance', models.FloatField(verbose_name='Total balance')),
                ('union_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.unionsection')),
            ],
            options={
                'verbose_name': 'Deposit Finance',
                'verbose_name_plural': 'Deposit Finances',
                'db_table': 'tbl_deposit_finance',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ContributionDeposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('total_number_workers', models.IntegerField(verbose_name='Total number workers')),
                ('total_number_committed', models.IntegerField(verbose_name='Total number committed')),
                ('to_deposit', models.FloatField(verbose_name='To deposit')),
                ('deposited', models.FloatField(verbose_name='Deposited')),
                ('high', models.FloatField(verbose_name='High')),
                ('low', models.FloatField(verbose_name='Low')),
                ('earring', models.FloatField(verbose_name='Earring')),
                ('union_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.unionsection')),
            ],
            options={
                'verbose_name': 'Contribution Deposit',
                'verbose_name_plural': 'Contribution Deposits',
                'db_table': 'tbl_contribution_deposit',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Approach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('approach', models.TextField(verbose_name='Approach')),
                ('type', models.CharField(max_length=255, verbose_name='Type')),
                ('act', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.act')),
                ('affiliate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.affiliate')),
            ],
            options={
                'verbose_name': 'Approach',
                'verbose_name_plural': 'Approaches',
                'db_table': 'tbl_approach',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('agreement', models.TextField(verbose_name='Agreement')),
                ('responsible', models.CharField(max_length=255, verbose_name='Responsible')),
                ('compliance_date', models.DateField(max_length=255, verbose_name='Compliance date')),
                ('state', models.CharField(max_length=45, verbose_name='State')),
                ('act', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.act')),
            ],
            options={
                'verbose_name': 'Agreement',
                'verbose_name_plural': 'Agreements',
                'db_table': 'tbl_agreement',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='affiliate',
            name='initial_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.initialstate'),
        ),
        migrations.AddField(
            model_name='act',
            name='initial_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.initialstate'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('slug', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('position', models.IntegerField(verbose_name='Position')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('union_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.unionsection')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'tbl_user',
                'ordering': ['-created'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
