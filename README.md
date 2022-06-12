# Source for http://lj020326.github.io

This repository contains the source for http://lj020326.github.io/.

## Building the Blog

Clone the repository & make sure submodules are included

```
$ git clone https://github.com/lj020326/leeblog.git
$ git checkout src
$ git submodule add https://github.com/getpelican/pelican-plugins.git plugins/pelican-plugins
$ git submodule add git://github.com/danielfrg/pelican-ipynb.git plugins/ipynb
$ git submodule update --init --recursive
```

Install the required packages:

```
$ virtualenv --python=3.5 venv
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


## Troubleshooting
Havent touched this in a while.
Just testing out on macOS machine.

Upon initializing the venv, i bumped into this error:

```
Collecting Markdown==2.6.11
  Using cached Markdown-2.6.11-py2.py3-none-any.whl (78 kB)
Collecting MarkupSafe==1.0
  Using cached MarkupSafe-1.0.tar.gz (14 kB)
  Preparing metadata (setup.py) ... error
  error: subprocess-exited-with-error
  
  × python setup.py egg_info did not run successfully.
  │ exit code: 1
  ╰─> [6 lines of output]
      Traceback (most recent call last):
        File "<string>", line 2, in <module>
        File "<pip-setuptools-caller>", line 34, in <module>
        File "/private/var/folders/w6/3rcdpp211v5cxml6vg45ww3r0000gn/T/pip-install-gm420vm4/markupsafe_05bcf19b93284c609402c55dec367752/setup.py", line 6, in <module>
          from setuptools import setup, Extension, Feature
      ImportError: cannot import name 'Feature' from 'setuptools' (/Users/ljohnson/repos/jekyll/leeblog/venv/lib/python3.8/site-packages/setuptools/__init__.py)
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
(venv) ljohnson@Lees-MBP:[leeblog](src)$ 
```


One issue mentioned pinning setuptools to remedy:

    https://github.com/pypa/setuptools/issues/2017

Removed and reinstalled with version set at 45:

```
pip uninstall setuptools
pip install setuptools==45
```

Tried again - made it further but still more issues.

Leaving on the back-burner now.
Will likely migrate notebooks over to hugo.




