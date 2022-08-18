from setuptools import setup

setup(
    name='todobricks',
    version='0.1.0',
    py_modules=['todobricks'],
    install_requires=[
        'Click', 'pandas', 'lxml', 'numpy'
    ],
    entry_points={
        'console_scripts': [
            'kwlfilecheck = kwltracking:get_file_list',
            'kwlfilecount = kwltracking:count_files',
            'kwlextracount = kwltracking:count_extra_files',

        ],
    },
)
