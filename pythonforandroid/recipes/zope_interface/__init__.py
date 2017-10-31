from pythonforandroid.toolchain import PythonRecipe, current_directory
import sh


class ZopeInterfaceRecipe(PythonRecipe):
    name = 'zope_interface'
    version = '4.4.3'
    url = 'https://github.com/zopefoundation/zope.interface/archive/{version}.tar.gz'
    site_packages_name = 'zope.interface'

    depends = [('python2', 'python3crystax')]
    patches = ['no_tests.patch']

    def prebuild_arch(self, arch):
        super(ZopeInterfaceRecipe, self).prebuild_arch(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            sh.rm('-rf', 'src/zope/interface/tests', 'src/zope/interface/common/tests')


recipe = ZopeInterfaceRecipe()
