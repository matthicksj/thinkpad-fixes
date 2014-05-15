thinkpad-fixes
=========

Fixes for running Fedora 20 on a Thinkpad X1 Carbon.  These are basically helper RPM's for setting up my Thinkpad installation as described here -  http://mattoncloud.org/2014/05/15/fedora-20-on-a-thinkpad-x1-carbon.

These packages are build using tito (https://github.com/dgoodwin/tito).
You must install that first and need a valid RPM build environment as
well.

To build, go into one of the src directories (e.g. thinkpad-fixes) and run:
    tito build

I host the results as a yum repository on OpenShift and you can see the
build.sh script as to how I automate that.

build.sh
-----------

For any updates, you need to commit the work, push it and 'tito tag' it
before running the overall build.  For example, you would do:

    git commit -a -m "My changes"
    tito tag
    git push
    git push --tags

Then you should be safe to run 'build.sh' to upload the results to
OpenShift.

Enjoy! 
