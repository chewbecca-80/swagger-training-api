from pathlib import Path

from setuptools import setup


if __name__ == '__main__':
    tests_require = [
        'pytest',
        'flake8',
        'mypy',
        'pylint',
        'pytest-cov',
    ]

    setup(
        name="python-demo-api",
        author="Rebecca Servaites",
        author_email="kathryn.servaites@udri.udayton.edu",
        description="Python API Demo",

        long_description=Path("README.md").read_text(),
        long_description_content_type="text/markdown",

        url="https://git.act3-ace.com/rebecca.servaites/python-demo-api",

        license="Distribution C",

        setup_requires=[
            'setuptools_scm',
            'pytest-runner'
        ],
        use_scm_version={
            'fallback_version': '0.0.0',
        },

        # add in package_data and/or data_files
        include_package_data=True,
        package_data={
            'servaites.python_demo_api': ['*.yml', '*.yaml']
        },

        packages=[
            'servaites.python_demo_api',
        ],
        package_dir={'': 'src'},

        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],

        install_requires=[
            # 'aiohttp>=3.6.2',
            'ruamel.yaml',
        ],
        extras_require={
            "testing":  tests_require,
        },
        python_requires='>=3.7',

        entry_points={
            'console_scripts': [
                'demo_server = servaites.python_demo_api.server:main'
            ],
        },

    )
