# About
This is the Personal documentaion for Tatsuya Osaki

To edit this documentation, you need sphinx pyhon package and markdown format. Please follow these instruction to set up the enviroment for editing markdown and sphinx document convertion.
## Installation of sphinx

### Sphinx + extensions

Sphinx was initially developped to document Python sources but can also applied to several other sources thanks to extensions.
Mainly based on the used of [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html) (or Markdown with extensions) it allows the generation of html documentation easily. Using the autodoc function, documentation is generated from the docstrings in sources. Since it is Python based, package managing for installation as well as extensions are simple and port well.

This is the installtion with conda package manager

```Bash
conda create -n sphinx
conda activate sphinx
conda install -c anaconda sphinx 

pip install sphinx-rtd-theme
pip install myst-parser
pip install sphinx-autobuild
pip install sphinx-rtd-theme
pip install furo
pip install pydata-sphinx-theme
conda install pydata-sphinx-theme --channel conda-forge
pip install sphinx-favicon
```
Then, set the theme
```Bash
html_theme = "pydata_sphinx_theme"
#html_theme = 'alabaster'
#html_theme = 'sphinx_rtd_theme'
#html_theme = 'furo'
```
> [Pydata_sphinx_theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/web-components.html#)
> 
> [Basic syntax Markdonw guite](https://www.markdownguide.org/basic-syntax/)
> 
> [Sphinx design](https://sphinx-design.readthedocs.io/en/latest/index.html)

Then, to make html build

```Bash
sphinx-build source docs
or
sphinx-autobuild source docs
```

Setting of this documentation can be edit
```Bash
con.py
```
