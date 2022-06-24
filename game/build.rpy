## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:
    build.packages = []

    build.package(build.directory_name + "Cross Platform",'zip','windows linux mac renpy mod binary',description="Wintermute - Cross Platform")

    build.package(build.directory_name + "Windows Exclusive",'zip','windows renpy mod binary',description="Wintermute - Windows")
    build.package(build.directory_name + "Mac Exclusive",'zip','mac renpy mod binary',description="Wintermute - Mac")
    build.package(build.directory_name + "Linux Exclusive",'zip','linux renpy mod binary',description="Wintermute - Linux")

    try:
        build.renpy_patterns.remove(build.pattern_list([("renpy.py", "all")])[0])
    except:
        pass

    build.classify_renpy("renpy.py", 'renpy all')

    build.archive("mod_assets", 'mod')
    build.archive("scripts", 'mod')

    build.classify("game/README.txt", None)
    build.classify("game/python-packages/**", "mod all")

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)
    build.classify('**.rpa',None)
    build.classify('CREDITS.txt','mod all')

    # To classify packages for both pc and android, make sure to add all to it like so
    # Example: build.classify("game/**.pdf", "scripts all")
    build.classify("game/mod_assets/**", "mod_assets all")
    build.classify("game/mod_code/**", "scripts all")
    build.classify("**.rpyc", "scripts all")

    build.documentation('CREDITS.txt')