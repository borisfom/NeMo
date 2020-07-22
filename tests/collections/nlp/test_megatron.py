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

from unittest import TestCase

import pytest

import nemo.collections.nlp as nemo_nlp

class TestMegatron(TestCase):
    @pytest.mark.unit
    def test_list_pretrained_models(self):
        pretrained_lm_models = nemo_nlp.modules.get_pretrained_lm_models_list()
        self.assertTrue(len(pretrained_lm_models) > 0)

    @pytest.mark.unit
    def test_get_pretrained_bert_345m_uncased_model(self):
        model = nemo_nlp.modules.get_pretrained_lm_model('megatron-bert-345m-uncased')
        assert isinstance(model, nemo_nlp.modules.MegatronBertEncoder)

#    TODO: uncomment once https://gitlab-master.nvidia.com/ADLR/megatron-lm/-/merge_requests/98 is merged.
#    @pytest.mark.unit
#    def test_get_pretrained_bert_345m_cased_model(self):
#        model = nemo_nlp.modules.get_pretrained_lm_model('megatron-bert-345m-cased')
#        assert isinstance(model, nemo_nlp.modules.MegatronBertEncoder)

#    TODO : add test for 2 models requiring config
