from django.db import models

# Modelo de Usuarios
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    contrasena = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo de Viviendas
class Vivienda(models.Model):
    direccion = models.CharField(max_length=255)
    propietario = models.CharField(max_length=100)
    numero_habitantes = models.IntegerField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.direccion

# Modelo de Cuotas
class Cuota(models.Model):
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE)
    fecha = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50, default='pendiente')

    def __str__(self):
        return f'Cuota de {self.vivienda} - {self.fecha}'

# Modelo de Pagos
class Pago(models.Model):
    cuota = models.ForeignKey(Cuota, on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Pago de {self.monto_pagado} para cuota {self.cuota}'

# Modelo de Morosidades (Opcional)
class Morosidad(models.Model):
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE)
    meses_pendientes = models.IntegerField()
    total_deuda = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_actualizacion = models.DateField()

    def __str__(self):
        return f'Morosidad de {self.vivienda}'

# Modelo de Informes
class Informe(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateField()
    tipo_informe = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return f'Informe {self.tipo_informe} generado por {self.usuario}'
