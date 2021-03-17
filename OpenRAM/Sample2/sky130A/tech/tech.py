# Created by: ShoanT (taware.shon@gmail.com)
# Saturday 06 March 2021 10∶52∶14 PM
#
import os
from design_rules import *
from module_type import *
from custom_cell_properties import cell_properties
from custom_layer_properties import layer_properties

"""
File containing the process technology parameters for SKY130 
"""

###################################################
# Custom modules
###################################################

# This uses the default classes to instantiate module from
# '$OPENRAM_HOME/compiler/modules'.
# Using tech_modules['cellname'] you can override each class by providing a custom
# implementation in '$OPENRAM_TECHDIR/modules/'
# For example: tech_modules['contact'] = 'contact_scn4m'
tech_modules = module_type()

###################################################
# Custom cell properties
###################################################
cell_properties = cell_properties()

###################################################
# Custom cell properties
###################################################
layer_properties = layer_properties()

###################################################
# GDS file info
###################################################
GDS={}
# gds units
# From http://www.cnf.cornell.edu/cnf_spie9.html: "The first
#is the size of a database unit in user units. The second is the size
#of a database unit in meters.  For example, if your library was
#created with the default units (user unit = 1 m and 1000 database
#units per user unit), then the first number would be 0.001 and the
#second number would be 10-9. Typically, the first number is less than
#1, since you use more than 1 database unit per user unit. To
#calculate the size of a user unit in meters, divide the second number
#by the first."
GDS["unit"]=(0.001,1e-6)
# default label zoom
GDS["zoom"] = 0.5

###################################################
# Interconnect stacks
###################################################

poly_stack = ("poly", "poly_contact", "li")
li_stack = ("li", "li_contact", "m1")
active_stack = ("active", "active_contact", "m1")
m1_stack = ("m1", "via1", "m2")
m2_stack = ("m2", "via2", "m3")
m3_stack = ("m3", "via3", "m4")

layer_indices = {"poly": 0,
                 "active": 0,
                 "li": 1,
                 "m1": 2,
                 "m2": 3,
                 "m3": 4,
                 "m4": 5}

# The FEOL stacks get us up to m1
feol_stacks = [poly_stack,
		li_stack,
               active_stack]

# The BEOL stacks are m1 and up
beol_stacks = [m1_stack,
               m2_stack,
               m3_stack]

layer_stacks = feol_stacks + beol_stacks

preferred_directions = {"poly": "V",
                        "active": "V",
                        "li": "V",
                        "m1": "H",
                        "m2": "V",
                        "m3": "H",
                        "m4": "V"}

###################################################
# Power grid
###################################################
# Use M3/M4
power_grid = m3_stack

###################################################
##GDS Layer Map
###################################################

# create the GDS layer map
layer={}
layer["active"]        = (65, 20)
layer["active_contact"]         = (65, 44)
layer["nwell"]       = (64, 20)
layer["dnwell"]      = (64, 18)
layer["pwbm"]        = (19, 44)
layer["pwde"]        = (124, 20)
layer["natfet"]      = (124, 21)
layer["hvtr"]        = (18, 20)
layer["hvtp"]        = (78, 44)
layer["ldntm"]       = (11, 44)
layer["hvi"]         = (75, 20)
layer["tunm"]        = (80, 20)
layer["lvtn"]        = (125, 44)
layer["poly"]        = (66, 20)
layer["hvntm"]       = (125, 20)
layer["nimplant"]        = (93, 44)
layer["pimplant"]        = (94, 20)
layer["rpm"]         = (86, 20)
layer["urpm"]        = (79, 20)
layer["npc"]         = (95, 20)
layer["poly_contact"]       = (66, 44)
layer["li"]          = (67, 20)
layer["li_contact"]        = (67, 44)
layer["m1"]          = (68, 20)
layer["via1"]         = (68, 44)
layer["m2"]          = (69, 20)
layer["via2"]        = (69, 44)
layer["m3"]          = (70, 20)
layer["via3"]        = (70, 44)
layer["m4"]          = (71, 20)
layer["via4"]        = (71, 44)
layer["m5"]          = (72, 20)
layer["pad"]         = (76, 20)

layer["boundary"]       = (235, 4)

