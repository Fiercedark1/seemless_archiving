#!/usr/bin/python

import os
import time
import subprocess
from datetime import datetime

f  = os.listdir("/proj/tmp_arch/")
g = "/proj/3hr_limit/"
p = "/proj/tmp_arch/"
now = time.time()
three_hours = now - 3 * 3600

print "Searching for tar files 3 hours or older........"
for tar_file in f:
    file_age = os.stat("/proj/tmp_arch/"+tar_file).st_mtime
    if file_age < three_hours:
        subprocess.call(["tar", "-xvzf", p+tar_file, "-C", g+tar_file])
        print "%s is 3 hours or older" % (tar_file)
        subprocess.call(["rm", p+tar_file])
        print "%s has been removed from " + p + "and moved to "+ g % (tar_file)
    else:
        print "%s isn't 3 hours or older" % (tar_file)
print "Search complete... No files meet the criteria"        
