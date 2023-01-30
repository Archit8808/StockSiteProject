# Generated by Django 4.1.5 on 2023-01-30 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0003_alter_services_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Financialstatements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BalanceSheets',
            fields=[
                ('financialstatements_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='playground.financialstatements')),
            ],
            bases=('playground.financialstatements', models.Model),
        ),
        migrations.CreateModel(
            name='CashflowStatements',
            fields=[
                ('financialstatements_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='playground.financialstatements')),
            ],
            bases=('playground.financialstatements', models.Model),
        ),
        migrations.CreateModel(
            name='IncomeStatements',
            fields=[
                ('financialstatements_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='playground.financialstatements')),
            ],
            bases=('playground.financialstatements', models.Model),
        ),
    ]
