import os
CWD = os.environ.get("OPENRAM_TECH") + "/sky130A/tf"
ui().importCds("default", CWD+"/display.drf", CWD+"/mosis.tf", 1000, 1, CWD+"/layers.map")




