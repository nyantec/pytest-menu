from setuptools import setup

setup(
     name="pytest-menu",
     version='0.0.4',
     description='A pytest plugin for console based interactive test selection'
                 ' just after the collection phase',
     license='MIT',
     author='Karl Engelhardt',
     author_email='ken@nyantec.com',
     url='https://github.com/nyantec/pytest-menu',
     download_url='https://github.com/nyantec/pytest-menu/tarball/0.0.4',
     platforms=['linux'],
     packages=['menu'],
     entry_points={'pytest11': [
         'menu = menu.plugin'
     ]},
     zip_safe=False,
     install_requires=['pytest>=2.4.2', 'npyscreen>=4.0'],
     classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3',
        'Environment :: Console',
     ],
)
