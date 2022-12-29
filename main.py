from fastapi import FastAPI
import uvicorn
from api.v1 import service


app = FastAPI()
app.include_router(service.router, prefix='/api/v1')

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080)