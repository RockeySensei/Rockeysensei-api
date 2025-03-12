from fastapi import FastAPI, HTTPException, Query, APIRouter
from fastapi.responses import Response
from API.Funcion_Ruta.loop import registrar_rutas_desde_directorio
import json
import os
import uvicorn

app = FastAPI()

# Configuración de rutas
carpeta_api = os.path.join(os.path.dirname(__file__), 'API')
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
    port = int(os.getenv("PORT", 8000))  # Usa 8000 como fallback
    uvicorn.run(app, host="0.0.0.0", port=port)
