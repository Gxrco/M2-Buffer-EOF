def cargar_buffer(entrada, inicio, tamano_buffer):
  buffer = entrada[inicio:inicio + tamano_buffer]
  if len(buffer) < tamano_buffer:
    buffer.append("eof")
  return buffer

def procesar_buffer(buffer):
    temp = []
    i = 0
    while i <= len(buffer):
        if buffer[i] == " ":
            print(f'Lexema procesado: {"".join(temp)}')
            buffer.pop(i)
            temp.clear()
        elif buffer[i] == "eof":
            print(f'Lexema procesado: {"".join(temp)}')
            break
        temp.append(buffer.pop(i))
       

entrada = list("Esto es un ejemplo de entrada con varios lexemas")
inicio = 0
tamano_buffer = 10
buffer = cargar_buffer(entrada, inicio, tamano_buffer)
procesar_buffer(buffer)