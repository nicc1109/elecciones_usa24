# === Configuración de Rutas ===
import os
import sys

# Agregar la raíz del proyecto al sys.path
project_root = os.path.abspath("..")  # Ajusta si el notebook está en otra carpeta
if project_root not in sys.path:
    sys.path.append(project_root)

# === Configuración del Entorno ===
from src import configurar_entorno
from dotenv import load_dotenv

# Configurar entorno y cargar variables del archivo .env
configurar_entorno()
load_dotenv()

print("Entorno configurado y variables de entorno cargadas.")

# === Librerías Estándar ===
from datetime import datetime

# === Librerías para Análisis de Datos ===
import pandas as pd
import numpy as np

# === Librerías para Visualización ===
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de visualizaciones
sns.set(style="whitegrid", palette="pastel")
plt.rcParams['figure.figsize'] = (10, 6)

print("Librerías importadas y configuradas correctamente.")