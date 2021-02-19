# OpenRAM Configuration For SkyWater SKY130 PDKs
This page enlists the methodology and challenges in configuring the OpenRAM memory compiler for the Google SkyWater Sky130 PDKs.

# Table of Contents
  - [Installation and Setup of OpenRAM](#installation-and-setup-of-openram)
  - [OpenRAM Directory Structure](#openram-directory-structure)
  - [Porting SKY130 to OpenRAM](#porting-sky130-to-openram)
    - [gds_lib directory](#gds_lib-directory)
    - [sp_lib directory](#sp_lib-directory)
    - [layers.map](#layersmap)
    - [tech Directory](#tech-directory)
  - [Usage of OpenRAM](#usage-of-openram)
  - [Issues, Challenges and Fixes in configuring OpenRAM for SKY130](#issues-challenges-and-fixes-in-configuring-openram-for-sky130)

# Installation and Setup of OpenRAM
The detailed OpenRAM project can be found [here](https://github.com/VLSIDA/OpenRAM). The steps to the installation and setup are mentioned below.

1. **Clone the OpenRAM project**
```
  $    git clone https://github.com/VLSIDA/OpenRAM.git

```

2. **Configure Path**
  Add following lines in `.bashrc` file.
```
  $    export OPENRAM_HOME="$HOME/openram/compiler"
  $    export OPENRAM_TECH="$HOME/openram/technology"

  # Add Python Path of OpenRAM compiler
  $    export PYTHONPATH="$PYTHONPATH:$OPENRAM_HOME"

  # Set Path to PDKs
  $    export SKY130A="/path-to-pdks/sky130"

```

# OpenRAM Directory Structure
  After the installation is properly done. The directory structure of OpenRAM directory looks similar to that of mentioned. 
```
  ├── OpenRAM 
  |  ├── compiler
  |  ├── technologies
  |     ├── freepdk45  (available with compiler)
  |     ├── scn4m_subm (available with compiler)
  |     ├── sky130A 

```
  The `sky130A` directory is not available by default. You need to create it in order to add support for SkyWater PDK Sky130. The detailed contents and their description is explained further in the document. Also, the configure `sky130A` directory is included in the repository for reference. It can be found at [OpenRAM/sky130A/](https://github.com/ShonTaware/SRAM_SKY130/tree/main/OpenRAM/sky130A)

# Porting SKY130 to OpenRAM
The OpenRAM compiler is currently available for two technologies, namely - SCMOS and FreePDK45.
For adding a new technology support to OpenRAM, a directory with name of process node should be created in `technology` directory of OpenRAM.

The `technology` directory should contains following information.

```
  ├── technology 
  |  ├── sky130A
  |     ├── gds_lib
  |     ├── sp_lib
  |     ├── mag_lib (optional)
  |     ├── models
  |     ├── layers.map (can be included in another sub-directory)
  |     ├── tech
  |        ├── __init__.py
  |        ├── tech.py
  |        ├── sky130A.tech

```

## `gds_lib` directory
  This directory contains all the custom premade library cells in `.gds` file format. Following files should be listed in the gds_lib directory:
  1. dff.gds
  2. sense_amp.gds
  3. write_driver.gds
  4. cell_6t.gds
  5. replica_cell_6t.gds
  6. dummy_cell_6t.gds 

## `sp_lib` directory
This directory contains all the spice netlsits of custom premade library cells in `.sp` file format. 

## `models` directory
This directory contains all the NMOS and PMOS models for temperatures, voltages and process corners as per requirement. This repository contains the nfet and pfet models for all process corners operating at 1.8 V. 

## `layers.map`
This file contains the layer description for gds layers. It needs to be generated from the SKY130 PDK document provided by SkyWater. You can find the document [here](https://docs.google.com/spreadsheets/d/1oL6ldkQdLu-4FEQE0lX6BcgbqzYfNnd1XA8vERe0vpE/edit#gid=0).
  
The `layers.map` should be organized in a specific syntax. Here, each layer is given on a separate line in below mentioned format:

```
  <layer-name> <purpose-of-layer> <GDS-layer> <GDS-purpose>
```
The `layers.map` file is added to the repository and can be found [here](https://github.com/ShonTaware/SRAM_SKY130/blob/main/OpenRAM/sky130A/layers.map).  

## `tech/` Directory

### `tech/sky130A.tech`
  This is the technology file provided by SkyWater in the SKY130 PDKs. It needs to copied to this `tech` directory.
  The `sky130A.tech` technology file is added to the repository.

### `tech/tech.py`
  This python file contains all the technology related configuration. It contains information about below mentioned paramaters.
  
**Note:** The values for any parameters given below are only for reference and not the actual values. It will be replaced in future commits with correct and appropriate values for Sky130 process node. 

1. **Custom modules**
  ```
    tech_modules = module_type()
  ```

2. **Custom cell properties**
  ```
    cell_properties = cell_properties()
  ```

3. **Layer properties**
  ```
    layer_properties = layer_properties()
  ```

4. **GDS file info**
  ```
    GDS={}
    GDS["unit"]=(0.001,1e-6)
    GDS["zoom"] = 0.5
  ```

5. **Interconnect stacks**
  
  This defines the contacts and preferred directions of the metal, poly and active diffusion layers.
  ```
    poly_stack = ("poly", "poly_contact", "m1")
    active_stack = ("active", "active_contact", "m1")
    m1_stack = ("m1", "via1", "m2")
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
  ```

6. **Power grid**
  
  By default, the power grid is set to m3_stack i.e. it uses m3 and m4 layers for power grid.
  ```
    power_grid = m1_stack  # Use m1 and m2 for power grid
  ```

7. **GDS Layer Map**
  
  The values are similar to those listed in the `layers.map` file.
  ```
    layer["diff"]        = (65, 20)
    layer["tap"]         = (65, 44)
    layer["nwell"]       = (64, 20)
    layer["dnwell"]      = (64, 18)
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
    ...
  ```

8. **Layer names for external PDKs**
  ```
    layer_names = {}
    layer["diff"]        = "active"
    layer["tap"]         = "tap"
    layer["nwell"]       = "nwell"
    layer["dnwell"]      = "dnwell"
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
    ...
  ```

9. **DRC/LVS Rules Setup**
  
  **Note:** Drc rules are required for all the layers mentioned in the interconnect stacks.
  ```
    drclvs_home=os.environ.get("DRCLVS_HOME")
    
    drc = design_rules("sky130A")
    
    #grid size is 1/2 a lambda
    drc["grid"]=0.5*_lambda_
    
    #DRC/LVS test set_up
    drc["drc_rules"] = drclvs_home+"/calibreDRC_sky130A.rul"  # Replace it with "None" to skip it
    drc["lvs_rules"] = drclvs_home+"/calibreLVS_sky130A.rul"  # Replace it with "None" to skip it
    drc["layer_map"] = os.environ.get("OPENRAM_TECH")+"/scn3me_subm/layers.map"
    
    # minwidth_tx with contact (no dog bone transistors)
    drc["minwidth_tx"] = 4*_lambda_
    drc["minlength_channel"] = 2*_lambda_
    
    # Minimum spacing between wells of different type (if both are drawn)
    drc["pwell_to_nwell"] = 0
    
    # Minimum width
    drc.add_layer("nwell",
                  width = 12*_lambda_,
                  spacing = 6*_lambda_)
    
    # Enclosure
    drc.add_enclosure("m1",
                    layer = "via1",
                    enclosure = _lambda_)
    ...
  ```

10. **Technology parameter**
  ```
    _lambda_ = 0.2

    #technology parameter
    parameter                = {}
    parameter["min_tx_size"] = 4*_lambda_
    parameter["beta"]        = 2
    
    # These 6T sizes are used in the parameterized bitcell.
    parameter["6T_inv_nmos_size"] = 8*_lambda_
    parameter["6T_inv_pmos_size"] = 3*_lambda_
    parameter["6T_access_size"]   = 4*_lambda_

  ```

11. **Spice Simulation Parameters**
  
    1. **Spice model info**
    ```
      # spice model info
      spice         = {}
      spice["sky130_fd_pr__nfet_01v8"] = "nmos"
      spice["sky130_fd_pr__pfet_01v8"] = "pmos"
      
    ```
    2. **Map of corners to model files**
    ```
      # This is a map of corners to model files
      SPICE_MODEL_DIR=os.environ.get("SPICE_MODEL_DIR")
      spice["fet_models"] = {"TT": [SPICE_MODEL_DIR + "/nom/pmos.sp", SPICE_MODEL_DIR + "/nom/nmos.sp"],
                             "FF": [SPICE_MODEL_DIR + "/ff/pmos.sp", SPICE_MODEL_DIR + "/ff/nmos.sp"],
                             "FS": [SPICE_MODEL_DIR + "/ff/pmos.sp", SPICE_MODEL_DIR + "/ss/nmos.sp"],
                             "SF": [SPICE_MODEL_DIR + "/ss/pmos.sp", SPICE_MODEL_DIR + "/ff/nmos.sp"],
                             "SS": [SPICE_MODEL_DIR + "/ss/pmos.sp", SPICE_MODEL_DIR + "/ss/nmos.sp"],
                             "ST": [SPICE_MODEL_DIR + "/ss/pmos.sp", SPICE_MODEL_DIR + "/nom/nmos.sp"],
                             "TS": [SPICE_MODEL_DIR + "/nom/pmos.sp", SPICE_MODEL_DIR + "/ss/nmos.sp"],
                             "FT": [SPICE_MODEL_DIR + "/ff/pmos.sp", SPICE_MODEL_DIR + "/nom/nmos.sp"],
                             "TF": [SPICE_MODEL_DIR + "/nom/pmos.sp", SPICE_MODEL_DIR + "/ff/nmos.sp"],
                             }

    ```

    3. **Spice stimulus related variables**
    ```
      spice["feasible_period"]    = 10              # estimated feasible period in ns
      spice["supply_voltages"]    = [4.5, 5.0, 5.5] # Supply voltage corners in [Volts]
      spice["nom_supply_voltage"] = 5.0             # Nominal supply voltage in [Volts]
      spice["rise_time"]          = 0.05            # rise time in [Nano-seconds]
      spice["fall_time"]          = 0.05            # fall time in [Nano-seconds]
      spice["temperatures"]       = [0, 25, 100]    # Temperature corners (celcius)
      spice["nom_temperature"]    = 25              # Nominal temperature (celcius)

    ```

    4. **Analytical delay parameters**
    ```
      spice["nom_threshold"]  = 1.3    # Nominal Threshold voltage in Volts
      spice["wire_unit_r"]    = 0.075  # Unit wire resistance in ohms/square
      spice["wire_unit_c"]    = 0.64   # Unit wire capacitance ff/um^2
      spice["min_tx_drain_c"] = 0.7    # Minimum transistor drain capacitance in ff
      spice["min_tx_gate_c"]  = 0.1    # Minimum transistor gate capacitance in ff
      spice["dff_setup"]      = 9      # DFF setup time in ps
      spice["dff_hold"]       = 1      # DFF hold time in ps
      spice["dff_in_cap"]     = 9.8242 # Input capacitance (D) [Femto-farad]
      spice["dff_out_cap"]    = 2      # Output capacitance (Q) [Femto-farad]

    ```

    5. **Analytical power parameters**
    ```
      spice["bitcell_leakage"] = 1 # Leakage power of a single bitcell in nW
      spice["inv_leakage"]     = 1 # Leakage power of inverter in nW
      spice["nand2_leakage"]   = 1 # Leakage power of 2-input nand in nW
      spice["nand3_leakage"]   = 1 # Leakage power of 3-input nand in nW
      spice["nand4_leakage"]   = 1 # Leakage power of 4-input nand in nW
      spice["nor2_leakage"]    = 1 # Leakage power of 2-input nor in nW
      spice["dff_leakage"]     = 1 # Leakage power of flop in nW
      
      spice["default_event_frequency"] = 100 # Default event activity of every gate. MHz
    ```

12. **Logical Effort relative values for the Handmade cells**
  ```
    parameter["le_tau"]              = 18.17         # In pico-seconds.
    parameter["min_inv_para_delay"]  = 2.07          # In relative delay units
    parameter["cap_relative_per_ff"] = .91           # Units of Relative Capacitance/ Femto-Farad
    parameter["dff_clk_cin"]         = 27.5          # In relative capacitance units
    parameter["6tcell_wl_cin"]       = 2             # In relative capacitance units
    parameter["sa_en_pmos_size"]     = 24 * _lambda_
    parameter["sa_en_nmos_size"]     = 9 * _lambda_
    parameter["sa_inv_pmos_size"]    = 18 * _lambda_
    parameter["sa_inv_nmos_size"]    = 9 * _lambda_
    parameter["bitcell_drain_cap"]   = 0.2           # In Femto-Farad, approximation of drain capacitance

  ```

13. **Technology Tool Preferences**
  ```
    drc_name = "magic"
    lvs_name = "netgen"
    pex_name = "magic"

  ```

# Usage of OpenRAM
  A configuration file need to be generated in python which contains all parameters required for the compiler. Every parameter mentioned in the configuration file overrides the default value of the parameter. If a parameter is not mentioned in the file, compiler will take a default value.
  
A template file named `myconfig_sky130.py` is added in the repository. The file contains parameters as given below.

```
  # Data word size
  word_size = 32
  # Number of words in the memory
  num_words = 1024

  # Technology to use in $OPENRAM_TECH
  tech_name = "sky130A"
  
  # You can use the technology nominal corner only
  #nominal_corner_only = True
  # Or you can specify particular corners
  # Process corners to characterize
  process_corners = ["SS", "TT", "FF"]
  # process_corners = ["TT"]
  # Voltage corners to characterize
  supply_voltages = [ 1.8 ]
  # supply_voltages = [ 3.0, 3.3, 3.5 ]
  # Temperature corners to characterize
  # temperatures = [ 0, 25 100]

  # Output directory for the results
  output_path = "temp"
  # Output file base name
  output_name = "sram_{0}_{1}_{2}".format(word_size,num_words,tech_name)

  # Disable analytical models for full characterization (WARNING: slow!)
  # analytical_delay = False
```

OpenRAM is invoked using the following command
```
  python3 $OPENRAM_HOME/openram.py myconfig_sky130
  
  or
  
  python3 $OPENRAM_HOME/openram.py myconfig_sky130.py
```

# Issues, Challenges and Fixes in configuring OpenRAM for SKY130

1. By default, OpenRAM comes with a contact named `poly_contact` between the polysilicon and metal1. But SKY130 does not have a direct contact available between polysilicon and metal1 layers. Instead, it has a `pcontact` between polysilicon and locali (local interconnect) and further, contact `licon` between locali and metal1.

Therefore, `feol_stacks` mentioned above will have an extra entry for `licon` along with `poly_contact` and `active_contact`.

```
  poly_stack = ("poly", "pcontact", "li")
  li_stack = ("li", "licon", "m1")
  
  # The FEOL stacks get us up to m1
  feol_stacks = [poly_stack,
                 li_stack,
                 active_stack]

```

2. The default `active` layer corresponds to `diff` (active diffusion) layer in SKY130. Similarly, the default `active_contact` layer corresponds to  `tap` layer in SKY130.

```
  layer["diff"]        = (65, 20)
  layer["tap"]         = (65, 44)

  layer["diff"]        = "active" 
  layer["tap"]         = "tap"

```

3. One of the major issue is, the SKY130 PDK do not have boundary layer for drawing purpose in the GDS layer description provided by SkyWater. But OpenRAM compiler expects a boundary layer to compute the cell area and to avoid overlapping of cells.

**Note:** We are currently working on resolving this issue. The solution will be updated to repository soon.

