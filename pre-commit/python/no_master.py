#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import subprocess

class TestSuite():

    def __init__(self):
        self.init  = True

    def run(self, files):
        try:
            git_proc = subprocess.Popen(['git', 'symbolic-ref', 'HEAD'], stdout=subprocess.PIPE)
            out, err = git_proc.communicate()
            branch = re.search("refs/heads/master", out.decode('utf-8'))
        except Exception as _excp:
            print(_excp)
        else:
            if branch:
                print("""You can't commit directly to master!
                
Please make a new branch and submit pull request against the master branch from there.

You can create a branch using the following.

git checkout -b your_feature

When you are ready to submit a pull request you should pull the current master branch into your own branch to ensure that it is up to date. You can do that using the following command.

git pull origin master
            
Code review is important, it helps others learn and ensures that you won't be publicly shamed with a git blame when you BREAK THE BUILD.""")
                return 1
            else:
                return 0
        return 0

