from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

app = FastAPI(title="Reportes Empleados")
app.mount("/static", StaticFiles(directory="static"), name="static")

class EmpleadoBasico(BaseModel):
    num_empleado: int
    nombre: str
    apellidos: str
    genero: str
    fecha_contrato: date

class EmpleadoVigenteDepto(BaseModel):
    num_empleado: int
    nombre_completo: str
    departamento: str
    salario: float

class SalarioActual(BaseModel):
    num_empleado: int
    nombre_completo: str
    salario: float

class ManagerDepto(BaseModel):
    departamento: str
    nombre: str
    apellidos: str
    fecha_inicio: date

class TopPagadoDepto(BaseModel):
    departamento: str
    num_empleado: int
    nombre_completo: str
    salario: float

class Departamento(BaseModel):
    id: int
    nombre: str

@app.get("/", response_class=HTMLResponse)
async def index():
    return FileResponse("static/index.html", media_type="text/html")

#///////////////////////////////////////////////////////////////

@app.get("/api/empleados", response_model=List[EmpleadoBasico])
def listar_empleados():
    #rows = repo_listar_empleados()  # ← devuelve List[dict]
    #return [EmpleadoBasico(**r) for r in rows]
    return []

@app.get("/api/departamentos", response_model=List[Departamento])
def listar_departamentos():
    return []

@app.get("/api/empleados/por-departamento", response_model=List[EmpleadoVigenteDepto])
def empleados_por_departamento(
    dept_id: Optional[int] = None,
    dept_nombre: Optional[str] = None
):
    return []

@app.get("/api/salarios/actuales", response_model=List[SalarioActual])
def salarios_actuales():
    return []

@app.get("/api/departamentos/manager", response_model=List[ManagerDepto])
def managers_actuales():
    return []

@app.get("/api/departamentos/pago-alto", response_model=List[TopPagadoDepto])
def top_pagado_por_departamento():
    return []
