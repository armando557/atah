from django.contrib import admin
from django.utils.html import format_html
from .models import Registro

@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):

    list_display = (
        'nombre',
        'edad',
        'telefono',
        'ciudad',
        'genero',
        'antiguedad',
        'estado',
        'mostrar_licencia'
    )

    search_fields = (
        'nombre',
        'telefono',
        'ciudad'
    )

    list_filter = (
        'estado',
        'genero',
        'ciudad'
    )

    list_editable = (
        'estado',
    )

    list_per_page = 10

    fieldsets = (
        ('Información Personal', {
            'fields': (
                'nombre',
                'edad',
                'telefono',
                'ciudad',
                'genero'
            )
        }),

        ('Información Laboral', {
            'fields': (
                'antiguedad',
                'documentos_vigentes',
                'estado'
            )
        }),

        ('Licencia Federal', {
            'fields': (
                'licencia_federal',
            )
        }),
    )

    def mostrar_licencia(self, obj):

        if obj.licencia_federal:
            return format_html(
                '<img src=\"{}\" width=\"150\" height=\"100\" style=\"border-radius:10px; object-fit:cover;\" />',
                obj.licencia_federal.url
            )

        return "Sin imagen"

    mostrar_licencia.short_description = "Licencia"

    def estado_color(self, obj):

        if obj.estado == 'Aceptado':
            color = 'green'

        elif obj.estado == 'Rechazado':
            color = 'red'

        else:
            color = 'orange'

        return format_html(
            '<strong style=\"color:{}\">{}</strong>',
            color,
            obj.estado
        )

    estado_color.short_description = "Estado"