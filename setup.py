from setuptools import setup, find_packages


setup(
        name = 'myPackages',
        version = '0.1',
        packages = find_packages(exclude = ['tests*']),
        license = 'MIT',
        description = 'My First Python Package',
        long_description = open('README.md').read(),  
        install_requires = ['numpy'],
        url = 'https://github.com/troyecks/myPackages',
        author = 'Chukwunta Chibueze',
        author_email = 'chukwuntachibueze@gmail.com'




)