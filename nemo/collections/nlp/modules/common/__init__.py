# Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
# Copyright 2018 The Google AI Language Team Authors and
# The HuggingFace Inc. team.
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

from nemo.collections.nlp.modules.common.bert_module import BertModule
from nemo.collections.nlp.modules.common.common_utils import get_pretrained_lm_model, get_pretrained_lm_models_list
from nemo.collections.nlp.modules.common.huggingface import *
from nemo.collections.nlp.modules.common.megatron import *
from nemo.collections.nlp.modules.common.sequence_classifier import SequenceClassifier
from nemo.collections.nlp.modules.common.token_classifier import BertPretrainingTokenClassifier, TokenClassifier
