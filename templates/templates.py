PACKAGE = \
"""import fire

def main():
    fire.Fire(Toolname)

class Toolname:

    def ur_command(self, param):
        ...
    
    
    def test(self):
        print('test method')
        ...


if __name__ == '__main__':
    main()
"""



SETUP =\
"""from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tool_name',
    version='1.0.0',
    author='Your Name',
    author_email='your@gmail.com',
    description='short synopsis of your tool',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/tool_name',
    py_modules=['tool_name.tool_name'], # example: ['tipytools.tipytools']
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'fire',
        # Add any other dependencies required by your tool
    ],
    entry_points='''
        [console_scripts]
        # tipy=tipytools.tipytools:main
        tool_name=tool_name.tool_name:main
    ''',
)
"""


README =\
"""# Tool name


```shell

```

- author: Your Name
- version: 1.0.0
"""