from fastapi import FastAPI, HTTPException

from typing import Optional

app = FastAPI()

lista_empleados = [
    {
        'id':'1',
        'nombre':'Sergio Valencia',
        'puesto':'Full-Stack Developer JR'
    },
    {   
        'id':'2',
        'nombre':'Hever Rubio',
        'puesto':'Full-Stack Developer JR'
    }
]

@app.get("/")
def read_root():
    return {'Hello':'World'}

@app.get("/items/{item_id}")
def read_item(item_id:int, q:Optional[str] = None, tab:Optional[str] = None):
    return {'item_id': item_id, 'query': q, 'tab': tab}

@app.get("/empleados")
def read_empleados(empid:Optional[int] = None):
    try:
        if empid <= 0:
            empid = 0
        else:
            empid = empid - 1
        empleado = lista_empleados[empid]
    except:
        raise HTTPException(status_code=404, detail='Item not found')
    print(empleado)
    return empleado