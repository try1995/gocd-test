from statistics import mode
import sys
from loguru import logger
from config import *

# 日志配置，移除句柄
logger.remove()
logger.add(sys.stderr, level=log_level)

model = None
model_loaded = False

# 加载模型
@logger.catch
def load_model():
    global model, model_loaded
    if model_loaded:
        return model
    logger.info("加载模型...")
    # TODO
    logger.info("加载模型完成")
    model_loaded = True
    return model

# 运行推理
@logger.catch
def inference(item):
    logger.info("运行推理...")
    prediction = {}
    prediction["msg"] = ""
    prediction["status"] = 0
    prediction["result"] = ""
    # TODO
    logger.info("推理完成")
    return prediction