from setuptools import find_packages, setup


if __name__ == '__main__':
    setup(
        name='depth_anything',
        version='0.1.1',
        description='Human Parser from cozymantis/human-parser-comfyui-node',
        long_description='This repo is a fork from cozymantis/human-parser-comfyui-node',
        # long_description_content_type='text/markdown',
        author='Akmal Mukhsimov',
        author_email='aka.mukhsimov@gmail.com',
        keywords='computer vision, human part segmentation',
        url='https://github.com/amukhsimov/human-parser-comfyui-node',
        packages=['depth_anything', 'depth_anything.util'],
        # package_data={'schp.modules': ['src/*', 'src/utils/*']},
        # include_package_data=True,
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
        ],
        license='Apache License 2.0',
        install_requires=[
            'torch==2.3.0',
            'torchvision',
            'gradio==4.19.2',
            'gradio_imageslider',
            'opencv-python==4.8.0.76',
            'huggingface_hub'
        ]
        # extras_require={
        #     'eth_xgaze': parse_requirements('requirements.txt'),
        #     'tests': parse_requirements('requirements/tests.txt'),
        #     'build': parse_requirements('requirements/build.txt'),
        #     'optional': parse_requirements('requirements/optional.txt'),
        # },
        # ext_modules=[],
        # cmdclass={'build_ext': BuildExtension},
        # zip_safe=False
    )