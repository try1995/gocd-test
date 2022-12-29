from fastapi import Request, APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from predict.v1.inference import inference, load_model
from pydantic import BaseModel
from typing import Union
import requests

class Item(BaseModel):
    title:Union[str, None] = None
    content: Union[str, None] = None

router = APIRouter()
load_model()

@router.post('/predict')
async def predict_service(item:Item):
    """
    @description 预测服务
    Returns:
    """
    prediction = inference(item)
    json_compatible_item_data = jsonable_encoder(prediction)
    return JSONResponse(content=json_compatible_item_data)


@router.get('/health')
async def predict_service(request: Request):
    json_compatible_item_data = jsonable_encoder({'status': 0})
    return JSONResponse(content=json_compatible_item_data)

from typing import Union

from fastapi import FastAPI, Path, Query

@router.get("/asr/")
async def read_items(rate : int = 0
):
    results = {"rate": rate}
    return results
