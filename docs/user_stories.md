# User Stories: Proceso de Traslados de Salida

## Introducción
Este documento describe las User Stories relacionadas con el proceso de "traslados de salida", que incluye los archivos `S2.txt`, `R2.txt`, `S4.txt`, `R4.txt` y sus variantes automáticas. Estas historias se basan en el cumplimiento de la Resolución 762 de 2023 y en procesos internos de validación en la EPS.

## Historias de Usuario

### Historia 1: Cargar Archivos de Entrada
**Como** operador de la EPS,  
**quiero** cargar los archivos generados por ADRES (`S2.txt`, `R2.txt`, etc.),  
**para** validar su contenido y procesarlos según las normativas.

---

### Historia 2: Validar Información con Bases de Datos Internas
**Como** operador de la EPS,  
**quiero** validar los datos de los archivos contra nuestras bases internas (`Excel`),  
**para** automatizar la aprobación de traslados con base en criterios definidos.

---

### Historia 3: Generar Archivos de Salida
**Como** operador de la EPS,  
**quiero** generar los archivos `S4.txt` y `R4.txt` con causales de aprobación o negación,  
**para** enviarlos a ADRES y cumplir con los requisitos normativos.

---

### Historia 4: Reportar Resultados
**Como** analista de la EPS,  
**quiero** generar reportes consolidados en formatos `.xlsx` y `.txt`,  
**para** analizar los resultados y documentar las decisiones.

---

### Próximos Pasos
1. Revisar y ajustar estas historias en base a necesidades específicas.
2. Expandir las User Stories para cubrir otros procesos (novedades, ingresos nuevos).
3. Implementar las funcionalidades correspondientes y enlazar cada historia con un módulo del proyecto.

# Borrador de la User Stories

La idea es crear un ejecutable portable que permita hacer los diferentes reportes a la ADRES, dichos reportes ya estan estructurados en la Resolución 762 de 2023, desde el nombre de los archivos, hasta el numero de caracteres por columna el regimen y los campos por archivo y/o proceso. son 3 grandes procesos.
1. movilidades y traslados: donde se reportan cambios de regimen y de EPS, que inician con los archivos S1 y R1 de esos archivos se desglosan los S1.val, S1automatico, S2, R2, S2automatico, R2automatico, S2, R4, S4.val, R4.val, S4.neg, R4.neg S3, R3, S5, R5, S6 y R6.
Los archivos S hacen referencia al regimen subsidiado y los archivos R hacen referencia al regimen contributivo, hay archivos entre regimen que comparten estructura y en otros no.
2. Novedades: Donde se reportan actualización de datos, desde cambios de nombres hasta cambios de municipio de residencia. Estos archivos son NS.txt, NC.txt, NS.val, NC.val, NS.neg y NC.neg el S de subsidiado y el C de contributivo.
3. Ingresos nuevos: Es donde se reportan los usuarios que se afilan por primera vez al sistema de salud colombiano usualmente, recién nacidos o extranjeros. 

Para este primer proceso identifique un subproceso pequeño y fácil de gestionar que lo llamare para facilidad de uso “proceso de traslados de salida” estos comprenden los archivos S2.txt, R2.txt, S2automaticos.txt, R2automaticos.txt R4.txt, S4.txt, S4.neg y R4.neg estos archivos los podemos agrupar de 2 manera: 
1. Los archivos que genera ADRES: S2.txt, R2.txt, S2automaticos.txt, R2automaticos.txt, S4.neg y R4.neg Estos archivos los entrega adres después de validar los S1.txt y R1.txt que nosotros como EPS entregamos y después de validar los R2.txt y los S2.txt que nosotros generamos.
2. Los archivos que nosotros generamos: son solo 4 R4.txt, S4.txt uno por cada régimen subsidiado y contributivo, los archivos S4.txt se derivan de los archivos S2.txt que entrega ADRES y estos hacen referencia a traslados que otras EPS del régimen subsidiado están solicitando a nosotros y lo mismo para el régimen contributivo con los archivos R. 

Ahora bien, como se genera el S4 y R4 los archivos S2 y R2 contienen los datos de los usuarios que nos están solicitando otras EPS en una columna determinada nosotros damos la aprobación o negación y en otra el motivo de este, todo con numero ejemplo de aprobación es un 1 y de negación es un 0 las causales de aprobación y negación también son números. Para determinar si se aprueba o se niega el traslado lo realizamos de 2 maneras una según la resolución 762 del 2023 que contiene las causales de aprobación y negación y la otra es validando bases de datos en Excel, estas bases de datos nos indican si los usuarios se comunicaron con nosotros solicitando la aprobación de traslado, si demandaron a la EPS, presentaron PQR u otro proceso que de manera interna la EPS considere valido para aprobar el traslado, se cruza tipo y numero de documento para extraer estos datos de los exceles, usualmente se manejan 3 a 4 exceles para esta validación, si los usuarios aparecen en estos exceles se apruba el traslado de manera automática de lo contrario se niegan. Para aprobar traslados acorde a la norma se valida solo los S2, R2 y los archivos maestros de la EPS para verificar las causales de aprovación o negación se clasifican y se asigna cada valor según las condiciones que se presenten en la validación o cruce de información, 
Con este proceso se termina Generando el S4 y R4 con la información del S2 y R2 pero con la aprovación o negación con sus causales para cada registro.
