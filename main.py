import os

import requests
from fastapi import FastAPI, File, UploadFile
import torch
from mmaction.apis import init_recognizer, inference_recognizer
from mmengine import Config

app = FastAPI(
    title="Judicial Precedent API",
    description="사고 유형을 예측하고 판례를 제공하는 API",
    version="1.0.0",
)


def video_classification(video_input_path):
    config_path = "work_dirs/my_custom_config_tsn/my_custom_config_tsn.py"
    checkpoint_path = "work_dirs/my_custom_config_tsn/best_acc_top1_epoch_20.pth"

    config = Config.fromfile(config_path)

    model = init_recognizer(config, checkpoint_path, device="cuda:0")

    result = inference_recognizer(model, video_input_path)

    predict = int(result.pred_score.argmax())
    print(f"Predicted class: {predict}")

    import gc

    torch.cuda.empty_cache()
    del config, model, result
    gc.collect()

    return predict


@app.post("/judicial-precedent")
async def judicial_precedent(video: UploadFile = File(...)):
    if not os.path.exists("input_video"):
        os.mkdir("input_video")

    video_input_path = f"input_video/{video.filename}"

    with open(video_input_path, "wb") as buffer:
        buffer.write(video.file.read())

    predict = video_classification(video_input_path)

    # local network 내의 판례 API 호출
    response = requests.post(
        "http://192.168.0.7:8383/judgment", json={"accident_type": predict}
    )

    return response.json()
