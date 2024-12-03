import os

def generate_structure(directory, output_file, ignore_list=None):
    """
    Genera la estructura del directorio en un archivo de salida, excluyendo carpetas y archivos irrelevantes.

    Args:
        directory (str): Directorio base del proyecto.
        output_file (str): Ruta del archivo donde se guardará la estructura.
        ignore_list (list): Lista de carpetas o archivos a ignorar.
    """
    if ignore_list is None:
        ignore_list = ['.git', '__pycache__', '*.pyc', '*.pyo', '*.log', '.DS_Store', 'Thumbs.db', 'env', '.venv']

    def should_ignore(name):
        """Verifica si un archivo o carpeta debe ser ignorado."""
        return any(ignore in name for ignore in ignore_list)

    with open(output_file, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(directory):
            # Excluir carpetas irrelevantes
            dirs[:] = [d for d in dirs if not should_ignore(d)]
            
            level = root.replace(directory, '').count(os.sep)
            indent = '    ' * level
            f.write(f"{indent}├── {os.path.basename(root)}\n")
            
            subindent = '    ' * (level + 1)
            for file in files:
                # Excluir archivos irrelevantes
                if not should_ignore(file):
                    f.write(f"{subindent}└── {file}\n")

if __name__ == "__main__":
    # Directorio base del proyecto
    base_directory = os.getcwd()
    # Archivo de salida
    output_path = os.path.join(base_directory, 'docs', 'project_structure.md')

    # Generar estructura
    generate_structure(base_directory, output_path)
    print(f"Estructura del proyecto generada en: {output_path}")
