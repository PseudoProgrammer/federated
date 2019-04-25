# Lint as: python3
# Copyright 2019, The TensorFlow Federated Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""A tiny version of Federated EMNIST, for testing.

The digits were generated programmatically using PIL.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import numpy as np


def from_ints(data):
  data = np.array(data)
  results = []
  for img_array in data:
    img_array = img_array.astype(np.float32) / 9.0
    results.append(img_array)
  return results


def get_data():
  """Returns a dictionary suitable for `tf.data.Dataset.from_tensor_slices`.

  Returns:
    A dictionary that matches the structure of the data produced by
    `tff.simulation.datasets.emnist.load_data`, with keys `pixels` and `label`.
  """
  data = np.array(DIGITS_DATA)
  img_list = []
  for img_array in data:
    img_array = img_array.astype(np.float32) / 9.0
    img_list.append(img_array)
  assert len(img_list) == 10
  return collections.OrderedDict([
      ('pixels', img_list), ('label', list(range(10)))])


# pyformat: disable
# pylint: disable=bad-continuation,bad-whitespace
DIGITS_DATA = [
   [[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,7,4,4,4,4,4,7,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,4,0,0,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,2,0,2,4,2,0,2,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,2,0,2,4,2,0,2,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,4,0,0,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,7,4,4,4,4,4,7,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]],

   [[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,7,4,4,4,7,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,4,4,2,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,0,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,4,4,2,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,4,4,2,0,0,0,2,4,4,4,7,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,0,0,0,0,0,0,0,0,4,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,4,4,4,4,4,4,4,4,4,4,7,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]],

   [[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,7,4,4,4,4,4,7,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,4,0,0,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,2,0,2,4,2,0,2,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,4,4,7,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,7,4,2,0,2,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,7,4,2,0,2,4,7,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,2,0,2,4,4,4,4,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,2,4,2,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,0,0,0,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,4,4,4,4,4,4,4,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]],

   [[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,7,4,4,4,4,4,7,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,4,0,0,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,2,0,2,4,2,0,2,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,4,4,7,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,7,4,4,4,2,0,2,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,4,0,0,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,7,4,4,4,2,0,2,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,4,4,7,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,2,0,2,4,2,0,2,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,4,0,0,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,7,4,4,4,4,4,7,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]],

   [[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,7,4,4,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,7,4,2,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,7,4,4,4,2,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,4,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,2,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,2,4,2,0,0,0,2,4,7,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,0,0,0,0,0,0,0,0,4,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,4,4,4,4,2,0,0,0,2,4,7,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,7,4,4,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]],

   [[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,4,4,4,4,4,4,4,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,0,0,0,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,2,4,4,4,4,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,2,4,4,4,7,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,0,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,2,4,2,0,2,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,4,4,7,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,7,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,4,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,2,4,4,4,2,0,2,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,0,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,4,4,4,4,4,4,7,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]],

   [[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,7,4,4,4,4,4,7,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,4,0,0,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,2,0,2,4,2,0,2,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,7,4,4,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,2,4,4,4,7,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,0,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,2,4,2,0,2,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,2,0,2,4,2,0,2,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,4,0,0,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,7,4,4,4,4,4,7,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]],

   [[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,4,4,4,4,4,4,4,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,0,0,0,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,2,4,2,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,4,4,7,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,7,4,2,0,2,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,7,4,2,0,2,4,7,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,7,4,4,4,7,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]],

   [[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,7,4,4,4,4,4,7,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,4,0,0,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,2,0,2,4,2,0,2,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,2,0,2,4,2,0,2,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,4,0,0,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,2,0,2,4,2,0,2,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,2,0,2,4,2,0,2,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,4,0,0,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,7,4,4,4,4,4,7,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]],

   [[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,7,4,4,4,4,4,7,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,4,0,0,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,2,0,2,4,2,0,2,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,2,0,2,4,2,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,4,0,0,0,0,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,7,4,4,4,2,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,4,4,7,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,4,0,0,0,4,9,4,0,0,0,4,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,7,4,2,0,2,4,2,0,2,4,7,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,4,0,0,0,0,0,4,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,7,4,4,4,4,4,7,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
    [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]]
]