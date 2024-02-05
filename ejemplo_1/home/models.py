from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

# Create your models here.
class Estado(models.Model):
    #id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from = 'nombre')
    numero = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'estado' #esto es para que la table se llame estado y no Estado
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'


class Genero(models.Model):
    nombre =models.CharField(max_length=100,null=True)

    #esto de aqui abajo no es necesario, pero cesar lo coloco
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'genero' #esto es para que la table se llame estado y no Estado
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'


class Pais(models.Model):
    nombre =models.CharField(max_length=100,null=True)

    #esto de aqui abajo no es necesario, pero cesar lo coloco
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'pais' #esto es para que la table se llame estado y no Estado
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'


class Perfiles(models.Model):
    nombre =models.CharField(max_length=100,null=True)

    #esto de aqui abajo no es necesario, pero cesar lo coloco
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'perfiles' #esto es para que la table se llame estado y no Estado
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'


class Metadata(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    keyword = models.TextField()
    correo = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    titulo = models.CharField(max_length=255)
    #esto de aqui abajo no es necesario, pero cesar lo coloco
    def __str__(self):
        return self.correo
    
    class Meta:
        db_table = 'metadata' #esto es para que la table se llame estado y no Estado
        verbose_name = 'Metadata'
        verbose_name_plural = 'Metadata'


class Categoria(models.Model):
    nombre =models.CharField(max_length=100,null=True)
    slug = AutoSlugField(populate_from = 'nombre')

    #esto de aqui abajo no es necesario, pero cesar lo coloco
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'categoria' #esto es para que la table se llame estado y no Estado
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING)
    nombre = models.CharField(max_length=100,null=True)
    slug = AutoSlugField(populate_from = 'nombre')
    #fecha = models.DateTimeField(auto_now = True)
    hora = models.TimeField(auto_now = True)
    fecha = models.DateField(auto_now = True)
    descripcion = models.TextField()

    #esto de aqui abajo no es necesario, pero cesar lo coloco
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'producto' #esto es para que la table se llame estado y no Estado
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


class UsersMetadata(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    pais = models.ForeignKey(Pais, models.DO_NOTHING)
    genero =  models.ForeignKey(Genero, models.DO_NOTHING)
    correo = models.CharField(max_length = 100, blank = True)
    telefono = models.CharField(max_length = 100, blank = True, null = True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField(default='1980-05-24')

    #esto de aqui abajo no es necesario, pero cesar lo coloco
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    class Meta:
        db_table = 'users_metadata' #esto es para que la table se llame estado y no Estado
        verbose_name = 'User metadata'
        verbose_name_plural = 'Users metadata'