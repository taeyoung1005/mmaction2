import torch
from mmaction.apis import init_recognizer, inference_recognizer
from mmengine import Config

# 설정 파일과 체크포인트 파일 경로 설정
config_path = '/mmaction2/work_dirs/my_custom_config_swin/my_custom_config_swin.py'
checkpoint_path = '/mmaction2/work_dirs/my_custom_config_swin/best_acc_top1_epoch_20.pth'

# 구성 파일 로드
config = Config.fromfile(config_path)

# 모델 초기화
model = init_recognizer(config, checkpoint_path, device='cuda:0')

# 모델을 평가 모드로 전환
model.eval()

# 데이터로더를 사용하여 데이터 반복
with torch.no_grad():
    video_path = "videos/bb_1_201113_vehicle_218_21015.mp4"  # 배치 내 각 비디오 경로

    # 예측 수행
    result = inference_recognizer(model, video_path)
    
    # 예측 결과에서 가장 높은 점수를 가진 클래스를 추출
    pred_class = result.pred_score.argmax()  # 예측된 클래스 ID를 추출

    print(f"Real class: 66, Predicted class: {pred_class}")  # Predicted class: 0
# Accuracy: 0.35