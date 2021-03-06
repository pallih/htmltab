from setuptools import setup


setup(name="htmltab",
      version="0.1.0-pre",
      description="A command-line utility that converts an HTML table into "
                  "CSV data",
      long_description=open("README.rst").read(),
      url="https://github.com/flother/htmltab",
      license="MIT",
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Natural Language :: English",
          "Programming Language :: Python :: 3",
          "Topic :: Utilities",
      ],
      py_modules=["htmltab"],
      entry_points={
          "console_scripts": ["htmltab=htmltab:main"],
      },
      install_requires=[
          "beautifulsoup4>=4.3.2",
          "click>=6.0",
          "lxml>=3.2.0",
          "cssselect>=0.9.1",
      ])
