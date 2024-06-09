_base_ = [
    '../../recognition/tsn/tsn_imagenet-pretrained-r50_8xb32-1x1x3-100e_kinetics400-rgb.py'  # inherit template config
]

# model settings
model = dict(
    cls_head=dict(
        type='TSNHead',
        num_classes=434,
        multi_class=False))

# dataset settings
dataset_type = 'RawframeDataset'
data_root = ''
ann_file_train = 'data/custom/custom_train_list.txt'
ann_file_val = 'data/custom/custom_val_list.txt'
ann_file_test = 'data/custom/custom_val_list.txt'

train_dataloader = dict(
    dataset=dict(
        ann_file=ann_file_train,
        data_prefix=dict(video=data_root)))
val_dataloader = dict(
    dataset=dict(
        ann_file=ann_file_val,
        data_prefix=dict(video=data_root)))
test_dataloader = dict(
    dataset=dict(
        ann_file=ann_file_val,
        data_prefix=dict(video=data_root)))

train_cfg = dict(
    type='EpochBasedTrainLoop',
    max_epochs=50,  # change from 100 to 50
    val_begin=1,
    val_interval=1)

val_cfg = dict(type='ValLoop')
test_cfg = dict(type='TestLoop')

param_scheduler = [
    dict(
        type='MultiStepLR',
        begin=0,
        end=50,  # change from 100 to 50
        by_epoch=True,
        milestones=[20, 40],  # change milestones
        gamma=0.1)
]

optim_wrapper = dict(
    optimizer=dict(
        type='SGD',
        lr=0.005, # change from 0.01 to 0.005
        momentum=0.9,
        weight_decay=0.0001),
    clip_grad=dict(max_norm=40, norm_type=2))