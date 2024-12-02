
# Automatización de Procesos ADRES

## Descripción

Este proyecto tiene como objetivo desarrollar una herramienta ejecutable y portable en Python que automatice el procesamiento y gestión de los archivos de novedades requeridos por la Administradora de los Recursos del Sistema General de Seguridad Social en Salud (ADRES) en Colombia. La herramienta facilitará la selección y validación de archivos en formatos `.txt`, `.val`, `.neg` y `.xlsx`, estandarizados según la Resolución 762 de 2023, optimizando el flujo de trabajo y reduciendo errores manuales.

## Funcionalidades

- **Selección de Archivos**: Permite al usuario elegir archivos en formatos `.txt`, `.val`, `.neg` y `.xlsx` correspondientes a los procesos de novedades de la ADRES y archivos de validación internos a la EPS.
- **Validación de Datos**: Verifica la integridad y consistencia de los datos según las especificaciones técnicas establecidas por la ADRES.
- **Procesamiento Automatizado**: Gestiona automáticamente los diferentes tipos de archivos de novedades:
  - **Movilidades y Traslados**: Procesa archivos `R1`, `S1`, `R2`, `S2`, `R4`, `S4`, incluyendo sus variantes automáticas y archivos de glosas.
  - **Ingresos Nuevos**: Maneja archivos `MS` y `MC` para registros nuevos.
  - **Novedades de Actualización**: Administra archivos `NS` y `NC` para cambios de nombre, evolución de documento, cambio de municipio, entre otros.
- **Generación de Reportes**: Produce reportes detallados de los resultados del procesamiento, indicando aprobaciones, negaciones y glosas para corrección.

## Requisitos

- **Python 3.8 o superior**: Lenguaje de programación principal.
- **Librerías**:
  - `pandas`: Para manipulación y análisis de datos.
  - `openpyxl`: Para manejo de archivos Excel (`.xlsx`).
  - `pyinstaller`: Para la creación del ejecutable portable.
- **Sistema Operativo**: Compatible con Windows, macOS y Linux.

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/Automatizacion-de-Procesos-ADRES.git
   cd Automatizacion-de-Procesos-ADRES
   ```
2. **Crear un entorno virtual**:
   ```bash
   python -m venv env
   ```
3. **Activar el entorno virtual**:
   - En Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source env/bin/activate
     ```
4. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. **Ejecutar la herramienta**:
   ```bash
   python src/main.py
   ```
2. **Seleccionar los archivos a procesar**: Utilice la interfaz para elegir los archivos en formato `.txt`, `.val`, `.neg` y `.xlsx`.
3. **Iniciar el procesamiento**: La herramienta validará y procesará los archivos seleccionados, generando los reportes correspondientes en la carpeta `output`.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, siga los siguientes pasos:

1. **Crear una rama para su función o corrección**:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
2. **Realizar los cambios y confirmar los commits**:
   ```bash
   git commit -m "feat: descripción de la nueva funcionalidad"
   ```
3. **Enviar los cambios al repositorio remoto**:
   ```bash
   git push origin feature/nueva-funcionalidad
   ```
4. **Crear una Pull Request**: Desde GitHub, solicite la revisión y fusión de sus cambios.

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).

## Contacto

Para más información, puede visitar el repositorio o contactar a [Osmar Yesid Rincón Zorro](mailto:rincon3259@gmail.com).
