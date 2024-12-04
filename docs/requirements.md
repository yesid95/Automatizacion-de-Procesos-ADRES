# Requisitos y Funcionalidades Principales

## Funcionalidades del Proyecto

### Funciones Principales del Proceso "Traslados de Salida"
1. **Procesamiento de Archivos**:
   - Leer y procesar archivos generados por ADRES: `S2.txt`y `R2.txt`
   - Validar estructura, formato y contenido de los archivos, según la Resolución 762 de 2023.
   - Incorporar aprobaciones o negaciones con causales basadas en reglas normativas y validaciones internas.
   - Generar archivos `S4.txt` y `R4.txt` como resultado para el reporte a ADRES y un informe del proceso en EXCEL con una tabla resumen de la cantidad de usuarios solicitados, aprobados, negados.

2. **Automatización de Flujos**:
   - Clasificación automática de usuarios en "aprobados" o "negados" basada en:
     - Bases de datos internas (`Excel`).
     - Reglas de negocio definidas en la a Resolución 762 de 2023.

3. **Generación de Reportes**:
   - Exportar archivos `S4.txt` y `R4.txt` con los resultados procesados y `xlsx` con el resumen del proceso.
   - Incluir causales específicas para cada usuario procesado.

---

### Funciones Futuras (En Planeación)
El sistema está diseñado para ser escalable y permitirá la inclusión de nuevos procesos relacionados. Funciones planeadas:

1. **Generación de Archivos S1 y R1**:
   - Crear archivos iniciales de traslados y movilidades.
   - Validar datos antes de enviarlos a ADRES.

2. **Gestión de Novedades**:
   - Procesar archivos `NS.txt`, `NC.txt`, y sus validaciones (`NS.val`, `NC.val`).
   - Reportar actualizaciones de datos, como cambios de nombre o municipio.

3. **Gestión de Ingresos Nuevos**:
   - Automatizar el reporte de usuarios que ingresan al sistema por primera vez.

---

## Requisitos No Funcionales

1. **Escalabilidad**:
   - Soportar un gran volumen de datos sin degradación significativa del rendimiento.

2. **Portabilidad**:
   - Ejecutable portable compatible con Windows.

3. **Mantenibilidad**:
   - Código modular y bien documentado.
   - Pruebas unitarias para todas las funcionalidades principales.

---

### Próximos Pasos
1. Diseñar e implementar las funciones principales para el "proceso de traslados de salida".
2. Validar el flujo de aprobación y negación de traslados basado en:
   - Resolución 762 de 2023.
   - Bases de datos internas (`Excel`).
3. Generar y exportar los archivos `S4.txt` y `R4.txt`.
4. Planificar la integración de los otros procesos (S1, R1, Novedades, Ingresos Nuevos).

# Crear una Lista de Tareas
- GitHub Issues/Projects
- Plantillas de Casos de Uso: Usa diagramas UML para representar el flujo de interacciones.
- User Stories (Historias de Usuario): Describe las funcionalidades desde el punto de vista del usuario.
