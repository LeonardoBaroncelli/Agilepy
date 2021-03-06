***********
Development
***********

Git flow after v1.0.0
=====================

Theory
------

Branches
^^^^^^^^

Two main branches:

* **master**: contains only production releases.
* **develop**: contains commits that will be included in the next production release.

Two support branches:

* **feature** branch: each new feature (Trello's card) should be developed in its own feature branch, branching from **develop** and merged back into it. The **feature** branch are not pushed into the remote.
* **hotfix** branch: if an hotfix is needed it should be develop in its own branch, branching from **master** and merged back to it.

.. image:: static/gitflow.png
  :width: 600
  :alt: Git flow


Versioning
^^^^^^^^^^
The **master** branch contains only production releases: when the **develop** branch (or **hotfix** branch) is merged
to **master** a new release tag must be created. Its name follows the `semantic versioning <https://semver.org/>`_.

    x.y.z

Incrementing:

* x version when you make incompatible API changes,
* y version when you add functionality in a backwards compatible manner, and
* z version when you make backwards compatible bug fixes.


Branches names
^^^^^^^^^^^^^^

The **master** and the **develop** branch have an infinite lifetime, hence their name is fixed.

The **feature** branch takes the following format:

    feature-#<card-number>-<short-description>

e.g. feature-#61-bayesian-blocks

The **hotfix** branch name takes the following format:

    hotfix-#<card-number>-<release-number>

e.g. hotfix-#57-1.0.0


The release number is the one of the production release from which it originates from.

Practice
--------

Development of a new feature
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you start from scratch:
::

    git clone --single-branch --branch develop https://github.com/AGILESCIENCE/Agilepy.git

Creating a new **feature** branch:
::

    git checkout develop
    git pull origin develop
    git checkout -b feature-#61-bayesian-blocks develop



Development and testing of the new feature. Then, CHANGELOG.md update and merging back to **develop** branch.

::

    vim CHANGELOG
    git commit -m ""
    git checkout develop
    git merge --no-ff feature-#61-bayesian-blocks
    git branch -d feature-#61-bayesian-blocks
    git push origin develop


Release of a new version
^^^^^^^^^^^^^^^^^^^^^^^^

Change the version of the software in setup.py. The version increment must be take
in account all the commits of the **develop** branch. You can check the CHANGELOG.md
to facilitate this process.

::

    git checkout master
    git merge --no-ff develop
    git tag -a <new-tag>
    git push origin <new-tag>

Git flow before v1.0.0
======================

Clone the following repository:
::

    cd
    git clone https://github.com/AGILESCIENCE/Agilepy/
    cd Agilepy


Activate the anaconda virtual environment:
::

    conda activate <env_name>


Export the following environment variable:
::

    export PYTHONPATH=.


Update the source, then commit and push on origin/master.

If you want your modification to be included into the anaconda package you need to

- delete the remote v1.0.0 tag
- delete the local v1.0.0 tag
- create a new v1.0.0 tag, pointing to the last commit
- push the commit and the tag on the master branch

::

    git push --delete origin v1.0.0
    git tag -d v1.0.0
    git tag v1.0.0 $(git log --format="%H" -n 1)
    git push origin master --tags
