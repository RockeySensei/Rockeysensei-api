from fastapi import FastAPI, APIRouter
from fastapi.responses import Response
from API.Funcion_Ruta.loop import registrar_rutas_desde_directorio
import json
import os
import uvicorn

app = FastAPI()

# Configuración de rutas
carpeta_api = os.path.join(os.path.dirname(__file__), "API")
router_principal = APIRouter()

registrar_rutas_desde_directorio(router_principal, carpeta_api)
app.include_router(router_principal)

@app.get("/")
def on_router():
    return Response(
        json.dumps({"status": 200, "data": {"message": "welcome API Proyect Comunity"}}, indent=4),
        media_type="application/json",
        status_code=200
    )

# Ejecutar la aplicación en Railway
if __name__ == "__main__":
    port = os.getenv("PORT", "8000")  # Obtiene el puerto de Railway o usa 8000 por defecto
    if not port.isdigit():
        port = 8000  # Si PORT no es un número válido, usa 8000
    else:
        port = int(port)

    uvicorn.run(app, host="0.0.0.0", port=port)
