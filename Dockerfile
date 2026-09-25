# Usar una imagen oficial de Python ligera
FROM python:3.10-slim

# Evitar que Python genere archivos .pyc y forzar la salida en consola
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias del sistema necesarias para compilar conectores de base de datos (como MySQL)
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copiar el archivo de requerimientos y las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código del proyecto
COPY . .

# Exponer el puerto en el que corre Flask
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "run.py"]