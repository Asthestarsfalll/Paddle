# Copyright (c) 2024 PaddlePaddle Authors. All Rights Reserved.
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

from typing import Protocol, Union

from typing_extensions import TypeAlias

from paddle import (
    CPUPlace,
    CUDAPinnedPlace,
    CUDAPlace,
    CustomPlace,
    IPUPlace,
    XPUPlace,
)


class _Place(Protocol):
    def __init__(self, id: int) -> None:
        ...


NPUPlace = _Place
MLUPlace = _Place

PlaceLike: TypeAlias = Union[
    CPUPlace,
    CUDAPlace,
    CUDAPinnedPlace,
    NPUPlace,
    IPUPlace,
    CustomPlace,
    MLUPlace,
    XPUPlace,
    # It seems that we cannot define the literal for dev:id in nowadays python type-hinting.
    str,
]
