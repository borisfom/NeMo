# Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Dict, Optional

import torch
from torch import nn as nn

from nemo.collections.common.parts import transformer_weights_init
from nemo.core.classes import Exportable, NeuralModule, typecheck
from nemo.core.neural_types import ChannelType, NeuralType

__all__ = ['Classifier']


class Classifier(NeuralModule, Exportable):
    """
    A baseclass for modules to perform various classification tasks.
    """

    @property
    def input_types(self) -> Optional[Dict[str, NeuralType]]:
        """
        Returns definitions of module input ports.
        """
        return {"hidden_states": NeuralType(('B', 'T', 'D'), ChannelType())}

    def __init__(self, hidden_size: int, dropout: float = 0.0,) -> None:

        """
        Initializes the Token Classifier module.

        Args:
            hidden_size: the size of the hidden dimension
            num_classes: number of classes
            num_layers: number of fully connected layers in the multilayer perceptron (MLP)
            activation: activation to usee between fully connected layers in the MLP
            log_softmax: whether to apply softmax to the output of the MLP
            dropout: dropout to apply to the input hidden states
            use_transformer_init: whether to initialize the weights of the classifier head with the same approach used in Transformer
        """
        super().__init__()
        self._hidden_size = hidden_size
        self.dropout = nn.Dropout(dropout)

    def post_init(self, use_transformer_init):
        if use_transformer_init:
            self.apply(lambda module: transformer_weights_init(module, xavier=False))

    def _prepare_for_export(self):
        """
        Returns a pair in input, output examples for tracing.
        Returns:
            A pair of (input, output) examples.
        """
        bs = 8
        seq = 64
        input_example = torch.randn(bs, seq, self._hidden_size).to(next(self.parameters()).device)
        output_example = self.forward(hidden_states=input_example)
        return input_example, output_example

    def save_to(self, save_path: str):
        """
        Saves the module to the specified path.
        Args:
            save_path: Path to where to save the module.
        """
        pass

    @classmethod
    def restore_from(cls, restore_path: str):
        """
        Restores the module from the specified path.
        Args:
            restore_path: Path to restore the module from.
        """
        pass
