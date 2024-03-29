### Requisitos previos

Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

### Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/mrgomezsv/Platzi_Curso_de_Flask.git
   cd Platzi_Curso_de_Flask
   ```
2. Crea y activa un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
      ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Asignación de la variable de ejecución del proyecto:

   ```bash
   $env:FLASK_APP = "main.py"
   ```
### Ejecución

   Ejecución

   Podemos activar el modo Debug para ver los cambios en tiempo real.
   Aplica para Windows:

      $env:FLASK_DEBUG = 1

   Ejecuta la aplicación con el siguiente comando:

      flask run

   Ejecuta los test con el siguiente comando:

      flask test

   La aplicación estará disponible en http://127.0.0.1:5000. En tu navegador


### Comandos de GCP (Google Cloud Platform)

   Listar los proyectos

      gcloud config list

   Seleccionar un proyecto en concreto

      gcloud config set project platzi-flask-mrgomez

   Login de usuario de Google

      gcloud auth login    

   Elegir la aplicación por default de nuestro proyecto, con este comando vamos a poder correr desde nuestro servidor local y comunicarnos con nuestra db

      gcloud auth application-default login 


# ¡Gracias por tu interés en este proyecto!

## Att: Mario Roberto
### mrgomez.dev@outlook.com