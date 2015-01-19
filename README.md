# cython-example
Example code exploring issues with distributing cython code

The code consists of several version illustrating errors or problems that I blundered through. Each version is tagged
and this Readme is (almost) correctly updated for each example.

**I recommend that you use python virtual environments to install this code so that you have a fresh environment each time
and you don't mess up your working install of Python.**

# ex1
The module installs without errors, but because of me not indicating the paths of the cython files properly (I omit the
``kgcyex`` directory in the path) the cython files do not compile. You will note this because there are no compilation
messages during the install, though the failure is otherwise silent

    kghose$ kgcyex
    Traceback (most recent call last):
      File "/Users/kghose/.venvs/blog/bin/kgcyex", line 9, in <module>
        load_entry_point('kgcyex==1.0.0', 'console_scripts', 'kgcyex')()
      File "/Users/kghose/.venvs/blog/lib/python2.7/site-packages/pkg_resources.py", line 356, in load_entry_point
        return get_distribution(dist).load_entry_point(group, name)
      File "/Users/kghose/.venvs/blog/lib/python2.7/site-packages/pkg_resources.py", line 2431, in load_entry_point
        return ep.load()
      File "/Users/kghose/.venvs/blog/lib/python2.7/site-packages/pkg_resources.py", line 2147, in load
        ['__name__'])
      File "/Users/kghose/.venvs/blog/lib/python2.7/site-packages/kgcyex/main.py", line 2, in <module>
        import kgcyex.cy1 as cy1
    ImportError: No module named cy1


#ex2
I correctly write out the full paths of the cython modules, and everything installs and runs fine.

    kghose$ kgcyex
    foo from kgcyex.mod1
    foo from kgcyex.cy1
    foo from kgcyex.lib.mod2
    foo from kgcyex.lib.cy2
    
#ex3
Suppose the other user does not have Cython? The [cython documentation][1] suggests that we distribute the generated c code
with the source. There is some debate as to whether this is "proper" since the .c files are actually generated from the
.pyx files and in principle we should only really be distributing files which can not be auto-generated from the "real" 
source. For now, we put pragmatism over principle. Note that the ``setup.py`` changes a bit

[1]: http://docs.cython.org/src/reference/compilation.html#distributing-cython-modules

If you read the setup.py you will note that I have used a check to test if the user has Cython or not. This check then
tells setup to either use the .pyx files or the .c files. This is standard stuff recommended by the Cython folks. Look
carefully at the ``setup.py`` where I add the extensions. 

    extensions = [Extension("cy1", ["kgcyex/cy1"+ext]), Extension("cy2", ["kgcyex/lib/cy2"+ext])]

Things compile properly because I've remembered to indicate the peoper path to the ``.pyx`` (or ``.c``) files. When we run
``setup.py`` we can see the modules being compiled. But what the #$%@! when we go to run the code it again complains that it
can find the compiled modules! In real life this error caused me to lose about an hour :(

My error was that though I had correctly indicated the path to the source (the second parameter for ``Extension``) I had
not given the proper dotted path for the modules themselves. If you look under ``site-packages`` of your installation
you will note that there are two compiled modules ``cy1.so`` and ``cy2.so`` directly under ``site-packages`` rather than
in their proper places under ``kgcyex`` and ``kgcyex/lib``. The correct form of this line is ...

#ex4

    extensions = [Extension("kgcyex.cy1", ["kgcyex/cy1"+ext]), Extension("kgcyex.lib.cy2", ["kgcyex/lib/cy2"+ext])]
    
