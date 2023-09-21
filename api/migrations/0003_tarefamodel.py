# Generated by Django 4.2.5 on 2023-09-21 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_disciplinamodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TarefaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('data_entrega', models.DateField()),
                ('concluida', models.BooleanField(default=False)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.alunomodel')),
                ('disciplinas', models.ManyToManyField(to='api.disciplinamodel')),
            ],
        ),
    ]