# Layer names for external PDKs
layer_names = {}
layer_names["active"]        = "active"
layer_names["active_contact"]         = "active_contact"
layer_names["nwell"]       = "nwell"
layer_names["dnwell"]      = "dnwell"
layer_names["pwbm"]        = "pwbm"
layer_names["pwde"]        = "pwde"
layer_names["natfet"]      = "natfet"
layer_names["hvtr"]        = "hvtr"
layer_names["hvtp"]        = "hvtp"
layer_names["ldntm"]       = "ldntm"
layer_names["hvi"]         = "hvi"
layer_names["tunm"]        = "tunm"
layer_names["lvtn"]        = "lvtn"
layer_names["poly"]        = "poly"
layer_names["hvntm"]       = "hvntm"
layer_names["nimplant"]    = "nimplant"
layer_names["pimplant"]    = "pimplant"
layer_names["rpm"]         = "rpm"
layer_names["urpm"]        = "urpm"
layer_names["npc"]         = "npc"
layer_names["poly_contact"]       = "poly_contact"
layer_names["li"]          = "li"
layer_names["li_contact"]        = "li_contact"
layer_names["m1"]          = "m1"
layer_names["via1"]         = "via1"
layer_names["m2"]          = "m2"
layer_names["via2"]        = "via2"
layer_names["m3"]          = "m3"
layer_names["via3"]        = "via3"
layer_names["m4"]          = "m4"
layer_names["via4"]        = "via4"
layer_names["m5"]          = "m5"
layer_names["pad"]         = "pad"
layer_names["boundary"]    = "boundary"

###################################################
# DRC/LVS Rules Setup
###################################################
_lambda_ = 1


#technology parameter
parameter={}
parameter["min_tx_size"] = 0.42
parameter["beta"] = 2

# These 6T sizes are used in the parameterized bitcell.
parameter["6T_inv_nmos_size"] = 1.26
parameter["6T_inv_pmos_size"] = 0.55
parameter["6T_access_size"] = 0.42

drclvs_home=os.environ.get("DRCLVS_HOME")

drc = design_rules("sky130A")

#grid size is 1/2 a lambda
drc["grid"]=0.01

#DRC/LVS test set_up
drc["drc_rules"]=None #drclvs_home+"/calibreDRC_scn3me_subm.rul"
drc["lvs_rules"]=None #drclvs_home+"/calibreLVS_scn3me_subm.rul"
drc["layer_map"]=os.environ.get("OPENRAM_TECH")+"/sky130A/tf/layers.map"


###########################################################################

#drc["minwidth_li"] = 4*_lambda_
drc["minwidth_li_contact"] = 0.17

drc.add_layer("li",
              width = 0.17,
              spacing = 0.17)

drc.add_enclosure("li",
                  layer = "poly_contact",
                  enclosure = 0.08)
drc.add_enclosure("li",
                  layer = "li_contact",
                  enclosure = 0)
drc.add_enclosure("m1",
                  layer = "li_contact",
                  enclosure = 0.06)
                  
drc["li_contact_to_li_contact"] = 0.19


###########################################################################



# minwidth_tx with contact (no dog bone transistors)
drc["minwidth_tx"] = 0.42
drc["minlength_channel"] = 0.35

# 1.4 Minimum spacing between wells of different type (if both are drawn)
drc["pwell_to_nwell"] = 0
# 1.3 Minimum spacing between wells of same type (if both are drawn)
# 1.1 Minimum width
drc.add_layer("nwell",
              width = 0.84,
              spacing = 1.27)


drc.add_layer("pwell",
              width = 0,
              spacing = 0)

# 3.1 Minimum width
# 3.2 Minimum spacing over active
drc.add_layer("poly",
              width = 0.15,
              spacing = 0.21)
# 3.3 Minimum gate extension of active
drc["poly_extend_active"] = 0.25 #########################

# 5.5.b Minimum spacing between poly contact and other poly (alternative rules)
drc["poly_to_poly_contact"] = 0.21
# ??
drc["active_enclose_gate"] = 0.0
# 3.5 Minimum field poly to active
drc["poly_to_active"] = 0.075
# 3.2.a Minimum spacing over field poly
#drc["poly_to_field_poly"] = 3*_lambda_

# 2.1 Minimum width
# 2.2 Minimum spacing
drc.add_layer("active",
              width = 0.15,
              spacing = 0.27)

