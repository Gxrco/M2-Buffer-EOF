# Procesamiento de Buffer Simulado
Esta implementación permite dividir y procesar grandes entradas en partes más pequeñas (buffers), lo que es útil cuando se maneja texto extenso o flujos de datos continuos, evitando cargar todo en memoria a la vez. Las configuraciones del buffer y de la entrada se realizan de forma personalizada.

## Funcionamiento
- **Carga de Buffer (cargar_buffer):**
Extrae un segmento del tamaño especificado (tamano_buffer) desde la entrada (entrada), comenzando en el índice dado (inicio).
Si el buffer cargado no tiene suficiente longitud (es menor que tamano_buffer), se añade un marcador especial "eof" para indicar el final del flujo.
- **Procesamiento del Buffer (procesar_buffer):**
Recorre el buffer carácter por carácter, construyendo lexemas (unidades de texto) en función de los espacios.
Si encuentra un espacio (" "), considera que un lexema ha terminado, lo agrega a la lista de lexemas y limpia el acumulador temporal (temp).
Si encuentra "eof", detiene el procesamiento y añade cualquier contenido residual en temp como un último lexema.
- **Bucle Principal:**
Se recorre toda la entrada en segmentos de tamaño definido (tamano_buffer).
En cada iteración, el buffer cargado se procesa para extraer y mostrar los lexemas generados.

### Consideración
> Las cadenas aceptadas para el procesado del buffer se consideran token todas aquellas palabras separadas por " " (espacios), generalmente se pensaría hacer uso de expresiones regulares para analizar cadenas en un contexto real.
