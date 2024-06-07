import torch
from torch.utils.data import DataLoader, Dataset
from mmaction.apis import init_recognizer, inference_recognizer
from mmengine import Config

class CustomDataset(Dataset):
    def __init__(self, annotation_file):
        self.data = []
        with open(annotation_file, 'r') as f:
            for line in f:
                video_path, label = line.strip().split(' ')
                self.data.append((video_path, int(label)))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        video_path, label = self.data[idx]
        return video_path, label

# 설정 파일과 체크포인트 파일 경로 설정
config_path = '/mmaction2/work_dirs/my_custom_config_swin/my_custom_config_swin.py'
checkpoint_path = '/mmaction2/work_dirs/my_custom_config_swin/best_acc_top1_epoch_20.pth'

# 구성 파일 로드
config = Config.fromfile(config_path)

# 모델 초기화
model = init_recognizer(config, checkpoint_path, device='cuda:0')

# 데이터셋 및 데이터로더 빌드
annotation_file = '/mmaction2/data/custom/custom_val_list.txt'
dataset = CustomDataset(annotation_file)
dataloader = DataLoader(dataset, batch_size=32, shuffle=False, num_workers=4)

total = 0
correct = 0

# 모델을 평가 모드로 전환
model.eval()

# 데이터로더를 사용하여 데이터 반복
with torch.no_grad():
    for video_paths, labels in dataloader:
        for i in range(len(video_paths)):
            video_path = video_paths[i]  # 배치 내 각 비디오 경로
            label = labels[i].item()  # 배치 내 각 라벨

            # 예측 수행
            result = inference_recognizer(model, video_path)
            
            # 예측 결과에서 가장 높은 점수를 가진 클래스를 추출
            pred_class = result.pred_score.argmax()  # 예측된 클래스 ID를 추출
            
            if pred_class == label:
                correct += 1
            total += 1

accuracy = correct / total
print(f"Accuracy: {accuracy:.2f}")

# Accuracy: 0.35