# 2.3 Source/drain active to well edge
drc.add_enclosure("nwell",
                  layer = "active",
                  enclosure = 0.18)
drc.add_enclosure("pwell",
                  layer = "active",
                  enclosure = 0)

# 4.1 Minimum select spacing to channel of transistor to ensure adequate source/drain width
drc["implant_to_channel"] = _lambda_
# 4.2 Minimum select overlap of active
drc.add_enclosure("implant",
                  layer = "active",
                  enclosure = 0)
# 4.3 Minimum select overlap of contact

drc.add_enclosure("implant",
                  layer = "contact",
                  enclosure = 0)
# Not a rule
drc["implant_to_contact"] = 0
# Not a rule
drc.add_layer("implant",
              width = 0,
              spacing = 0)

# 6.1 Exact contact size
# 5.3 Minimum contact spacing
drc.add_layer("active_contact",
              width = 0.15,
              spacing = 0.27)
# 6.2.b Minimum active overlap
drc.add_enclosure("active",
                  layer = "active_contact",
                  enclosure = 0)
drc.add_enclosure("active",
                  layer = "poly_contact",
                  enclosure = 0)
# Reserved for other technologies
drc["active_contact_to_gate"] = _lambda_
# 5.4 Minimum spacing to gate of transistor
drc["poly_contact_to_gate"] = 0.19

# 6.1 Exact contact size
# 5.3 Minimum contact spacing
drc.add_layer("poly_contact",
              width = 0.17,
              spacing = 0.17)
drc["minwidth_poly_contact"] = 0.17    
drc["minwidth_via1"] = 0.26    
drc["via1_to_via1"] = 0.06    

drc.add_enclosure("npc",
                  layer = "poly",
                  enclosure = 0.025) ######## Confirm value | Added temporary value

# 8.3 Minimum overlap by m1
drc.add_enclosure("m1",
                  layer = "via1",
                  enclosure = 0.03)

              
# 5.2.b Minimum poly overlap
drc.add_enclosure("poly",
                  layer = "poly_contact",
                  enclosure = 0.08)
# Reserved for other technologies
#drc["poly_contact_to_gate"] = 2*_lambda_
# 5.4 Minimum spacing to gate of transistor
#drc["poly_contact_to_poly"] = 2*_lambda_

# 7.1 Minimum width
# 7.2 Minimum spacing
drc.add_layer("m1",
              width = 0.14,
              spacing = 0.14)
# 7.3 Minimum overlap of any contact
'''
drc.add_enclosure("m1",
                  layer = "poly_contact",
                  enclosure = _lambda_)
'''
drc.add_enclosure("m1",
                  layer = "active_contact",
                  enclosure = _lambda_)

# 8.1 Exact size
# 8.2 Minimum via spacing
drc.add_layer("via1",
              width = 0.26,
              spacing = 0.03)

# 9.1 Minimum width
# 9.2 Minimum spacing
drc.add_layer("m2",
              width = 0.14,
              spacing = 0.14)
# 9.3 Minimum overlap of via
drc.add_enclosure("m2",
                  layer = "via1",
                  enclosure = 0.03)
# 14.3 Minimum overlap by m2
drc.add_enclosure("m2",
                  layer = "via2",
                  enclosure = 0.045)

# 14.1 Exact size
# 14.2 Minimum spacing
drc.add_layer("via2",
              width = 0.28,
              spacing = 0.12)

# 15.1 Minimum width
# 15.2 Minimum spacing to m3
drc.add_layer("m3",
              width = 0.30,
              spacing = 0.30)

# 15.3 Minimum overlap of via 2
drc.add_enclosure("m3",
                  layer = "via2",
                  enclosure = 0.025)

# 21.3 Minimum overlap by m3
drc.add_enclosure("m3",
                  layer = "via3",
                  enclosure = 0.03)

# 21.1 Exact size
# 21.2 Minimum spacing
drc.add_layer("via3",
              width = 0.32,
              spacing = 0.08)

# 22.1 Minimum width
# 22.2 Minimum spacing to m4
drc.add_layer("m4",
              width = 0.30,
              spacing = 0.30)

# 22.3 Minimum overlap of via 3
drc.add_enclosure("m4",
                  layer = "via3",
                  enclosure = 0.005)

