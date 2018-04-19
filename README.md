# Source for http://jakevdp.github.io

This repository contains the source for http://jakevdp.github.io/.

## Building the Blog

Clone the repository & make sure submodules are included

```
$ git clone https://github.com/lj020326/lj020326.github.io-source.git
$ git submodule add https://github.com/getpelican/pelican-plugins.git plugins/pelican-plugins
$ git submodule add git://github.com/danielfrg/pelican-ipynb.git plugins/ipynb
$ git submodule update --init --recursive
```

Install the required packages:

```
$ virtualenv python=3.5 venv
$ source activate venv
$ pip install -r requirements.txt
```

Build the html and serve locally:

```
$ make html
$ make serve
$ open http://localhost:8000
```

Deploy to github pages

```
$ make publish-to-github
```
