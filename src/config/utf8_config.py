# -*- coding: utf-8 -*-
"""
Configuración global para UTF-8 en toda la aplicación
"""
import sys
import os

# Configurar el encoding por defecto del sistema a UTF-8
if sys.version_info[0] >= 3:
    # Python 3
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    
# Asegurar que stdout y stderr usen UTF-8
def configure_utf8():
    """Configura UTF-8 para toda la aplicación"""
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    
    # Variables de entorno para PostgreSQL
    os.environ['PGCLIENTENCODING'] = 'UTF8'
    os.environ['LC_ALL'] = 'es_ES.UTF-8'
    os.environ['LANG'] = 'es_ES.UTF-8'

# Ejecutar configuración al importar
configure_utf8()
