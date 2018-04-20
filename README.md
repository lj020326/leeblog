# Source for http://lj020326.github.io

This repository contains the source for http://lj020326.github.io/.

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

Make, test and/or publish your contents

```
# Generate Site
make html

# Start test webserver on localhost
# Then, go to address localhost:8000 in your browser.
make serve

# Instead of repeating the above 2 steps 
# you can run "Generate + test"
# This will automatically regenerate html instantly after any changes made to src.
make devserver

# Deploy to github page
make github
```

