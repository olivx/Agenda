# Generated by Django 2.1.2 on 2019-01-17 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0007_auto_20181019_0039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_cidade', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'cidade',
                'ordering': ('nom_cidade',),
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_estado', models.CharField(max_length=255)),
                ('sgl_estado', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'estado',
            },
        ),
        migrations.RemoveField(
            model_name='ordemdecompra',
            name='cli_name',
        ),
        migrations.DeleteModel(
            name='OrdemDeCompra',
        ),
        migrations.AddField(
            model_name='cidade',
            name='cod_estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.Estado'),
        ),
    ]