###################################################
# Spice Simulation Parameters
###################################################

# spice model info
spice={}
spice["nmos"]="sky130_fd_pr__nfet_01v8"
spice["pmos"]="sky130_fd_pr__nfet_01v8"
# This is a map of corners to model files
SPICE_MODEL_DIR=os.environ.get("SPICE_MODEL_DIR")
spice["fet_models"] = {"TT": [SPICE_MODEL_DIR + "/tt.sp"],
                       "FF": [SPICE_MODEL_DIR + "/ff.sp"],
                       "FS": [SPICE_MODEL_DIR + "/ff.sp"],
                       "SF": [SPICE_MODEL_DIR + "/ss.sp"],
                       "SS": [SPICE_MODEL_DIR + "/ss.sp"],
                       "ST": [SPICE_MODEL_DIR + "/ss.sp"],
                       "TS": [SPICE_MODEL_DIR + "/tt.sp"],
                       "FT": [SPICE_MODEL_DIR + "/ff.sp"],
                       "TF": [SPICE_MODEL_DIR + "/tt.sp"],
                       }


#spice stimulus related variables
spice["feasible_period"] = 10         # estimated feasible period in ns
spice["supply_voltages"] = [4.5, 5.0, 5.5]  # Supply voltage corners in [Volts]
spice["nom_supply_voltage"] = 5.0    # Nominal supply voltage in [Volts]
spice["rise_time"] = 0.05            # rise time in [Nano-seconds]
spice["fall_time"] = 0.05            # fall time in [Nano-seconds]
spice["temperatures"] = [0, 25, 100]  # Temperature corners (celcius)
spice["nom_temperature"] = 25        # Nominal temperature (celcius)

# analytical delay parameters
spice["nom_threshold"] = 1.3   # Nominal Threshold voltage in Volts
# FIXME: These need to be updated for SCMOS, they are copied from FreePDK45.
spice["wire_unit_r"] = 0.075    # Unit wire resistance in ohms/square
spice["wire_unit_c"] = 0.64     # Unit wire capacitance ff/um^2
spice["min_tx_drain_c"] = 0.7   # Minimum transistor drain capacitance in ff
spice["min_tx_gate_c"] = 0.1    # Minimum transistor gate capacitance in ff
spice["dff_setup"] = 9        # DFF setup time in ps
spice["dff_hold"] = 1         # DFF hold time in ps
spice["dff_in_cap"] = 9.8242  # Input capacitance (D) [Femto-farad]
spice["dff_out_cap"] = 2       # Output capacitance (Q) [Femto-farad]

# analytical power parameters, many values are temporary
spice["bitcell_leakage"] = 1     # Leakage power of a single bitcell in nW
spice["inv_leakage"] = 1         # Leakage power of inverter in nW
spice["nand2_leakage"] = 1       # Leakage power of 2-input nand in nW
spice["nand3_leakage"] = 1       # Leakage power of 3-input nand in nW
spice["nand4_leakage"] = 1       # Leakage power of 4-input nand in nW
spice["nor2_leakage"] = 1        # Leakage power of 2-input nor in nW
spice["dff_leakage"] = 1      # Leakage power of flop in nW

spice["default_event_frequency"] = 100         # Default event activity of every gate. MHz

# Logical Effort relative values for the Handmade cells
parameter["le_tau"] = 18.17                  # In pico-seconds.
parameter["min_inv_para_delay"] = 2.07       # In relative delay units
parameter["cap_relative_per_ff"] = .91       # Units of Relative Capacitance/ Femto-Farad
parameter["dff_clk_cin"] = 27.5              # In relative capacitance units
parameter["6tcell_wl_cin"] = 2               # In relative capacitance units
parameter["sa_en_pmos_size"] = 12 * _lambda_
parameter["sa_en_nmos_size"] = 4 * _lambda_
parameter["sa_inv_pmos_size"] = 12 * _lambda_
parameter["sa_inv_nmos_size"] = 4 * _lambda_
parameter["bitcell_drain_cap"] = 0.2        # In Femto-Farad, approximation of drain capacitance

###################################################
# Technology Tool Preferences
###################################################

drc_name = "magic"
lvs_name = "netgen"
pex_name = "magic"

blackbox_bitcell = False
