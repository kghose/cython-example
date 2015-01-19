# cython-example
Example code exploring issues with distributing cython code

The code consists of several version illustrating errors or problems that I blundered through. Each version is tagged
and this Readme is (almost) correctly updated for each example.

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