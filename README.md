
# API de votaciones

Prueba tecnica para New Inntech


## Requerimientos

- Se debe de tener instalado python, preferiblemente en la version >=3.9
- Como gestor de base de datos, se utiliza postgreSQL

## Ejecución

Para ejecutar el proyecto se debe de seguir los siguientes pasos

- Clonar el repositorio de forma local
- Crear un entorno virtual en python utilizando el siguiente comando:

```bash
  python -m venv venv
```
- Activar el entorno virtual creado utilizando este comando:
```bash
  source venv/bin/activate # En Windows: venv\Scripts\activate
```
- Instalar las dependencias con el siguiente comando:
```bash
  pip install -r requirements.txt
```
- Crear la base de datos e inicializar la base de datos en el gestor de postgreSQL (pgAdmin 4), utilizar el init.sql
- Cambiar los datos de las variables dentro del archivo app/database.py para la correcta conexion a la base de datos:
```bash
  DB_USER = "usuario" # postgres
  DB_PASSWORD = "contraseña"
  DB_HOST = "host" # localhost
  DB_PORT = "puerto" # 5432
  DB_NAME = "database" # votaciones
```

- Por ultimo. Ejecutar el proyecto
```bash
  uvicorn app.main:app
  # Si se desean visualizar los cambios que se hacen, agregar --realod
  # uvicorn app.main:app --reload
```

## Documentacion de la API

Para acceder a la documentacion de la API, se debe de ingresar a la ruta /docs.
Esta ruta mostrará toda la documentacion con Swagger, y se podrán hacer pruebas desde la misma.


    