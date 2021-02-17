# Created by: ShonT
# On: 16/02/2021 10:06:10
#
#!/usr/bin/python

import sys
import os

TECHNOLOGY = "sky130A"

os.environ["MGC_TMPDIR"] = "/tmp"

# OpenRAM Paths
try:
    DRCLVS_HOME = os.path.abspath(os.environ.get("DRCLVS_HOME"))
except:
    OPENRAM_TECH=os.path.abspath(os.environ.get("OPENRAM_TECH"))
    DRCLVS_HOME=OPENRAM_TECH+"/sky130A/tech"
os.environ["DRCLVS_HOME"] = DRCLVS_HOME

os.environ["SPICE_MODEL_DIR"] = "{0}/models".format(os.path.dirname(__file__))

