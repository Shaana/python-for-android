
from pythonforandroid.toolchain import (
    PythonRecipe,
    Recipe,
    current_directory,
    info,
    shprint,
)
from os.path import join
import sh


class SetuptoolsRecipe(PythonRecipe):
    version = '18.3.1'
    url = 'https://pypi.python.org/packages/source/s/setuptools/setuptools-{version}.tar.gz'

    depends = [('python2', 'python3crystax')]
    

recipe = SetuptoolsRecipe()
