# See LICENSE for licensing information.
#
# Copyright (c) 2016-2019 Regents of the University of California and The Board
# of Regents for the Oklahoma Agricultural and Mechanical College
# (acting for and on behalf of Oklahoma State University)
# All rights reserved.
#
import os
from design_rules import *
from module_type import *
from custom_cell_properties import cell_properties
from custom_layer_properties import layer_properties

"""
File containing the process technology parameters for SCMOS 4m, 0.35um
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

poly_stack = ("poly", "licon", "m1")
active_stack = ("active", "tap", "m1")
m1_stack = ("m1", "via", "m2")
m2_stack = ("m2", "via2", "m3")
m3_stack = ("m3", "via3", "m4")

layer_indices = {"poly": 0,
                 "active": 0,
                 "m1": 1,
                 "m2": 2,
                 "m3": 3,
                 "m4": 4}

# The FEOL stacks get us up to m1
feol_stacks = [poly_stack,
               active_stack]

# The BEOL stacks are m1 and up
beol_stacks = [m1_stack,
               m2_stack,
               m3_stack]

layer_stacks = feol_stacks + beol_stacks

preferred_directions = {"poly": "V",
                        "active": "V",
                        "m1": "H",
                        "m2": "V",
                        "m3": "H",
                        "m4": "V"}

###################################################
# Power grid
###################################################
# Use M3/M4
power_grid = m1_stack

###################################################
##GDS Layer Map
###################################################

# create the GDS layer map
layer={}
layer["diff"]        = (65, 20)
layer["tap"]         = (65, 44)
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
layer["nsdm"]        = (93, 44)
layer["psdm"]        = (94, 20)
layer["rpm"]         = (86, 20)
layer["urpm"]        = (79, 20)
layer["npc"]         = (95, 20)
layer["licon"]       = (66, 44)
layer["li"]          = (67, 20)
layer["mcon"]        = (67, 44)
layer["m1"]          = (68, 20)
layer["via"]         = (68, 44)
layer["m2"]          = (69, 20)
layer["via2"]        = (69, 44)
layer["m3"]          = (70, 20)
layer["via3"]        = (70, 44)
layer["m4"]          = (71, 20)
layer["via4"]        = (71, 44)
layer["m5"]          = (72, 20)
layer["via5"]        = (72, 44)
layer["boundary"]        = (72, 44)
layer["pad"]         = (76, 20)

#layer["text"]   = (83, 44)
#layer["boundary"] = (81, 4)

# Layer names for external PDKs
layer_names = {}
layer["diff"]        = "active"
layer["tap"]         = "tap"
layer["nwell"]       = "nwell"
layer["dnwell"]      = "dnwell"
layer["pwbm"]        = "pwbm"
layer["pwde"]        = "pwde"
layer["natfet"]      = "natfet"
layer["hvtr"]        = "hvtr"
layer["hvtp"]        = "hvtp"
layer["ldntm"]       = "ldntm"
layer["hvi"]         = "hvi"
layer["tunm"]        = "tunm"
layer["lvtn"]        = "lvtn"
layer["poly"]        = "poly"
layer["hvntm"]       = "hvntm"
layer["nimplant"]        = "nsdm"
layer["pimplant"]        = "psdm"
layer["rpm"]         = "rpm"
layer["urpm"]        = "urpm"
layer["npc"]         = "npc"
layer["licon"]       = "licon"
layer["li"]          = "li"
layer["mcon"]        = "mcon"
layer["m1"]          = "m1"
layer["via"]         = "via"
layer["m2"]          = "m2"
layer["via2"]        = "via2"
layer["m3"]          = "m3"
layer["via3"]        = "via3"
layer["m4"]          = "m4"
layer["via4"]        = "via4"
layer["m5"]          = "m5"
layer["via5"]        = "via5"
layer["boundary"]        = "boundary"
layer["pad"]         = "pad"

###################################################
# DRC/LVS Rules Setup
###################################################
_lambda_ = 0.5

#technology parameter
parameter={}
parameter["min_tx_size"] = 4*_lambda_
parameter["beta"] = 2

# These 6T sizes are used in the parameterized bitcell.
parameter["6T_inv_nmos_size"] = 8*_lambda_
parameter["6T_inv_pmos_size"] = 3*_lambda_
parameter["6T_access_size"] = 4*_lambda_

drclvs_home=os.environ.get("DRCLVS_HOME")

drc = design_rules("sky130")

#grid size is 1/2 a lambda
drc["grid"]=0.5*_lambda_

#DRC/LVS test set_up
drc["drc_rules"]=None #drclvs_home+"/calibreDRC_scn3me_subm.rul"
drc["lvs_rules"]=None #drclvs_home+"/calibreLVS_scn3me_subm.rul"
drc["layer_map"]=os.environ.get("OPENRAM_TECH")+"/scn3me_subm/layers.map"

# minwidth_tx with contact (no dog bone transistors)
drc["minwidth_tx"] = 4*_lambda_
drc["minlength_channel"] = 2*_lambda_

# 1.4 Minimum spacing between wells of different type (if both are drawn)
drc["pwell_to_nwell"] = 0
# 1.3 Minimum spacing between wells of same type (if both are drawn)
# 1.1 Minimum width
drc.add_layer("nwell",
              width = 12*_lambda_,
              spacing = 6*_lambda_)
drc.add_layer("pwell",
              width = 12*_lambda_,
              spacing = 6*_lambda_)

# 3.1 Minimum width
# 3.2 Minimum spacing over active
drc.add_layer("poly",
              width = 2*_lambda_,
              spacing = 3*_lambda_)
# 3.3 Minimum gate extension of active
drc["poly_extend_active"] = 2*_lambda_
# 5.5.b Minimum spacing between poly contact and other poly (alternative rules)
drc["poly_to_contact"] = 4*_lambda_
# ??
drc["active_enclose_gate"] = 0.0
# 3.5 Minimum field poly to active
drc["poly_to_active"] = _lambda_
# 3.2.a Minimum spacing over field poly
drc["poly_to_field_poly"] = 3*_lambda_

# 2.1 Minimum width
# 2.2 Minimum spacing
drc.add_layer("active",
              width = 3*_lambda_,
              spacing = 4*_lambda_)

# 2.3 Source/drain active to well edge
drc.add_enclosure("nwell",
                  layer = "active",
                  enclosure = 6*_lambda_)
drc.add_enclosure("pwell",
                  layer = "active",
                  enclosure = 6*_lambda_)

# 4.1 Minimum select spacing to channel of transistor to ensure adequate source/drain width
drc["implant_to_channel"] = 3*_lambda_
# 4.2 Minimum select overlap of active
drc.add_enclosure("implant",
                  layer = "active",
                  enclosure = 2*_lambda_)
# 4.3 Minimum select overlap of contact
drc.add_enclosure("implant",
                  layer = "contact",
                  enclosure = _lambda_)
# Not a rule
drc["implant_to_contact"] = 0
# Not a rule
drc.add_layer("implant",
              width = 0,
              spacing = 0)

# 6.1 Exact contact size
# 5.3 Minimum contact spacing
drc.add_layer("tap",
              width = 2*_lambda_,
              spacing = 3*_lambda_)
# 6.2.b Minimum active overlap
drc.add_enclosure("active",
                  layer = "tap",
                  enclosure = _lambda_)
drc.add_enclosure("active",
                  layer = "contact",
                  enclosure = _lambda_)
# Reserved for other technologies
drc["tap_to_gate"] = 2*_lambda_
# 5.4 Minimum spacing to gate of transistor
drc["licon_to_gate"] = 2*_lambda_

# 6.1 Exact contact size
# 5.3 Minimum contact spacing
drc.add_layer("licon",
              width = 2*_lambda_,
              spacing = 3*_lambda_)
drc["minwidth_licon"] = 3*_lambda_    
drc["minwidth_via"] = 3*_lambda_    
drc["via_to_via"] = 3*_lambda_    

drc.add_enclosure("npc",
                  layer = "poly",
                  enclosure = _lambda_)

# 8.3 Minimum overlap by m1
drc.add_enclosure("m1",
                  layer = "via",
                  enclosure = _lambda_)

              
# 5.2.b Minimum poly overlap
drc.add_enclosure("poly",
                  layer = "licon",
                  enclosure = _lambda_)
# Reserved for other technologies
drc["licon_to_gate"] = 2*_lambda_
# 5.4 Minimum spacing to gate of transistor
drc["licon_to_poly"] = 2*_lambda_

# 7.1 Minimum width
# 7.2 Minimum spacing
drc.add_layer("m1",
              width = 3*_lambda_,
              spacing = 3*_lambda_)
# 7.3 Minimum overlap of any contact
drc.add_enclosure("m1",
                  layer = "licon",
                  enclosure = _lambda_)
drc.add_enclosure("m1",
                  layer = "tap",
                  enclosure = _lambda_)

# 8.1 Exact size
# 8.2 Minimum via spacing
drc.add_layer("via",
              width = 2*_lambda_,
              spacing = 3*_lambda_)

# 9.1 Minimum width
# 9.2 Minimum spacing
drc.add_layer("m2",
              width = 3*_lambda_,
              spacing = 3*_lambda_)
# 9.3 Minimum overlap of via
drc.add_enclosure("m2",
                  layer = "via",
                  enclosure = _lambda_)
# 14.3 Minimum overlap by m2
drc.add_enclosure("m2",
                  layer = "via2",
                  enclosure = _lambda_)

# 14.1 Exact size
# 14.2 Minimum spacing
drc.add_layer("via2",
              width = 2*_lambda_,
              spacing = 3*_lambda_)

# 15.1 Minimum width
# 15.2 Minimum spacing to m3
drc.add_layer("m3",
              width = 3*_lambda_,
              spacing = 3*_lambda_)

# 15.3 Minimum overlap of via 2
drc.add_enclosure("m3",
                  layer = "via2",
                  enclosure = _lambda_)

# 21.3 Minimum overlap by m3
drc.add_enclosure("m3",
                  layer = "via3",
                  enclosure = _lambda_)

# 21.1 Exact size
# 21.2 Minimum spacing
drc.add_layer("via3",
              width = 2*_lambda_,
              spacing = 3*_lambda_)

# 22.1 Minimum width
# 22.2 Minimum spacing to m4
drc.add_layer("m4",
              width = 6*_lambda_,
              spacing = 6*_lambda_)

# 22.3 Minimum overlap of via 3
drc.add_enclosure("m4",
                  layer = "via3",
                  enclosure = 2*_lambda_)

###################################################
# Spice Simulation Parameters
###################################################

# spice model info
spice={}
spice["sky130_fd_pr__nfet_01v8"]="sky130_fd_pr__nfet_01v8"
spice["sky130_fd_pr__pfet_01v8"]="sky130_fd_pr__nfet_01v8"
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
parameter["sa_en_pmos_size"] = 24 * _lambda_
parameter["sa_en_nmos_size"] = 9 * _lambda_
parameter["sa_inv_pmos_size"] = 18 * _lambda_
parameter["sa_inv_nmos_size"] = 9 * _lambda_
parameter["bitcell_drain_cap"] = 0.2        # In Femto-Farad, approximation of drain capacitance

###################################################
# Technology Tool Preferences
###################################################

drc_name = "magic"
lvs_name = "netgen"
pex_name = "magic"

blackbox_bitcell = False