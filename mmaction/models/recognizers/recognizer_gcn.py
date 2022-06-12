# Copyright (c) OpenMMLab. All rights reserved.
from mmaction.registry import MODELS
from .base import BaseRecognizer


@MODELS.register_module()
class RecognizerGCN(BaseRecognizer):
    """GCN recognizer model framework."""

    def extract_feat(self, batch_inputs, stage='backbone', **kwargs):
        """Extract features of different stages.

        Args:
            batch_inputs (torch.Tensor): The input data.
            stage (str): Which stage to output the feature.
                Defaults to "backbone".
        Returns:
                torch.tensor: The extracted features.
                dict: A dict recording the kwargs for downstream
                    pipeline. These keys are usually included:
                    `loss_aux`.
        """

        # Record the kwargs required by `loss` and `predict`
        loss_predict_kwargs = dict()
        x = self.backbone(batch_inputs)

        if stage == 'backbone':
            return x, loss_predict_kwargs

        if self.with_cls_head and stage == 'head':
            x = self.cls_head(x, **loss_predict_kwargs)
            return x, loss_predict_kwargs
