![](https://janakiev.com/assets/pelican_jupyter_files/Australian_Pelicans.jpg) Image from [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Australian_Pelicans.jpg)

26 Jul 2019

## Table of Contents

-   [Installation and Quickstart](https://janakiev.com/blog/pelican-jupyter/#installation-and-quickstart)
-   [Installing Themes](https://janakiev.com/blog/pelican-jupyter/#installing-themes)
-   [Writing an Article](https://janakiev.com/blog/pelican-jupyter/#writing-an-article)
-   [Installing Pelican Plugins](https://janakiev.com/blog/pelican-jupyter/#installing-pelican-plugins)
-   [Using Jupyter Notebooks to Write Articles](https://janakiev.com/blog/pelican-jupyter/#using-jupyter-notebooks-to-write-articles)
-   [Hosting Your Blog on GitHub with GitHub Pages](https://janakiev.com/blog/pelican-jupyter/#hosting-your-blog-on-github-with-github-pages)
-   [Conclusion](https://janakiev.com/blog/pelican-jupyter/#conclusion)
-   [Resources](https://janakiev.com/blog/pelican-jupyter/#resources)

Writing articles and tutorials are a great way to learn new things in depth while building a portfolio. In this tutorial, you will find the first steps that you will need to start your data science blog with Pelican and Jupyter Notebooks.

Data Science lives and breathes from communicating your findings, presenting reports and discussing results and new insights. A blog is a great way to engage in this discussion. David Robinson wrote a great [article](http://varianceexplained.org/r/start-blog/) explaining much better how a blog could help you.

## Installation and Quickstart

Pelican runs best with Python 2.7, but you can also use Python 3.3+. To install pelican you need to run:

For more details on the installation, have a look at the [installation guide](http://docs.getpelican.com/en/3.6.3/install.html). After the installation, you are ready to create a Pelican project. First, you need to create the folder for your project and then you can run inside the folder the command:

This should prompt you to add general information for your website.

## Installing Themes

There are many existing themes out there that you can use right away with Pelican. You can find on [Pelican Themes](http://www.pelicanthemes.com/) a whole list of great themes to choose from. To install a theme simply create a folder called themes inside the project folder and inside there you can clone a theme from Github. Here is how you would do that for the [attila](https://github.com/arulrajnet/attila) theme:

Another way would be to use a git submodule if you don’t want to modify the theme:

Now, you just need to add the theme to the configuration file `pelicanconf.py`. There you need to specify the folder of the theme by adding the line:

If you want to create a theme yourself, have a look at this [guide](http://docs.getpelican.com/en/3.6.3/themes.html).

## Writing an Article

Before we get to Jupyter, let’s have a look how writing an article would look like. For this, we can use [Markdown](https://en.wikipedia.org/wiki/Markdown) files with additional metadata. Here is how such an article would look like:

```
Title: This is the Best Tool so far
Date: 2019-06-21 12:00
Category: tools
Tags: tool, software, best
Slug: best-tool
Authors: Jon Doe
Summary: This is the most important tool out there

# Header

You have to learn about this new tool
...
```

Here is a quick rundown of the most common fields:

-   Title: title of the post
-   Slug: path at which the post will be accessed on the server
-   Date: publication date
-   Category: category for the post
-   Tags: space-separated list of tags to use for the post
-   Author: Author of the post
-   Summary: summary of your post

This file needs to be saved in the `content` folder. For more information on how to write content, have a look at the [documentation](http://docs.getpelican.com/en/3.6.3/content.html). To generate the HTML from your Markdown files you can run:

```
pelican content -o output
```

This will generate the whole website in the `output` folder. To view the website, you can launch Pelican’s web server with:

Now you can open the website on `localhost:8000`. If you want to use a different port, you can change `8000` with any other port you want.

## Installing Pelican Plugins

Pelican can be extended with various features for almost any kind of need. You can find most plugins in the [Pelican Plugins](https://github.com/getpelican/pelican-plugins) repository. To add the plugins to your project, you can add it as a [git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules) in the following way:

Many of the plugins are in the form of submodules in this repository, which means that you will find many empty folders. To load those as well, you can load them recursively with:

```
git submodule update --init --recursive
```

Update all submodules to latest commit on origin:

```
git submodule update --remote --merge --recursive
```

Now you can include plugins by adding them to your `pelicanconf.py`. Here is how you would add the [sitemap](https://github.com/getpelican/pelican-plugins/tree/master/sitemap) plugin:

```
# Path to the folder containing the plugins
PLUGIN_PATHS = ['pelican-plugins']
# Enabled plugins
PLUGINS = ['sitemap']
```

Additionally, for the sitemap plugin, you would need to add some configuration:

```
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'always',
        'indexes': 'hourly',
        'pages': 'monthly'
    }
}
```

This would generate a sitemap on the for the URL `BASEURL/sitemap.xml`, where your `BASEURL` would be `localhost:8000` when testing. For more information about Pelican plugins, have a look at the [documentation](http://docs.getpelican.com/en/3.6.3/plugins.html).

## Using Jupyter Notebooks to Write Articles

You’ve seen now how to use Pelican, but you are still wondering how you would use Jupyter Notebooks efficiently with Pelican. There is another great plugin, called [pelican-ipynb](https://github.com/danielfrg/pelican-ipynb) which has got you covered. You will even find this plugin in your `pelican-plugins/` folder. To use it, simply add `pelican-ipynb.markup` to the list of plugins:

```
PLUGINS = ['sitemap', 'pelican-ipynb.markup']
```

Now, you need to add the `.ipynb` to the markup extensions and you need to ignore the `.ipynb_checkpoints/` folder:

```
MARKUP = ('md', 'ipynb')

IGNORE_FILES = [".ipynb_checkpoints"]  
```

Now you can use Jupyter Notebooks instead of Markdown files. There are a couple of ways to add metadata to your notebooks. You can add the metadata in an additional metadata file with the same file name and the same format as in the markdown file but with `.nbdata` extension. Another option is to add the metadata in a cell in the notebook. Before you can do that you need to enable this mode by adding `IPYNB_USE_METACELL = True` to your configuration. Then you can add the metadata in the first notebook cell in markdown mode like this:

```
- title: This is the Best Tool so far
- date: 2019-06-21 12:00
- category: tools
- tags: tool, software, best
- slug: best-tool
- authors: Jon Doe
- summary: This is the most important tool out there
```

Finally, the last way to add metadata is by directly modifying the metadata tag in the raw notebook file. Jupyter Notebooks are stored as JSON documents and inside them, you will find a `"metadata"` tag, where you can add the metadata directly. It is also possible to edit the metadata with Jupyter Notebook. If you are using [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/), you can edit the metadata of the notebooks with the [jupyterlab-nbmetadata](https://github.com/yuvipanda/jupyterlab-nbmetadata) plugin. Make sure to have a look at the [documentation](https://github.com/danielfrg/pelican-ipynb) for more details on how to provide the notebook with metadata.

## Hosting Your Blog on GitHub with GitHub Pages

You can host your website directly on GitHub with [GitHub Pages](https://pages.github.com/). Before we get started, you have to create a repository in GitHub with `username.github.io`, where you should replace `username` with your username on GitHub. After you have set up your website in the previous steps, you can add this repository as a submodule in the output folder:

Additionally, you will need to add `ignore = all` to the `.gitmodules` file in the `[submodule "output"]` section:

Finally, you need to specify in the `publishconf.py` configuration file that you don’t want the `.git` submodule dir to be deleted and to use the correct absolute URL. This can be specified by modifying the file with:

Now you can generate the website and after committing and pushing it, you should find your website ready at `username.github.io` to be filled with content. Note, that it is also possible to use [GitLab Pages](https://about.gitlab.com/product/pages/) too. The steps are mostly pretty much the same.

## Conclusion

You have seen how to create your data science blog using Pelican and Jupyter Notebooks. This is a powerful way to share your projects and articles with others and is additionally a helpful way to learn new topics in more depth. There is another plugin [ipynb2pelican](https://github.com/peijunz/ipynb2pelican), which I haven’t tested but which can also integrate Jupyter notebooks with Pelican.

If anything is unclear or if you have further suggestions, feel free to add them in the comments below.

## Resources

Here are some further resources that might be helpful for you

-   [Pelican Documentation](http://docs.getpelican.com/en/latest/index.html)
-   [Pelican Themes](http://www.pelicanthemes.com/)
-   [Building a Data Science Blog for Your Portfolio](https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/)
-   [Git Tools - Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)