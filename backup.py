import os
import subprocess
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
OUTPUT_DIR = "./backup´_desarrollo"

print(f"Iniciando backup completo para la DB: '{DB_NAME}'...")

comando = f'mongodump --uri="{MONGO_URI}" --db="{DB_NAME}" --out="{OUTPUT_DIR}"'

try:
    subprocess.run(comando, shell=True, check=True)
    print("\n [BACKUP EXITOSO]")
    print(f"Respaldo fisico consolidado en {OUTPUT_DIR}")
except subprocess.CalledProcessError as e:
     print(f"\n Fallo en la consistencia del backup: {e}")