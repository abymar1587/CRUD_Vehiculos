# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Categoria(models.Model):
    id=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=10)

    def __str__(self):
        fila =self.descripcion
        return fila

class Subcategoria(models.Model):
    id=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=30)

    def __str__(self):
        fila =self.descripcion
        return fila

class Marca(models.Model):
    id=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=15)

    def __str__(self):
        fila =self.descripcion
        return fila
    
class Modelo(models.Model):
    id=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=15)

    def __str__(self):
        fila =self.descripcion
        return fila

class Color(models.Model):
    id=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=15)

    def __str__(self):
        fila =self.descripcion
        return fila

class Estado(models.Model):
    id=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=5)

    def __str__(self):
        fila =self.descripcion
        return fila

class NumeroPuertas(models.Model):
    id=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=3)

    def __str__(self):
        fila =self.descripcion
        return fila

class TipoMotor(models.Model):
    id=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=10)

    def __str__(self):
        fila =self.descripcion
        return fila

class Vehiculo(models.Model):
    id=models.AutoField(primary_key=True)
    imagen=models.ImageField(upload_to='imagenes/', verbose_name="Imagen", null=True)
    idCategoria=models.ForeignKey(Categoria, related_name='vehiculo', on_delete=models.CASCADE, verbose_name="Categoria", null=True)
    idSubcategoria=models.ForeignKey(Subcategoria, related_name='vehiculo', on_delete=models.CASCADE, verbose_name="Subcategoria", null=True)
    idMarca=models.ForeignKey(Marca, related_name='vehiculo', on_delete=models.CASCADE, verbose_name="Marca", null=True)
    idModelo=models.ForeignKey(Modelo, related_name='vehiculo', on_delete=models.CASCADE, verbose_name="Modelo", null=True)
    idColor=models.ForeignKey(Color, related_name='vehiculo', on_delete=models.CASCADE, verbose_name="Color", null=True)    
    año=models.CharField(max_length=4, verbose_name="Año", null=True)
    idEstado=models.ForeignKey(Estado, related_name='vehiculo', on_delete=models.CASCADE, verbose_name="Estado", null=True)
    kilometrosRec=models.CharField(max_length=10, verbose_name="Kilometro", null=True)
    numeroPasajeros=models.CharField(max_length=4, verbose_name="Numero de pasajeros", null=True)
    idNumeroPuertas=models.ForeignKey(NumeroPuertas, related_name='vehiculo', on_delete=models.CASCADE, verbose_name="Numero de puertas", null=True)
    idTipoMotor=models.ForeignKey(TipoMotor, related_name='vehiculo', on_delete=models.CASCADE, verbose_name="Tipo de motor", null=True)
    cilindraje=models.CharField(max_length=4, verbose_name="Cilindraje", null=True)
    tipoTransmision=models.CharField(max_length=20, verbose_name="Tipo de transmision", null=True)
    precio=models.IntegerField(verbose_name="Precio", null=True)
    IVA=models.FloatField(verbose_name="IVA", null=True)
    disponibilidad=models.IntegerField(verbose_name="Disponibilidad", null=True)
    
    def __str__(self):
        fila =self.marca+"/"+self.modelo+"/"+self.año
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

