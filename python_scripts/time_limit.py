#!/usr/bin/python

import os
import time
import subprocess
from datetime import datetime

f  = os.listdir("/proj/3hr_limit/")
p = "/proj/3hr_limit/"
g = "/proj/tmp_arch/"
now = time.time()
diff_hours = now - 3 * 3600

print "Searching for files 3 hours or older........"
for old_file in f:
    file_age = os.stat("/proj/3hr_limit/"+old_file).st_mtime
    if file_age < diff_hours:
        subprocess.call(["tar", "-cvf", g+old_file+".tar", p+old_file])
        print old_file+" is 3 hours or older"
        subprocess.call(["rm", p+old_file])
        print old_file+" has been removed from " + p + "and moved to "+ g
    else:
        print old_file+" isn't 3 hours or older"
print "Search complete... No files meet the criteria"
