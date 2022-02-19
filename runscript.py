#!/usr/bin/python3

import sys
# Execute shell commands.
def runscript(script):
    if sys.version_info[0]<3:
        import commands
        result = commands.getstatusoutput(script).split("\n")
    else:
        import subprocess
        result = subprocess.getoutput(script).split("\n")
    return result
