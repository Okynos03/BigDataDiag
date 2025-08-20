from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List, Optional
import mysql.connector

from DAO.employeeDAO import employeeDAO
from DAO.deptoDAO import deptoDAO
from models import *

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin123.",
    database="employeesdb",
    port="3308"
)

eDAO = employeeDAO()
dDAO = deptoDAO()
empleados = []
departamentos = []
vigentes = []
salarios = []
managers = []
top_pagados = []

app = FastAPI(title="Reportes Empleados")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# @app.get("/", response_class=HTMLResponse)
# async def index():
#     return FileResponse("static/index.html", media_type="text/html")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    empleados = []
    departamentos = []
    rows = eDAO.get_all_employees(conexion)
    for row in rows:
        empleados.append({
            "num_empleado": row["emp_no"],
            "nombre": row["first_name"],
            "apellidos": row["last_name"],
            "genero": row["gender"],
            "fecha_contrato": row["hire_date"]
        })

    rows = dDAO.get_all_depts(conexion)
    for row in rows:
        departamentos.append({
            "id": row["dept_no"],
            "nombre": row["dept_name"]
        })

    vigentes = []
    salarios = []
    managers = []
    top_pagados = []

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "empleados": empleados,
            "departamentos": departamentos,
            "vigentes": vigentes,
            "salarios": salarios,
            "managers": managers,
            "top_pagados": top_pagados,
            "dept_id": None
        }
    )

#///////////////////////////////////////////////////////////////
@app.get("/pordept", response_class=HTMLResponse)
async def index(request: Request, dept_id: Optional[str] = 0):
    vigentes = []
    rows = dDAO.get_employees_by_dept(conexion, dept_id)
    for row in rows:
        vigentes.append({
            "num_empleado": row["emp_no"],
            "nombre_completo": row["full_name"],
            "departamento": row["dept_name"]
        })

    empleados = []
    departamentos = []
    salarios = []
    managers = []
    top_pagados = []
    rows = eDAO.get_all_employees(conexion)
    for row in rows:
        empleados.append({
            "num_empleado": row["emp_no"],
            "nombre": row["first_name"],
            "apellidos": row["last_name"],
            "genero": row["gender"],
            "fecha_contrato": row["hire_date"]
        })

    rows = dDAO.get_all_depts(conexion)
    for row in rows:
        departamentos.append({
            "id": row["dept_no"],
            "nombre": row["dept_name"]
        })

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "empleados": empleados,
            "departamentos": departamentos,
            "vigentes": vigentes,
            "salarios": salarios,
            "managers": managers,
            "top_pagados": top_pagados,
            "dept_id": None
        }
    )

@app.get("/salarios", response_class=HTMLResponse)
async def index(request: Request):
    salarios = []
    rows = eDAO.get_current_n_salary(conexion)
    for row in rows:
        salarios.append({
            "num_empleado": row["emp_no"],
            "nombre_completo": row["full_name"],
            "salario": row["salary"]
        })

    empleados = []
    departamentos = []
    vigentes = []
    managers = []
    top_pagados = []

    rows = eDAO.get_all_employees(conexion)
    for row in rows:
        empleados.append({
            "num_empleado": row["emp_no"],
            "nombre": row["first_name"],
            "apellidos": row["last_name"],
            "genero": row["gender"],
            "fecha_contrato": row["hire_date"]
        })

    rows = dDAO.get_all_depts(conexion)
    for row in rows:
        departamentos.append({
            "id": row["dept_no"],
            "nombre": row["dept_name"]
        })

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "empleados": empleados,
            "departamentos": departamentos,
            "vigentes": vigentes,
            "salarios": salarios,
            "managers": managers,
            "top_pagados": top_pagados,
            "dept_id": None
        }
    )

@app.get("/managers", response_class=HTMLResponse)
async def index(request: Request):
    managers = []
    rows = dDAO.get_managers(conexion)
    for row in rows:
        managers.append({
            "departamento": row["dept_name"],
            "nombre_completo": row["full_name"],
            "fecha_inicio": row["from_date"]
        })

    empleados = []
    departamentos = []
    vigentes = []
    salarios = []
    top_pagados = []

    rows = eDAO.get_all_employees(conexion)
    for row in rows:
        empleados.append({
            "num_empleado": row["emp_no"],
            "nombre": row["first_name"],
            "apellidos": row["last_name"],
            "genero": row["gender"],
            "fecha_contrato": row["hire_date"]
        })

    rows = dDAO.get_all_depts(conexion)
    for row in rows:
        departamentos.append({
            "id": row["dept_no"],
            "nombre": row["dept_name"]
        })

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "empleados": empleados,
            "departamentos": departamentos,
            "vigentes": vigentes,
            "salarios": salarios,
            "managers": managers,
            "top_pagados": top_pagados,
            "dept_id": None
        }
    )

@app.get("/highest", response_class=HTMLResponse)
async def index(request: Request):
    top_pagados = []
    rows = dDAO.highest_payed(conexion)
    for row in rows:
        top_pagados.append({
            "departamento": row["dept_name"],
            "num_empleado": row["emp_no"],
            "nombre_completo": row["full_name"],
            "salario": row["salary"]
        })

    empleados = []
    departamentos = []
    vigentes = []
    salarios = []
    managers = []

    rows = eDAO.get_all_employees(conexion)
    for row in rows:
        empleados.append({
            "num_empleado": row["emp_no"],
            "nombre": row["first_name"],
            "apellidos": row["last_name"],
            "genero": row["gender"],
            "fecha_contrato": row["hire_date"]
        })

    rows = dDAO.get_all_depts(conexion)
    for row in rows:
        departamentos.append({
            "id": row["dept_no"],
            "nombre": row["dept_name"]
        })

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "empleados": empleados,
            "departamentos": departamentos,
            "vigentes": vigentes,
            "salarios": salarios,
            "managers": managers,
            "top_pagados": top_pagados,
            "dept_id": None
        }
    )