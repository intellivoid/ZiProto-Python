# 
#  Copyright 2020 Intellivoid Technologies
# 
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#


import os
import sys
from shutil import rmtree
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()


setup(name='ziproto',
        version='1.0',
        description='Protocol Buffer used to serialize and compress data',
        long_description=long_description,
        long_description_content_type='text/markdown',
        author='Intellivoid Technologies',
        author_email='netkas@intellivoid.net',
        url='https://github.com/intellivoid/ZiProto-Python/',
        python_requires='>=3.6.0',
        include_package_data=True,
        py_modules=[
            'ziproto',
            'ziproto.ValueType',
            'ziproto.Headmap',
            'ziproto.ZiProtoFormat',
            'ziproto.ZiProtoEncoder',
            'ziproto.ZiProtoDecoder'
        ]
)
