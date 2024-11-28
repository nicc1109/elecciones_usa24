from dotenv import load_dotenv
import os
import sys

def configurar_entorno():
    """
    Carga el archivo .env y agrega el path del proyecto al sys.path
    """
    # Cargar variables del archivo .env
    load_dotenv()

    # Agregar el path del proyecto al sys.path
    project_root = os.getenv("PROJECT_ROOT")
    if project_root and project_root not in sys.path:
        sys.path.append(project_root)

    # Verificar que el path se agregó correctamente
    print(f"Path del proyecto cargado: {project_root}")
