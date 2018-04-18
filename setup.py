from setuptools import setup, find_packages

# Workaround for issue
# https://bugs.python.org/issue15881

try:
	import multiprocessing
except ImportError:
	pass

setup(name = 'o3d3xx',
      version = '0.1.0',
      description = 'A Python library for ifm O3D3xx devices, created by Christoph Freundl, fixed by ndyzzjwdx',
      url = 'https://github.com/ndyzzjwdx/o3d3xx-python',
      author = 'ndyzzjwdx',
      author_email = '371974021@qq.com',
      license = 'MIT',
      packages = ['o3d3xx', 'o3d3xx.rpc', 'o3d3xx.pcic'],
      install_requires = ['future'],
      test_suite = 'nose.collector',
      tests_require = ['nose'],
      zip_safe = False)

