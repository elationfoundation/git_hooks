#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import sys

def main():
    all_files = False
    if len(sys.argv) > 1 and sys.argv[1] == '--all-files':
        all_files = True
    files = stash_uncommitted(all_files)
    result  = run_checks(files)
    #unstash_uncommitted()
    sys.exit(result)


def stash_uncommitted(all_files):
    """
    Stashes away changes to the working tree that wont be committed.
    """
    # Stash any changes to the working tree that are not going to be committed
    #subprocess.call(['git', 'stash', '-u', '--keep-index'], stdout=subprocess.PIPE)
    
    files = []
    if all_files:
        for root, dirs, file_names in os.walk('.'):
            for file_name in file_names:
                files.append(os.path.join(root, file_name))
    else:
        #get clean list of files
        p = subprocess.Popen(['git', 'status', '--porcelain'], stdout=subprocess.PIPE)
        out, err = p.communicate()
        for line in out.splitlines():
            match = modified.match(line)
            if match:
                pritn(match)
                files.append(match.group('name'))
    return files
    
def run_checks(files):
    """
    Gets the directory of the pre-commit file and then runs the auto-built "run_tests" shell file in the same directory.
    """
    result = 0
    check_dir = os.path.dirname(os.path.realpath(__file__))
    for _file in files:
        print(_file)
        p = subprocess.Popen([check_dir+'/run_tests.sh', "-f", str(_file)], stdout=subprocess.PIPE)
    out, result = p.communicate()
    return result

def unstash_uncommitted():
    # Unstash changes to the working tree
    # https://stackoverflow.com/questions/20479794/how-do-i-properly-git-stash-pop-in-pre-commit-hooks-to-get-a-clean-working-tree
    subprocess.call(['git', 'reset', '--hard'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.call(['git', 'stash', 'pop', '--quiet', '--index'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


if __name__ == '__main__':
    main()

