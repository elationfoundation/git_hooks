#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import string

class CodeGen:
    """
    a Python code generator backend
    fredrik lundh, march 1998
    fredrik@pythonware.com
    http://www.pythonware.com
    """
    
    def begin(self, tab="\t"):
        self.code = []
        self.tab = tab
        self.level = 0

    def end(self):
        return string.join(self.code, "")

    def write(self, string):
        self.code.append(self.tab * self.level + string)

    def indent(self):
        self.level = self.level + 1 

    def dedent(self):
        if self.level == 0:
            raise SyntaxError, "internal error in code generator"
        self.level = self.level - 1



def main(directory, test_file, script):
    """
    """
    
def build_test():
    c = CodeGen()
    c.begin(tab="    ")
    #==============CODE TO WRITE===================
    import TEST_FILE

    test = TEST_FILE.TestSuite()

    result = 0
    
    for FILE in FILES:
        result = test.run(FILE) or 0
        if result == 1:
            err = 1

    if err != 1:
        err = result

    exit(result)
        
        
    
    
    #create object out of test file
    
    #test all files passed to us
    #return result to tester.

    #===============================================
    c.write("")

def get_args():
    """
    Argument parser for Command line use
    """
    parser = argparse.ArgumentParser(description='openThreads')
    parser.add_argument("-t", "--test-file", nargs="?", default=None, const=None, dest="test_file", metavar="TESTFILE", help="Specify the path to the test file to add to")
    parser.add_argument("-d", "--hook-directory", nargs="?", default=None, const=None, dest="hook_dir", metavar="HOOKS", help="Specify path to the .git/hooks directory")
    parser.add_argument("-s", "--script", nargs="?", default=None, const=None, dest="script", metavar="SCRIPT", help="Specify the path to the script to run the test from")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = get_args()
    main(args.hook_dir, args.test_file, args.script)
