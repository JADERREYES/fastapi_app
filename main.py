"""Aplicación FastAPI de ejemplo con rutas básicas."""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    """Ruta principal que da un saludo básico."""
    return {"mensaje": "¡Hola desde FastAPI!"}

@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    """Devuelve un saludo personalizado."""
    return {"saludo": f"Hola, {nombre}!"}

@app.post("/enviar/{dato}")
def recibir_dato(dato: str):
    """Recibe un dato desde la URL y lo devuelve."""
    return {"respuesta": f"Me has enviado: {dato}"}

class Persona(BaseModel):
    """Modelo de datos para registrar una persona."""
    nombre: str
    cedula: str

@app.post("/registrar")
def registrar_persona(persona: Persona):
    """Registra una persona con nombre y cédula."""
    return {
        "nombre_recibido": persona.nombre,
        "cedula_recibida": persona.cedula
    }
