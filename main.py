from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def read_root():
    return JSONResponse(content={"message": "Hello from Vercel"})

# Обработчик для Vercel
async def handler(request):
    return await app(request.scope, request.receive, request.send)