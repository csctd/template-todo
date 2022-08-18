from setuptools import setup
from setuptools import find_packages 

setup(
    name='todobricks',
    version='0.1.0',
    packages = find_packages(),
    install_requires=[
        'Click', 'pandas',
    ],


)

    #
    # entry_points={
    #     'console_scripts': [
    #         'kwlfilecheck = kwltracking:get_file_list',
    #         'kwlfilecount = kwltracking:count_files',
    #         'kwlextracount = kwltracking:count_extra_files',
    #
    #     ],    },
