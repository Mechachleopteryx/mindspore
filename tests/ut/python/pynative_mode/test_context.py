# Copyright 2020 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
""" test_context """
import pytest
from mindspore import context
# pylint: disable=W0212
# W0212: protected-access


def setup_module(module):
    context.set_context(mode=context.PYNATIVE_MODE)


def test_contex_create_context():
    """ test_contex_create_context """
    context.set_context(mode=context.PYNATIVE_MODE)
    if context._k_context is None:
        ctx = context._context()
        assert ctx is not None
    context._k_context = None


def test_switch_mode():
    """ test_switch_mode """
    context.set_context(mode=context.GRAPH_MODE)
    assert context.get_context("mode") == context.GRAPH_MODE
    context.set_context(mode=context.PYNATIVE_MODE)
    assert context.get_context("mode") == context.PYNATIVE_MODE


def test_set_device_id():
    """ test_set_device_id """
    with pytest.raises(TypeError):
        context.set_context(device_id="cpu")
    assert context.get_context("device_id") == 0
    context.set_context(device_id=1)
    assert context.get_context("device_id") == 1


def test_device_target():
    """ test_device_target """
    with pytest.raises(TypeError):
        context.set_context(device_target=123)
    context.set_context(device_target="GPU")
    assert context.get_context("device_target") == "GPU"
    context.set_context(device_target="Ascend")
    assert context.get_context("device_target") == "Ascend"
    assert context.get_context("device_id") == 1


def test_dump_target():
    """ test_dump_target """
    with pytest.raises(TypeError):
        context.set_context(save_dump_path=1)
    context.set_context(enable_dump=False)
    assert context.get_context("enable_dump") == False
    context.set_context(enable_dump=True)
    assert context.get_context("enable_dump") == True
    assert context.get_context("save_dump_path") == "."


def test_set_context():
    """ test_set_context """
    context.set_context(mode=context.GRAPH_MODE, device_target="Ascend",
                        device_id=0, save_graphs=True, save_graphs_path="/mindspore")
    assert context.get_context("device_id") == 0
    assert context.get_context("device_target") == "Ascend"
    assert context.get_context("save_graphs")
    assert context.get_context("save_graphs_path") == "/mindspore"
    assert context.get_context("mode") == context.GRAPH_MODE

    context.set_context(mode=context.PYNATIVE_MODE)
    assert context.get_context("mode") == context.PYNATIVE_MODE
    assert context.get_context("device_target") == "Ascend"

    with pytest.raises(ValueError):
        context.set_context(modex="ge")
