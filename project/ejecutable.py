from cx_Freeze import setup, Executable

target = Executable(
    script="chessGUI.py",
    base="Win32GUI",
    icon="chess.ico"
    )

setup(
    name="Chess Master",
    version="1.0",
    description="A single player chess",
    author="Marco Aurelio Gamboa Naranjo",
    executables=[target]
    )

'''  1. Este archivo le he llamado ejecutable.py. Llámale como quieras
     2. Sustituye en Executable el nombre del archivo py o pyw  por el que quieres convertir a exe.
     3. Abre la línea de comandos en Windows, sitúate en el directorio donde tengas el archivo ejecutable.py y el archivo a convertir en exe y escribe
    la siguiente línea de comando:
                                                             py ejecutable.py build.
    4.Esto te creará una carpeta build que contiene el ejecutable y todos los archivos necesarios
    NOTA: Recuerda que debes tener instalado cx_freeze. Lo puedes hacer desde la línea de comandos con:
                                                                                  pip install cx_Freeze

    '''
    
