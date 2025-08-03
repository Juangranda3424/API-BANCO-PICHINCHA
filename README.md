# Sistema Bancario API - Banco Pichincha

Una API REST completa para operaciones bancarias desarrollada con Flask y PostgreSQL.

## Tecnologías

- **Backend**: Flask (Python)
- **Base de Datos**: PostgreSQL
- **Email**: SMTP con templates HTML
- **Arquitectura**: Patrón Repository/Service/Controller

## Instalación


### 1. Instalar dependencias
```bash
pip install flask
pip install psycopg2-binary
```

### 2. Configurar base de datos
- Configura las credenciales de la base de datos en `src/db/Conn.py`

### 3. Ejecutar la aplicación
```bash
python app.py
```

La aplicación estará disponible en: `http://127.0.0.1:5000`

## Dependencias

Las siguientes librerías deben estar instaladas:

```bash
pip install flask

pip install psycopg2-binary

```
## Endpoints de la API

### Consultas
- `GET /cuenta-info/<numeroCuenta>` - Información de cuenta
- `GET /movimientos-info/<numeroCuenta>` - Historial de movimientos
- `GET /cantidad-cuentas/<id>` - Cuentas de una persona

### Operaciones
- `POST /deposito` - Realizar depósito
- `POST /transferencia` - Realizar transferencia
- `POST /retiro-sin-tarjeta` - Solicitar retiro sin tarjeta

## Formato de Requests

### Depósito
```json
{
    "numeroCuentaOrigen": "string",
    "numeroCuentaDestino": "string", 
    "monto": float,
    "motivo": "string",
    "ubicacion": "string",
    "telefono": "string"
}
```

### Transferencia
```json
{
    "numeroCuentaOrigen": "string",
    "numeroCuentaDestino": "string",
    "monto": float,
    "motivo": "string", 
    "ubicacion": "string",
    "telefono": "string"
}
```

### Retiro sin tarjeta
```json
{
    "numeroCuenta": "string",
    "monto": float,
    "motivo": "string",
    "ubicacion": "string",
    "numeroCelular": "string"
}
```
