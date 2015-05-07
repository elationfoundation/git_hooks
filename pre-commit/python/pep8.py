#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import re

class TestSuite():
    def __init__(self):
        self.init = True

    def run(self, files):
        try:
            self.pep_loaded = self.check_program("pep8")
        except Exception as _excp:
            print(_excp)
        if not self.pep_loaded:
            print("You need pep8 to run this pre-commit hook. Please run 'apt-get install pep8' to install it.")
            return 0
        err = 0
        result = 0
        for file_name in files:
            try:
                result = self.check_pep(file_name) or 0
            except Exception as _ee:
                print(_ee)
            if result == 1:
                err = 1
        return err
        
    def system(self, *args, **kwargs):
        kwargs.setdefault('stdout', subprocess.PIPE)
        proc = subprocess.Popen(args, **kwargs)
        out, err = proc.communicate()
        return out

    def check_program(self, name):
        for dir in os.environ['PATH'].split(':'):
            prog = os.path.join(dir, name)
            if os.path.exists(prog):
                return prog
        return None

    def check_pep(self, file_name):
        # watching python and lua scripts
        output = None
        if re.search(r"(\.py)$", file_name):
            # current script text
            with open(file_name, 'r') as fd: script = fd.read()
            # change modification date
            try:
                output = self.system('pep8', file_name)
            except Exception as __ee:
                print(__ee)
        if output:
            print(output.decode("utf-8"))
            return 1
        return 0        
