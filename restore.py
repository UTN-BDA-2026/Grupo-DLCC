import os
import subprocess
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
BACKUP_DIR = f"./backup_desarrollo/{DB_NAME}"

print(f" Iniciando RESTORE (Plan de Recuperación ante Desastres) en: '{DB_NAME}'...")

comando = f'mongorestore --uri="{MONGO_URI}" --db="{DB_NAME}" --drop "{BACKUP_DIR}"'

try:
    subprocess.run(comando, shell=True, check=True)
    print("\n [RESTAURACIÓN COMPLETADA]")
    print(" Base de datos restablecida al estado consistente del backup.")
except subprocess.CalledProcessError as e:
    print(f"\n Error crítico en el proceso de Restore: {e}")