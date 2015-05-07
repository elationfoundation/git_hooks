#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import subprocess
from datetime import datetime

class TestSuite():
    def __init__(self):
        self.stdout = 0

    def run(self, files):
        for file_name in files:
            try:
                self.set_changed(file_name)
            except Exception as _ee:
                print(_ee)
        print("Completed time stamping")
        return 0
        
    def system(self, *args, **kwargs):
        kwargs.setdefault('stdout', subprocess.PIPE)
        proc = subprocess.Popen(args, **kwargs)
        out, err = proc.communicate()
        return out

    def current_time(self):
        """Current date-time"""
        return datetime.now().strftime('%Y-%m-%d %H:%M')

    def set_changed(self, file_name):
        # watching python and lua scripts
        if re.search(r"(\.py|\.lua)$", file_name):
            # current script text
            with open(file_name, 'r') as fd: script = fd.read()
            # change modification date
            try:
                _now = self.current_time()
                print(_now)
                script = re.sub('(@changed\s*:\s+)\d{4}-\d{2}-\d{2} \d{2}:\d{2}', lambda m: m.group(1) + _now, script)
            except Exception as __ee:
                print(__ee)
            # write back to script
            with open(file_name, 'w') as fd: fd.write(script)
            # add changes to commit
            try:
                print(file_name+"'s timestamp updated")
                self.system('git', 'add', file_name)
            except Exception as _ee:
                print(_ee)
        return 0
        
