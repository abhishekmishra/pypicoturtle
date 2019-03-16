from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
#use_plugin("python.coverage")
use_plugin("python.distutils")

authors = [Author('Abhishek Mishra', 'abhishekmishra3@gmail.com')]

name = "pypicoturtle"
default_task = "publish"
version = "0.0.1"
license = "MIT"
summary = "PicoTurtle python client"
url = "https://github.com/abhishekmishra/pypicoturtle"



@init
def set_properties(project):
    project.set_property("dir_source_main_python", "src")
    project.set_property("dir_source_unittest_python", "test")
    project.set_property("dir_source_main_scripts", "bin")
