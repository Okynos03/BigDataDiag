from pydantic import BaseModel
from datetime import date

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
    nombre_completo: str
    fecha_inicio: date

class TopPagadoDepto(BaseModel):
    departamento: str
    num_empleado: int
    nombre_completo: str
    salario: float

class Departamento(BaseModel):
    id: int
    nombre: str