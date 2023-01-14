# Generated by Django 3.2.16 on 2022-11-20 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Proceso', '0004_auto_20221119_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='idCategoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehiculo', to='Proceso.categoria', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='idColor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehiculo', to='Proceso.color', verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='idEstado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehiculo', to='Proceso.estado', verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='idMarca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehiculo', to='Proceso.marca', verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='idModelo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehiculo', to='Proceso.modelo', verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='idNumeroPuertas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehiculo', to='Proceso.numeropuertas', verbose_name='Numero de puertas'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='idSubcategoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehiculo', to='Proceso.subcategoria', verbose_name='Subcategoria'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='idTipoMotor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehiculo', to='Proceso.tipomotor', verbose_name='Tipo de motor'),
        ),
    ]
