from django.db import models

class Registro(models.Model):

    GENEROS = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
    ]

    ESTADOS = [
        ('Revision', 'En revisión'),
        ('Aceptado', 'Aceptado'),
        ('Rechazado', 'Rechazado'),
    ]

    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=15)
    ciudad = models.CharField(max_length=100)

    antiguedad = models.IntegerField()

    genero = models.CharField(
        max_length=20,
        choices=GENEROS
    )

    licencia_federal = models.ImageField(
        upload_to='licencias/'
    )

    documentos_vigentes = models.BooleanField(default=True)

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='Revision'
    )

    # NUEVOS CAMPOS

    alias = models.CharField(max_length=100, blank=True)

    fecha_nacimiento = models.DateField(null=True, blank=True)

    lugar_nacimiento = models.CharField(max_length=200, blank=True)

    rfc = models.CharField(max_length=20, blank=True)

    curp = models.CharField(max_length=30, blank=True)

    domicilio = models.TextField(blank=True)

    cp = models.CharField(max_length=10, blank=True)

    colonia = models.CharField(max_length=100, blank=True)

    poblacion = models.CharField(max_length=100, blank=True)

    contacto_emergencia = models.CharField(max_length=100, blank=True)

    socio = models.CharField(max_length=100, blank=True)

    modalidad = models.CharField(max_length=100, blank=True)

    categoria = models.CharField(max_length=100, blank=True)

    unidad = models.CharField(max_length=100, blank=True)

    rol = models.CharField(max_length=100, blank=True)

    fecha_ingreso = models.DateField(null=True, blank=True)

    fecha_baja = models.DateField(null=True, blank=True)

    reingreso = models.DateField(null=True, blank=True)

    contrato = models.CharField(max_length=100, blank=True)

    licencia = models.CharField(max_length=100, blank=True)

    vigencia_licencia = models.DateField(null=True, blank=True)

    psicofisico = models.CharField(max_length=100, blank=True)

    numero_exp_medico = models.CharField(max_length=100, blank=True)

    antiguedad_licencia = models.CharField(max_length=100, blank=True)

    asegurado = models.BooleanField(default=False)

    afiliacion = models.CharField(max_length=100, blank=True)

    a_imss = models.CharField(max_length=100, blank=True)

    b_imss = models.CharField(max_length=100, blank=True)

    empresa = models.CharField(max_length=100, blank=True)

    curso = models.CharField(max_length=100, blank=True)

    movimiento = models.BooleanField(default=False)

    gafet = models.BooleanField(default=False)

    sindicato = models.BooleanField(default=False)

    observaciones = models.TextField(blank=True)

    def __str__(self):
        return self.nombre