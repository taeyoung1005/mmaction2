<div align="center">
  <img src="https://github.com/open-mmlab/mmaction2/raw/main/resources/mmaction2_logo.png" width="600"/>
  <div>&nbsp;</div>
  <div align="center">
    <b><font size="5">OpenMMLab website</font></b>
    <sup>
      <a href="https://openmmlab.com">
        <i><font size="4">HOT</font></i>
      </a>
    </sup>
    &nbsp;&nbsp;&nbsp;&nbsp;
    <b><font size="5">OpenMMLab platform</font></b>
    <sup>
      <a href="https://platform.openmmlab.com">
        <i><font size="4">TRY IT OUT</font></i>
      </a>
    </sup>
  </div>

[![Documentation](https://readthedocs.org/projects/mmaction2/badge/?version=latest)](https://mmaction2.readthedocs.io/en/latest/)
[![actions](https://github.com/open-mmlab/mmaction2/workflows/build/badge.svg)](https://github.com/open-mmlab/mmaction2/actions)
[![codecov](https://codecov.io/gh/open-mmlab/mmaction2/branch/main/graph/badge.svg)](https://codecov.io/gh/open-mmlab/mmaction2)
[![PyPI](https://img.shields.io/pypi/v/mmaction2)](https://pypi.org/project/mmaction2/)
[![LICENSE](https://img.shields.io/github/license/open-mmlab/mmaction2.svg)](https://github.com/open-mmlab/mmaction2/blob/main/LICENSE)
[![Average time to resolve an issue](https://isitmaintained.com/badge/resolution/open-mmlab/mmaction2.svg)](https://github.com/open-mmlab/mmaction2/issues)
[![Percentage of issues still open](https://isitmaintained.com/badge/open/open-mmlab/mmaction2.svg)](https://github.com/open-mmlab/mmaction2/issues)

[📘Documentation](https://mmaction2.readthedocs.io/en/latest/) |
[🛠️Installation](https://mmaction2.readthedocs.io/en/latest/get_started/installation.html) |
[👀Model Zoo](https://mmaction2.readthedocs.io/en/latest/modelzoo_statistics.html) |
[🆕Update News](https://mmaction2.readthedocs.io/en/latest/notes/changelog.html) |
[🚀Ongoing Projects](https://github.com/open-mmlab/mmaction2/projects) |
[🤔Reporting Issues](https://github.com/open-mmlab/mmaction2/issues/new/choose)

</div>

<div align="center">
  <a href="https://openmmlab.medium.com/" style="text-decoration:none;">
    <img src="https://user-images.githubusercontent.com/25839884/219255827-67c1a27f-f8c5-46a9-811d-5e57448c61d1.png" width="3%" alt="" /></a>
  <img src="https://user-images.githubusercontent.com/25839884/218346358-56cc8e2f-a2b8-487f-9088-32480cceabcf.png" width="3%" alt="" />
  <a href="https://discord.com/channels/1037617289144569886/1046608014234370059" style="text-decoration:none;">
    <img src="https://user-images.githubusercontent.com/25839884/218347213-c080267f-cbb6-443e-8532-8e1ed9a58ea9.png" width="3%" alt="" /></a>
  <img src="https://user-images.githubusercontent.com/25839884/218346358-56cc8e2f-a2b8-487f-9088-32480cceabcf.png" width="3%" alt="" />
  <a href="https://twitter.com/OpenMMLab" style="text-decoration:none;">
    <img src="https://user-images.githubusercontent.com/25839884/218346637-d30c8a0f-3eba-4699-8131-512fb06d46db.png" width="3%" alt="" /></a>
  <img src="https://user-images.githubusercontent.com/25839884/218346358-56cc8e2f-a2b8-487f-9088-32480cceabcf.png" width="3%" alt="" />
  <a href="https://www.youtube.com/openmmlab" style="text-decoration:none;">
    <img src="https://user-images.githubusercontent.com/25839884/218346691-ceb2116a-465a-40af-8424-9f30d2348ca9.png" width="3%" alt="" /></a>
  <img src="https://user-images.githubusercontent.com/25839884/218346358-56cc8e2f-a2b8-487f-9088-32480cceabcf.png" width="3%" alt="" />
  <a href="https://space.bilibili.com/1293512903" style="text-decoration:none;">
    <img src="https://user-images.githubusercontent.com/25839884/219026751-d7d14cce-a7c9-4e82-9942-8375fca65b99.png" width="3%" alt="" /></a>
  <img src="https://user-images.githubusercontent.com/25839884/218346358-56cc8e2f-a2b8-487f-9088-32480cceabcf.png" width="3%" alt="" />
  <a href="https://www.zhihu.com/people/openmmlab" style="text-decoration:none;">
    <img src="https://user-images.githubusercontent.com/25839884/219026120-ba71e48b-6e94-4bd4-b4e9-b7d175b5e362.png" width="3%" alt="" /></a>
</div>

English | [简体中文](/README_zh-CN.md)

## 📄 Table of Contents

- [📄 Table of Contents](#-table-of-contents)
- [🥳 🚀 What's New](#--whats-new-)
- [📖 Introduction](#-introduction-)
- [🎁 Major Features](#-major-features-)
- [🛠️ Installation](#️-installation-)
- [👀 Model Zoo](#-model-zoo-)
- [👨‍🏫 Get Started](#-get-started-)
- [🎫 License](#-license-)
- [🖊️ Citation](#️-citation-)
- [🙌 Contributing](#-contributing-)
- [🤝 Acknowledgement](#-acknowledgement-)
- [🏗️ Projects in OpenMMLab](#️-projects-in-openmmlab-)

## 🥳 🚀 What's New [🔝](#-table-of-contents)

**The default branch has been switched to `main`(previous `1.x`) from `master`(current `0.x`), and we encourage users to migrate to the latest version with more supported models, stronger pre-training checkpoints and simpler coding. Please refer to [Migration Guide](https://mmaction2.readthedocs.io/en/latest/migration.html) for more details.**

**Release (2023.10.12)**: v1.2.0 with the following new features:

- Support VindLU multi-modality algorithm and the Training of ActionClip
- Support lightweight model MobileOne TSN/TSM
- Support video retrieval dataset MSVD
- Support SlowOnly K700 feature to train localization models
- Support Video and Audio Demos

## 📖 Introduction [🔝](#-table-of-contents)

MMAction2 is an open-source toolbox for video understanding based on PyTorch.
It is a part of the [OpenMMLab](http://openmmlab.com/) project.

<div align="center">
  <img src="https://github.com/open-mmlab/mmaction2/raw/main/resources/mmaction2_overview.gif" width="380px">
  <img src="https://user-images.githubusercontent.com/34324155/123989146-2ecae680-d9fb-11eb-916b-b9db5563a9e5.gif" width="380px">
  <p style="font-size:1.5vw;"> Action Recognition on Kinetics-400 (left) and Skeleton-based Action Recognition on NTU-RGB+D-120 (right)</p>
</div>

<div align="center">
  <img src="https://user-images.githubusercontent.com/30782254/155710881-bb26863e-fcb4-458e-b0c4-33cd79f96901.gif" width="580px"/><br>
    <p style="font-size:1.5vw;">Skeleton-based Spatio-Temporal Action Detection and Action Recognition Results on Kinetics-400</p>
</div>
<div align="center">
  <img src="https://github.com/open-mmlab/mmaction2/raw/main/resources/spatio-temporal-det.gif" width="800px"/><br>
    <p style="font-size:1.5vw;">Spatio-Temporal Action Detection Results on AVA-2.1</p>
</div>

## 🎁 Major Features [🔝](#-table-of-contents)

- **Modular design**: We decompose a video understanding framework into different components. One can easily construct a customized video understanding framework by combining different modules.

- **Support five major video understanding tasks**: MMAction2 implements various algorithms for multiple video understanding tasks, including action recognition, action localization, spatio-temporal action detection, skeleton-based action detection and video retrieval.

- **Well tested and documented**: We provide detailed documentation and API reference, as well as unit tests.

## 🛠️ Installation [🔝](#-table-of-contents)

MMAction2 depends on [PyTorch](https://pytorch.org/), [MMCV](https://github.com/open-mmlab/mmcv), [MMEngine](https://github.com/open-mmlab/mmengine), [MMDetection](https://github.com/open-mmlab/mmdetection) (optional) and [MMPose](https://github.com/open-mmlab/mmpose) (optional).

Please refer to [install.md](https://mmaction2.readthedocs.io/en/latest/get_started/installation.html) for detailed instructions.

<details close>
<summary>Quick instructions</summary>

```shell
conda create --name openmmlab python=3.8 -y
conda activate openmmlab
conda install pytorch torchvision -c pytorch  # This command will automatically install the latest version PyTorch and cudatoolkit, please check whether they match your environment.
pip install -U openmim
mim install mmengine
mim install mmcv
mim install mmdet  # optional
mim install mmpose  # optional
git clone https://github.com/open-mmlab/mmaction2.git
cd mmaction2
pip install -v -e .
```

</details>

## 👀 Model Zoo [🔝](#-table-of-contents)

Results and models are available in the [model zoo](https://mmaction2.readthedocs.io/en/latest/model_zoo/modelzoo.html).

<details close>

<summary>Supported model</summary>

<table style="margin-left:auto;margin-right:auto;font-size:1.3vw;padding:3px 5px;text-align:center;vertical-align:center;">
  <tr>
    <td colspan="5" style="font-weight:bold;">Action Recognition</td>
  </tr>
  <tr>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/c3d/README.md">C3D</a> (CVPR'2014)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/tsn/README.md">TSN</a> (ECCV'2016)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/i3d/README.md">I3D</a> (CVPR'2017)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/c2d/README.md">C2D</a> (CVPR'2018)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/i3d/README.md">I3D Non-Local</a> (CVPR'2018)</td>
  </tr>
  <tr>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/r2plus1d/README.md">R(2+1)D</a> (CVPR'2018)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/trn/README.md">TRN</a> (ECCV'2018)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/tsm/README.md">TSM</a> (ICCV'2019)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/tsm/README.md">TSM Non-Local</a> (ICCV'2019)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/slowonly/README.md">SlowOnly</a> (ICCV'2019)</td>
  </tr>
  <tr>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/slowfast/README.md">SlowFast</a> (ICCV'2019)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/csn/README.md">CSN</a> (ICCV'2019)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/tin/README.md">TIN</a> (AAAI'2020)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/tpn/README.md">TPN</a> (CVPR'2020)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/x3d/README.md">X3D</a> (CVPR'2020)</td>
  </tr>
  <tr>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition_audio/resnet/README.md">MultiModality: Audio</a> (ArXiv'2020)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/tanet/README.md">TANet</a> (ArXiv'2020)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/timesformer/README.md">TimeSformer</a> (ICML'2021)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/projects/actionclip/README.md">ActionCLIP</a> (ArXiv'2021)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/swin/README.md">VideoSwin</a> (CVPR'2022)</td>
  </tr>
  <tr>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/videomae/README.md">VideoMAE</a> (NeurIPS'2022)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/mvit/README.md">MViT V2</a> (CVPR'2022)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/uniformer/README.md">UniFormer V1</a> (ICLR'2022)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/uniformerv2/README.md">UniFormer V2</a> (Arxiv'2022)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/videomaev2/README.md">VideoMAE V2</a> (CVPR'2023)</td>
  </tr>
  <tr>
    <td colspan="5" style="font-weight:bold;">Action Localization</td>
  </tr>
  <tr>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/localization/bsn/README.md">BSN</a> (ECCV'2018)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/localization/bmn/README.md">BMN</a> (ICCV'2019)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/localization/tcanet/README.md">TCANet</a> (CVPR'2021)</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td colspan="5" style="font-weight:bold;">Spatio-Temporal Action Detection</td>
  </tr>
  <tr>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/detection/acrn/README.md">ACRN</a> (ECCV'2018)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/detection/slowonly/README.md">SlowOnly+Fast R-CNN</a> (ICCV'2019)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/detection/slowfast/README.md">SlowFast+Fast R-CNN</a> (ICCV'2019)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/detection/lfb/README.md">LFB</a> (CVPR'2019)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/recognition/videomae/README.md">VideoMAE</a> (NeurIPS'2022)</td>
  </tr>
  <tr>
    <td colspan="5" style="font-weight:bold;">Skeleton-based Action Recognition</td>
  </tr>
  <tr>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/skeleton/stgcn/README.md">ST-GCN</a> (AAAI'2018)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/skeleton/2s-agcn/README.md">2s-AGCN</a> (CVPR'2019)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/skeleton/posec3d/README.md">PoseC3D</a> (CVPR'2022)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/skeleton/stgcnpp/README.md">STGCN++</a> (ArXiv'2022)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/projects/ctrgcn/README.md">CTRGCN</a> (CVPR'2021)</td>
  </tr>
  <tr>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/projects/msg3d/README.md">MSG3D</a> (CVPR'2020)</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td colspan="5" style="font-weight:bold;">Video Retrieval</td>
  </tr>
  <tr>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/configs/retrieval/clip4clip/README.md">CLIP4Clip</a> (ArXiv'2022)</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>

</table>

</details>

<details close>

<summary>Supported dataset</summary>

<table style="margin-left:auto;margin-right:auto;font-size:1.3vw;padding:3px 5px;text-align:center;vertical-align:center;">
  <tr>
    <td colspan="4" style="font-weight:bold;">Action Recognition</td>
  </tr>
  <tr>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/hmdb51/README.md">HMDB51</a> (<a href="https://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database/">Homepage</a>) (ICCV'2011)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/ucf101/README.md">UCF101</a> (<a href="https://www.crcv.ucf.edu/research/data-sets/ucf101/">Homepage</a>) (CRCV-IR-12-01)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/activitynet/README.md">ActivityNet</a> (<a href="http://activity-net.org/">Homepage</a>) (CVPR'2015)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/kinetics/README.md">Kinetics-[400/600/700]</a> (<a href="https://deepmind.com/research/open-source/kinetics/">Homepage</a>) (CVPR'2017)</td>
  </tr>
  <tr>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/sthv1/README.md">SthV1</a>  (ICCV'2017)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/sthv2/README.md">SthV2</a> (<a href="https://developer.qualcomm.com/software/ai-datasets/something-something">Homepage</a>) (ICCV'2017)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/diving48/README.md">Diving48</a> (<a href="http://www.svcl.ucsd.edu/projects/resound/dataset.html">Homepage</a>) (ECCV'2018)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/jester/README.md">Jester</a> (<a href="https://developer.qualcomm.com/software/ai-datasets/jester">Homepage</a>) (ICCV'2019)</td>
  </tr>
  <tr>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/mit/README.md">Moments in Time</a> (<a href="http://moments.csail.mit.edu/">Homepage</a>) (TPAMI'2019)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/mmit/README.md">Multi-Moments in Time</a> (<a href="http://moments.csail.mit.edu/challenge_iccv_2019.html">Homepage</a>) (ArXiv'2019)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/hvu/README.md">HVU</a> (<a href="https://github.com/holistic-video-understanding/HVU-Dataset">Homepage</a>) (ECCV'2020)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/omnisource/README.md">OmniSource</a> (<a href="https://kennymckormick.github.io/omnisource/">Homepage</a>) (ECCV'2020)</td>
  </tr>
  <tr>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/gym/README.md">FineGYM</a> (<a href="https://sdolivia.github.io/FineGym/">Homepage</a>) (CVPR'2020)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/kinetics710/README.md">Kinetics-710</a> (<a href="https://arxiv.org/pdf/2211.09552.pdf">Homepage</a>) (Arxiv'2022)</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td colspan="4" style="font-weight:bold;">Action Localization</td>
  </tr>
  <tr>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/thumos14/README.md">THUMOS14</a> (<a href="https://www.crcv.ucf.edu/THUMOS14/download.html">Homepage</a>) (THUMOS Challenge 2014)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/activitynet/README.md">ActivityNet</a> (<a href="http://activity-net.org/">Homepage</a>) (CVPR'2015)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/hacs/README.md">HACS</a> (<a href="https://github.com/hangzhaomit/HACS-dataset">Homepage</a>) (ICCV'2019)</td>
    <td></td>
  </tr>
  <tr>
    <td colspan="4" style="font-weight:bold;">Spatio-Temporal Action Detection</td>
  </tr>
  <tr>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/ucf101_24/README.md">UCF101-24*</a> (<a href="http://www.thumos.info/download.html">Homepage</a>) (CRCV-IR-12-01)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/jhmdb/README.md">JHMDB*</a> (<a href="http://jhmdb.is.tue.mpg.de/">Homepage</a>) (ICCV'2015)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/ava/README.md">AVA</a> (<a href="https://research.google.com/ava/index.html">Homepage</a>) (CVPR'2018)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/ava_kinetics/README.md">AVA-Kinetics</a> (<a href="https://research.google.com/ava/index.html">Homepage</a>) (Arxiv'2020)</td>
  </tr>
  <tr>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/multisports/README.md">MultiSports</a> (<a href="https://deeperaction.github.io/datasets/multisports.html">Homepage</a>) (ICCV'2021)</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td colspan="4" style="font-weight:bold;">Skeleton-based Action Recognition</td>
  </tr>
  <tr>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/skeleton/README.md">PoseC3D-FineGYM</a> (<a href="https://kennymckormick.github.io/posec3d/">Homepage</a>) (ArXiv'2021)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/skeleton/README.md">PoseC3D-NTURGB+D</a> (<a href="https://kennymckormick.github.io/posec3d/">Homepage</a>) (ArXiv'2021)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/skeleton/README.md">PoseC3D-UCF101</a> (<a href="https://kennymckormick.github.io/posec3d/">Homepage</a>) (ArXiv'2021)</td>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/skeleton/README.md">PoseC3D-HMDB51</a> (<a href="https://kennymckormick.github.io/posec3d/">Homepage</a>) (ArXiv'2021)</td>
  </tr>
  <tr>
    <td colspan="4" style="font-weight:bold;">Video Retrieval</td>
  </tr>
  <tr>
    <td><a href="https://github.com/open-mmlab/mmaction2/blob/main/tools/data/video_retrieval/README.md">MSRVTT</a> (<a href="https://www.microsoft.com/en-us/research/publication/msr-vtt-a-large-video-description-dataset-for-bridging-video-and-language/">Homepage</a>) (CVPR'2016)</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>

</table>

</details>

## 👨‍🏫 Get Started [🔝](#-table-of-contents)

For tutorials, we provide the following user guides for basic usage:

- [Migration from MMAction2 0.X](https://mmaction2.readthedocs.io/en/latest/migration.html)
- [Learn about Configs](https://mmaction2.readthedocs.io/en/latest/user_guides/config.html)
- [Prepare Datasets](https://mmaction2.readthedocs.io/en/latest/user_guides/prepare_dataset.html)
- [Inference with Existing Models](https://mmaction2.readthedocs.io/en/latest/user_guides/inference.html)
- [Training and Testing](https://mmaction2.readthedocs.io/en/latest/user_guides/train_test.html)

<details close>
<summary>Research works built on MMAction2 by users from community</summary>

- Video Swin Transformer. [\[paper\]](https://arxiv.org/abs/2106.13230)[\[github\]](https://github.com/SwinTransformer/Video-Swin-Transformer)
- Evidential Deep Learning for Open Set Action Recognition, ICCV 2021 **Oral**. [\[paper\]](https://arxiv.org/abs/2107.10161)[\[github\]](https://github.com/Cogito2012/DEAR)
- Rethinking Self-supervised Correspondence Learning: A Video Frame-level Similarity Perspective, ICCV 2021 **Oral**. [\[paper\]](https://arxiv.org/abs/2103.17263)[\[github\]](https://github.com/xvjiarui/VFS)

</details>

## 🎫 License [🔝](#-table-of-contents)

This project is released under the [Apache 2.0 license](LICENSE).

## 🖊️ Citation [🔝](#-table-of-contents)

If you find this project useful in your research, please consider cite:

```BibTeX
@misc{2020mmaction2,
    title={OpenMMLab's Next Generation Video Understanding Toolbox and Benchmark},
    author={MMAction2 Contributors},
    howpublished = {\url{https://github.com/open-mmlab/mmaction2}},
    year={2020}
}
```

## 🙌 Contributing [🔝](#-table-of-contents)

We appreciate all contributions to improve MMAction2. Please refer to [CONTRIBUTING.md](https://github.com/open-mmlab/mmcv/blob/2.x/CONTRIBUTING.md) in MMCV for more details about the contributing guideline.

## 🤝 Acknowledgement [🔝](#-table-of-contents)

MMAction2 is an open-source project that is contributed by researchers and engineers from various colleges and companies.
We appreciate all the contributors who implement their methods or add new features and users who give valuable feedback.
We wish that the toolbox and benchmark could serve the growing research community by providing a flexible toolkit to reimplement existing methods and develop their new models.

## 🏗️ Projects in OpenMMLab [🔝](#-table-of-contents)

- [MMEngine](https://github.com/open-mmlab/mmengine): OpenMMLab foundational library for training deep learning models.
- [MMCV](https://github.com/open-mmlab/mmcv): OpenMMLab foundational library for computer vision.
- [MIM](https://github.com/open-mmlab/mim): MIM installs OpenMMLab packages.
- [MMEval](https://github.com/open-mmlab/mmeval): A unified evaluation library for multiple machine learning libraries.
- [MMPreTrain](https://github.com/open-mmlab/mmpretrain): OpenMMLab pre-training toolbox and benchmark.
- [MMDetection](https://github.com/open-mmlab/mmdetection): OpenMMLab detection toolbox and benchmark.
- [MMDetection3D](https://github.com/open-mmlab/mmdetection3d): OpenMMLab's next-generation platform for general 3D object detection.
- [MMRotate](https://github.com/open-mmlab/mmrotate): OpenMMLab rotated object detection toolbox and benchmark.
- [MMYOLO](https://github.com/open-mmlab/mmyolo): OpenMMLab YOLO series toolbox and benchmark.
- [MMSegmentation](https://github.com/open-mmlab/mmsegmentation): OpenMMLab semantic segmentation toolbox and benchmark.
- [MMOCR](https://github.com/open-mmlab/mmocr): OpenMMLab text detection, recognition, and understanding toolbox.
- [MMPose](https://github.com/open-mmlab/mmpose): OpenMMLab pose estimation toolbox and benchmark.
- [MMHuman3D](https://github.com/open-mmlab/mmhuman3d): OpenMMLab 3D human parametric model toolbox and benchmark.
- [MMSelfSup](https://github.com/open-mmlab/mmselfsup): OpenMMLab self-supervised learning toolbox and benchmark.
- [MMRazor](https://github.com/open-mmlab/mmrazor): OpenMMLab model compression toolbox and benchmark.
- [MMFewShot](https://github.com/open-mmlab/mmfewshot): OpenMMLab fewshot learning toolbox and benchmark.
- [MMAction2](https://github.com/open-mmlab/mmaction2): OpenMMLab's next-generation action understanding toolbox and benchmark.
- [MMTracking](https://github.com/open-mmlab/mmtracking): OpenMMLab video perception toolbox and benchmark.
- [MMFlow](https://github.com/open-mmlab/mmflow): OpenMMLab optical flow toolbox and benchmark.
- [MMagic](https://github.com/open-mmlab/mmagic): Open**MM**Lab **A**dvanced, **G**enerative and **I**ntelligent **C**reation toolbox.
- [MMGeneration](https://github.com/open-mmlab/mmgeneration): OpenMMLab image and video generative models toolbox.
- [MMDeploy](https://github.com/open-mmlab/mmdeploy): OpenMMLab model deployment framework.
- [Playground](https://github.com/open-mmlab/playground): A central hub for gathering and showcasing amazing projects built upon OpenMMLab.

<br/>
<br/>

# 교통사고 판례 추천 API

이 프로젝트는 비디오 입력에서 사고 유형을 예측하고 예측된 사고 유형을 기반으로 사법 판례를 검색하는 API를 제공합니다.

## 기능

- **비디오 분류**: 사전 학습된 모델을 사용하여 비디오 입력에서 사고 유형을 분류합니다.
- **사법 판례 검색**: 예측된 사고 유형을 기반으로 로컬 네트워크 API를 호출하여 사법 판례를 검색합니다.

### 1. Data 준비

[AIHUB 교통사고 영상 데이터](https://aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=597)

[데이터 설명서](vscode-local:/c%3A/Users/mu070/OneDrive/Documents/%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%86%A1%20%EB%B0%9B%EC%9D%80%20%ED%8C%8C%EC%9D%BC/%EA%B5%90%ED%86%B5%EC%82%AC%EA%B3%A0_%EC%98%81%EC%83%81_%EB%8D%B0%EC%9D%B4%ED%84%B0_%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%84%A4%EB%AA%85%EC%84%9C.csv)
![alt text](image.png)

### 2. 모델 준비

모델 구성 파일과 체크포인트 파일을 `work_dirs` 디렉토리에 배치합니다.

- [`my_custom_config_tsn.py`](https://drive.google.com/file/d/1G0boPGOqMkOS__Ka1QtUPegbeOTH9o7W/view?usp=drive_link)
- [`best_acc_top1_epoch_20.pth`](https://drive.google.com/file/d/15FHjHs0ov2SoLl0Vhgz53GmqUqj6E7c7/view?usp=sharing)

### 3. Docker 컨테이너 빌드 및 실행

```bash
docker-compose up --build
```

이 명령어는 `2578` 포트에서 API 서비스를, `82` 포트에서 Nginx 서비스를 시작합니다.

<br/>

## API 엔드포인트

### `/judicial-precedent` (POST)

비디오에서 사고 유형을 예측하고 해당 사법 판례를 검색합니다.

#### 요청

- **메서드**: POST
- **Content-Type**: multipart/form-data
- **파라미터**:
  - `video`: 분류할 비디오 파일.

#### 예시 요청

```bash
curl -X POST "http://localhost:2578/judicial-precedent" -F "video=@path_to_your_video_file"
```

#### 응답

응답은 [판례 API](https://github.com/taeyoung1005/judgment-api)에서 반환된 JSON 데이터입니다.

### 예시 응답

```json
[
  {
    "판례정보일련번호": 187882,
    "사건명": "교통사고처리특례법위반",
    "사건번호": "2016노186",
    "선고일자": 20161027,
    "법원명": "대구지법",
    "법원종류코드": 400202,
    "사건종류명": "형사",
    "사건종류코드": 400102,
    "판시사항": "자동차 운전자인 피고인이 유턴을...",
    "판결요지": "자동차 운전자인 피고인이 유턴을...",
    "판례내용": "【피 고 인】 <br/>【항 소 인】 검사...",
    "url": "https://www.law.go.kr/precInfoP.do?mode=0&precSeq=187882"
  }
]
```

## 프로젝트 구조

- **main.py**: 주요 FastAPI 애플리케이션 파일.
- **docker-compose.yml**: Docker Compose 설정 파일.
- **Dockerfile**: API 서비스용 Dockerfile.
- **Dockerfile(nginx)**: Nginx 서비스용 Dockerfile.
- **nginx.conf**: Nginx 서비스 config.
- **work_dirs/**: 모델 구성 및 체크포인트 파일 디렉토리.

## 개발 노트

- 로컬 네트워크 사법 판례 API가 실행 중이며 `http://192.168.0.7:8383/judgment`에서 접근 가능한지 확인하세요.
- `main.py`에서 `config_path`와 `checkpoint_path`를 파일이 위치한 경로에 맞게 수정하세요.