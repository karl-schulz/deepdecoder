# Copyright 2015 Leon Sixt
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from distutils.core import setup
from pip.req import parse_requirements


install_reqs = parse_requirements('requirements.txt', session=False)
reqs = [str(ir.req) for ir in install_reqs]
dep_links = [str(req_line.url) for req_line in install_reqs]


setup(
    name='deepdecoder',
    version='0.0.1',
    description='models for my bacheleor thesis',
    author='Leon Sixt',
    author_email='github@leon-sixt.de',
    install_requires=reqs,
    dependency_links=dep_links,
    entry_points={
        'console_scripts': [
            'bb_extract_hd_images = deepdecoder.scripts.extract_hd_images:main',
            'bb_build_real_tag_dataset = deepdecoder.scripts.build_real_tag_dataset:run',
            'bb_generate_3d_tags = deepdecoder.scripts.generate_3d_tags:main',
            'bb_default_3d_tags_distribution = ' +
                'deepdecoder.scripts.default_3d_tags_distribution:main',
            'bb_train_tag3d_network = deepdecoder.scripts.train_tag3d_network:main',
            'bb_train_rendergan = deepdecoder.scripts.train_render_gan:main',
            'bb_sample_artificial_trainset = deepdecoder.scripts.sample_artificial_trainset:main',
            'bb_train_decoder = deepdecoder.scripts.train_decoder:main',
            'bb_evalute_decoder = deepdecoder.scripts.evaluate_decoder:main',
        ]
    },
    packages=[
        'deepdecoder',
        'deepdecoder.scripts',
    ]
)
