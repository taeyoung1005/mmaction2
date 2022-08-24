_base_ = [
    '../../_base_/default_runtime.py', '../_base_/models/slowonly_r50.py'
]

# model settings
lfb_prefix_path = 'data/ava/lfb_half'
max_num_sampled_feat = 5
window_size = 60
lfb_channels = 2048
dataset_modes = ('train', 'val')

model = dict(
    roi_head=dict(
        shared_head=dict(
            type='FBOHead',
            lfb_cfg=dict(
                lfb_prefix_path=lfb_prefix_path,
                max_num_sampled_feat=max_num_sampled_feat,
                window_size=window_size,
                lfb_channels=lfb_channels,
                dataset_modes=dataset_modes,
                device='gpu'),
            fbo_cfg=dict(
                type='non_local',
                st_feat_channels=2048,
                lt_feat_channels=lfb_channels,
                latent_channels=512,
                num_st_feat=1,
                num_lt_feat=window_size * max_num_sampled_feat,
                num_non_local_layers=2,
                st_feat_dropout_ratio=0.2,
                lt_feat_dropout_ratio=0.2,
                pre_activate=True)),
        bbox_head=dict(in_channels=2560)))

dataset_type = 'AVADataset'
data_root = 'data/ava/rawframes'
anno_root = 'data/ava/annotations'

ann_file_train = f'{anno_root}/ava_train_v2.1.csv'
ann_file_val = f'{anno_root}/ava_val_v2.1.csv'

exclude_file_train = f'{anno_root}/ava_train_excluded_timestamps_v2.1.csv'
exclude_file_val = f'{anno_root}/ava_val_excluded_timestamps_v2.1.csv'

label_file = f'{anno_root}/ava_action_list_v2.1_for_activitynet_2018.pbtxt'

proposal_file_train = (f'{anno_root}/ava_dense_proposals_train.FAIR.'
                       'recall_93.9.pkl')
proposal_file_val = f'{anno_root}/ava_dense_proposals_val.FAIR.recall_93.9.pkl'

file_client_args = dict(
    io_backend='petrel',
    path_mapping=dict({'data/ava': 's3://openmmlab/datasets/action/ava'}))

train_pipeline = [
    dict(type='SampleAVAFrames', clip_len=4, frame_interval=16),
    dict(type='RawFrameDecode', **file_client_args),
    dict(type='RandomRescale', scale_range=(256, 320)),
    dict(type='RandomCrop', size=256),
    dict(type='Flip', flip_ratio=0.5),
    dict(type='FormatShape', input_format='NCTHW', collapse=True),
    dict(type='PackActionInputs')
]
# The testing is w/o. any cropping / flipping
val_pipeline = [
    dict(
        type='SampleAVAFrames', clip_len=4, frame_interval=16, test_mode=True),
    dict(type='RawFrameDecode', **file_client_args),
    dict(type='Resize', scale=(-1, 256)),
    dict(type='FormatShape', input_format='NCTHW', collapse=True),
    dict(type='PackActionInputs')
]

train_dataloader = dict(
    batch_size=12,
    num_workers=8,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    dataset=dict(
        type=dataset_type,
        ann_file=ann_file_train,
        exclude_file=exclude_file_train,
        pipeline=train_pipeline,
        label_file=label_file,
        proposal_file=proposal_file_train,
        data_prefix=dict(img=data_root),
        person_det_score_thr=0.9))

val_dataloader = dict(
    batch_size=1,
    num_workers=8,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        ann_file=ann_file_val,
        exclude_file=exclude_file_val,
        pipeline=val_pipeline,
        label_file=label_file,
        proposal_file=proposal_file_val,
        data_prefix=dict(img=data_root),
        person_det_score_thr=0.9,
        test_mode=True))

test_dataloader = val_dataloader

val_evaluator = dict(
    type='AVAMetric',
    ann_file=ann_file_val,
    label_file=label_file,
    exclude_file=exclude_file_val)
test_evaluator = val_evaluator

default_hooks = dict(checkpoint=dict(interval=3, max_keep_ckpts=3))

train_cfg = dict(
    type='EpochBasedTrainLoop', max_epochs=20, val_begin=1, val_interval=1)
val_cfg = dict(type='ValLoop')
test_cfg = dict(type='TestLoop')

param_scheduler = [
    dict(
        type='LinearLR',
        start_factor=0.1,
        by_epoch=True,
        begin=0,
        end=5,
        convert_to_iter_based=True),
    dict(
        type='MultiStepLR',
        begin=0,
        end=20,
        by_epoch=True,
        milestones=[10, 15],
        gamma=0.1)
]

optim_wrapper = dict(
    optimizer=dict(type='SGD', lr=0.15, momentum=0.9, weight_decay=1e-05),
    clip_grad=dict(max_norm=20, norm_type=2))

find_unused_parameters = False
load_from = ('https://download.openmmlab.com/mmaction/recognition/slowonly/'
             'slowonly_r50_4x16x1_256e_kinetics400_rgb/'
             'slowonly_r50_4x16x1_256e_kinetics400_rgb_20200704-a69556c6.pth')