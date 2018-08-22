from distutils.core import setup
from Cython.Build import cythonize

setup(
    name="mktornado",
    ext_modules=cythonize("mktornado.py")
)
