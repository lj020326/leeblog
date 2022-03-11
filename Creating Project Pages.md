The [main difference](https://help.github.com/articles/user-organization-and-project-pages) between a User Page and Project Pages: Project Pages are kept in the same repository as the project, except the **gh-pages** branch is used for Project Pages and the **master** branch is used for a User Page.

Let’s say you are interested in building a Project Page for one of your projects but you would like to keep the files for your project separate from the files used to build the Project Page website. This can easily be done by “orphan”-ing off a **gh-pages** branch of your repository. This is a special type of repository that keeps the files related to your project in the **master** branch, but keeps all the files related to the website in an “orphan”-ed branch called **gh-pages**. This new orphan branch will have no history of all the other branches and commits which allows you to make a new history of all the commits associated with just the Project Page website separate from the actual project itself.

I will create a Project page using Jekyll-Bootstrap for a project with a repository called `coolproject`, except this time I will used `--orphan gh-pages` instead of just changing the name of my **master** branch to **gh-pages** as before (`git branch -m master gh-pages`). I’m assuming there are already files related to the project in `coolproject` which have been committed using `git commit`. Once you checkout the new **gh-pages** branch, you MUST remove everything from that branch before adding the files for the Project Page using `git rm -rf .`.

```
$ cd coolproject
$ git checkout --orphan gh-pages
$ git rm -rf .
```

From there, it’s similar to before. Use `jekyll` directly or `git clone` to copy the files using the GitHub [Jekyll-Bootstrap repository](https://github.com/plusjade/jekyll-bootstrap) or [Karl Broman’s simple site repository](https://github.com/kbroman/simple_site). Make sure to make all the [changes to the files](https://www.stephaniehicks.com/githubPages_tutorial/pages/pages/githubpages-jekyll.html) depending on the way you create your Project Page.

```
$ git clone https://github.com/plusjade/jekyll-bootstrap
$ mv jekyll-bootstrap coolproject
$ cd coolproject
$ rm -rf .git
$ git init 
$ git add .
$ git commit -m "initial project page commit"
```

If you used `jekyll` or `jekyll-bootstrap`, you can quickly view the website as it is locally as it is by running the command in the `coolproject` directory

```
$ jekyll build
$ jekyll serve
```

To view the website locally, go to [http://localhost:4000](http://localhost:4000/). Afterwards you can press ctrl-c to stop the process in the terminal. Otherwise, push everything to GitHub and you should be able to view or special Project Page at `http://username.github.io/coolproject`.

```
$ git remote add origin git@github.com:username/coolproject.git
$ git push -u origin gh-pages
```