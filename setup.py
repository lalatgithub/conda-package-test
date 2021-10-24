import setuptools
import os

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join(path, filename))
    return paths


docfiles = package_files('docs/build')

setuptools.setup(
    name="mdodata",
    version="2021.9.1",
    license="Proprietary",
    author="My Data Outlet International, LLC",
    author_email="support@mydataoutlet.com",
    description="This is the python version of the mdo.data library",
    long_description="This is the python version of the mdo.data library",
    long_description_content_type="text/markdown",
    url="https://mydataoutlet.com",
    include_package_data=True,
    packages=setuptools.find_packages(),
    package_data={"mdodata": ["mdologo.png", "assets/*"] + docfiles},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
    python_requires='>=3.7',
    install_requires=['pandas >= 1.3.2',
                      'sqlalchemy >= 1.4.19',
                      'snowflake_sqlalchemy==1.3.1',
                      'cryptography==3.3.2',
                      'snowflake_connector_python==2.6.2',
                      'numpy >= 1.18.1',
                      'dash==1.21.0',
                      'dash_core_components==1.17.1',
                      'dash_html_components==1.1.4',
                      'dash_bootstrap_components==0.13.0',
                      'dash_table==4.12.0',
                      'pyarrow==5.0.0',
                      'pyyaml >=5.4.1',
                      'certifi==2020.12.5',
                      'pyodbc==4.0.31',
                      'jupyter==1.0.0',
                      'jupyter-dash==0.4.0',
                      ]
)
