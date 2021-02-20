# Design of 1024x32 SRAM (32Kbits) using OpenRAM and SKY130 PDKs 
  This repository aims at design of 1024x32 SRAM cell array (32Kbits or 4KB) with a configuration of 1.8 V operating voltage and access time less than 2.5ns using Google SkyWater SKY130 PDKs and OpenRAM memory complier.
  
# Table of Contents
  - [Introduction To SRAM Cell Design](#introduction-to-sram-cell-design)
  - [Setting Up Environment](#setting-up-environment)
      - [Open-Source Tools Used](#open-source-tools-used)
      - [Cloning and Installing](#cloning-and-installing)
      - [Independent Installation](#independent-installation)
  - [SRAM Memory Architecture](#sram-memory-architecture)
  - [Custom Cells for OpenRAM](#custom-cells-for-openram)
      - [About OpenRAM](#about-openram)
      - [Custom Cells](#custom-cells)
  - [OpenRAM Configuration For SkyWater SKY130 PDKs](#openram-configuration-for-skywater-sky130-pdks)
    - [Installation and Setup of OpenRAM](#installation-and-setup-of-openram)
    - [OpenRAM Directory Structure](#openram-directory-structure)
    - [Porting SKY130 to OpenRAM](#porting-sky130-to-openram)
      - [gds_lib directory](#gds_lib-directory)
      - [sp_lib directory](#sp_lib-directory)
      - [layers.map](#layersmap)
      - [tech Directory](#tech-directory)
    - [Usage of OpenRAM](#usage-of-openram)
    - [Issues, Challenges and Fixes in configuring OpenRAM for SKY130](#issues-challenges-and-fixes-in-configuring-openram-for-sky130)
  - [Pre-Layout Schematic and Simulations](#pre-layout-schematic-and-simulations)
      1. [6T SRAM Cell](#1-6t-sram-cell)
      2. [Pre-charge Circuit](#2-pre-charge-circuit)
      3. [Sense Amplifier](#3-sense-amplifier)
      4. [Write Driver](#4-write-driver)
      5. [Tri-State Buffer](#5-tri-state-buffer)      
      6. [D-Flip-Flop](#6-d-flip-flop)      
      - [1-bit SRAM](#1-bit-sram)
<!--  - [Layout and Post-Layout Simulations](#layout-and-post-layout-simulations)
      1. [6-T SRAM Cell](#1-6-t-sram-cell)
      2. [Sense Amplifier](#2-sense-amplifier)
      3. [Write Driver](#3-write-driver)
      4. [Tri-State Buffer](#4-tri-state-buffer)      
      5. [D-Flip-Flop](#5-d-flip-flop)      
      - [1-bit Integrated SRAM](#1-bit-integrated-sram)-->
  - [Future Work](#future-work)
  - [References](#references)
  - [Acknowledgement](#acknowledgement)
  - [Contact Information](#contact-information)

# Introduction To SRAM Cell Design
  Today, Static Random-Access Memory (SRAM) has become a standard element of any Application Specific Integrated Circuit (ASIC), System-On-Chip (SoC), or other micro-architectures. For this wide variety of applications, SRAMs are configured using parameters like the word-length, bit lines, operating voltage, access time, and most importantly the technology node. The access time of an SRAM cell is the time require for a read or write operation of SRAM. 
  
  Manually configuring the SRAM for every change in parameter seems a slightly in-efficient and tedious task. Due to this reason, the memory compiler is used on a large scale, as it facilitates easy configuration and optimization of memory. OpenRAM, an open-source memory compiler is used for characterization and generation of SRAM designs.
  
# Setting Up Environment
  This repository mentioned multiple open-source circuit schematic design, layout design, SPICE simulations tools and memory compiler. The tools used and their installation is explained in details below. The complete environemnt setup for the open-source OpenLANE RTL2GDS flow can be found [here](https://github.com/ShonTaware/openlane_environment_setup).

## Open-Source Tools Used
  | Name of Tool | Description |
  | --- | --- |
  | [NGSPICE](https://github.com/imr/ngspice) | An open-source mixed-level/mixed-signal electronic spice circuit simulator. |
  | [Xschem](https://github.com/StefanSchippers/xschem) | A schematic editor for VLSI/Asic/Analog custom designs, netlist backends for VHDL, Spice and Verilog. |
  | [Magic](https://github.com/RTimothyEdwards/magic) | An open-source VLSI Layout Tool with easy DRC options. |

## Cloning and Installing
  For properly installing all the above mentioned tools and supporting tools to their updated version follow the below mentioned steps.(Only for Ubuntu Operating System)

      $    sudo apt-get install git
      $    git clone https://github.com/ShonTaware/SRAM_SKY130.git
      $    cd SRAM_SKY130
      $    chmod +777 setup_environment.sh
      $    ./setup_environment.sh

## Independent Installation
  1. **NGSPICE:** Following commands can be used for installing only the NGSPICE tool.

          $    sudo apt-get install ngspice

  2. **Xschem:** Following commands can be used for installing only the Xschem Schematic Editor tool.

          $    sudo apt-get install git
          $    git clone https://github.com/StefanSchippers/xschem.git
          $    cd xschem
          $    ./configure
          $    make
          $    make install

  3. **Magic:** Following commands can be used for installing only the Magic Layout tool.

          $    sudo apt-get install git
          $    git clone https://github.com/RTimothyEdwards/magic.git
          $    cd magic
          $    ./configure
          $    make
          $    make install      

# SRAM Memory Architecture
  SRAM Memory is a block which designed by integrating several sub-blocks. This SRAM memory architecture for a multi-port SRAM memory is shown in the diagram below.

  <img src="Diagrams/sram_arch.png">

# Custom Cells for OpenRAM
  
## About OpenRAM
  OpenRAM is an open-source Python framework to create the layout, netlists, timing and power models, placement and routing models, and other views necessary to use SRAMs in ASIC design. It supports integration in both commercial and open-source flows with both predictive and fabricable technologies.

## Custom Cells
  OpenRAM facilitates to convert any custom design cells and design rules to various IP deliverables or formats.

  <img src="Diagrams/custom_cell_openram.png">

  OpenRAM uses some custom-designed library primitives as technology input. Since density is extremely important, the following cells are pre-designed in each technology: 
  * 6T cell
  * Sense amplifier
  * Master-slave flip-flop 
  * Tri-state gate 
  * Write driver

# OpenRAM Configuration For SkyWater SKY130 PDKs
The detailed OpenRAM configuration, usage and issues for SKY130 pdk is documented in this section.

## Installation and Setup of OpenRAM
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

## OpenRAM Directory Structure
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

## Porting SKY130 to OpenRAM
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

### `gds_lib` directory
  This directory contains all the custom premade library cells in `.gds` file format. Following files should be listed in the gds_lib directory:
  1. dff.gds
  2. sense_amp.gds
  3. write_driver.gds
  4. cell_6t.gds
  5. replica_cell_6t.gds
  6. dummy_cell_6t.gds 

### `sp_lib` directory
This directory contains all the spice netlsits of custom premade library cells in `.sp` file format. 

### `models` directory
This directory contains all the NMOS and PMOS models for temperatures, voltages and process corners as per requirement. This repository contains the nfet and pfet models for all process corners operating at 1.8 V. 

### `layers.map`
This file contains the layer description for gds layers. It needs to be generated from the SKY130 PDK document provided by SkyWater. You can find the document [here](https://docs.google.com/spreadsheets/d/1oL6ldkQdLu-4FEQE0lX6BcgbqzYfNnd1XA8vERe0vpE/edit#gid=0).
  
The `layers.map` should be organized in a specific syntax. Here, each layer is given on a separate line in below mentioned format:

  ```
    <layer-name> <purpose-of-layer> <GDS-layer> <GDS-purpose>
  ```
The `layers.map` file is added to the repository and can be found [here](https://github.com/ShonTaware/SRAM_SKY130/blob/main/OpenRAM/sky130A/layers.map).  

### `tech/` Directory

* `tech/sky130A.tech`
  This is the technology file provided by SkyWater in the SKY130 PDKs. It needs to copied to this `tech` directory.
  The `sky130A.tech` technology file is added to the repository.

* `tech/tech.py`
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

## Usage of OpenRAM
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
  process_corners = ["TT"]
  
  # Voltage corners to characterize
  supply_voltages = [ 1.8 ]
  
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

## Issues, Challenges and Fixes in configuring OpenRAM for SKY130

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


# Pre-Layout Schematic and Simulations

## 1. 6T SRAM Cell
  As the name says, 6T SRAM cell consists of 6 MOSFETS - 2 PMOS and 4 NMOS. It is design by cross coupling two CMOS inverters which hold the bit, and two access transistor for enabling the access to the cross coupled inverters.

  <img src="Prelayout/Diagrams/SRAM_Cell_6T.png">

### Schematic
  The figure below shows the schematic of the generic 6T SRAM cell. Here, M1, M2 make the first inverter; M3, M4 make the second inverter and M5, M6 are the access transistors.

  <img src="Prelayout/Schematic/xschem_sram_6t_cell.png">

### Read Operation
  The read operation is a critical one in SRAM cell. This is becuase, before enabling the access transistors, the bit-lines are first pre-charged to high logic. Depending upon the bit store, one of the bit-line is pulled back to logic low when the access transistors are enabled. 

  <img src="Prelayout/Simulations/sram_cell_6T_read_waveform.JPG">

### Write Operation
  The bit to be written is first loaded to the bit-line and its inverted bit is loaded on the other bit-line. Once the access transistors are enabled the bit values on bit-lines are over-written on the inverter logic.

  <img src="Prelayout/Simulations/sram_cell_6T_write_waveform.JPG">

### Analyzing Stability of 6T SRAM Cell

* **Static Noise Margin**

  Static noise margin (SNM) is a key figure of merit for an SRAM cell. It can be extracted by nesting the largest possible square in the two voltage transfer curves (VTC) of the two CMOS inverters involved. The SNM is defined as the side-length of the square (i.e. diagonal-length), given in volts. When an external DC noise is larger than the SNM, the state of the SRAM cell can change and data is lost.

1. **Hold SNM**

  <img src="Prelayout/Schematic/xschem_sram_6t_cell_hold_snm.png">

        $    ngspice hold_snm.spice

  <img src="Prelayout/Simulations/sram_cell_6T_hold_snm_waveform.JPG">
  SNM<sub>high</sub> = 1.0879 V <br />
  SNM<sub>low</sub> = 1.1112 V <br />
  Hold SNM = min(SNM<sub>high</sub>, SNM<sub>low</sub>) = 1.0879 V  <br /><br />

2. **Read SNM**

  <img src="Prelayout/Schematic/xschem_sram_6t_cell_read_snm.png">

        $    ngspice read_snm.spice

  <img src="Prelayout/Simulations/sram_cell_6T_read_snm_waveform.JPG">
  SNM<sub>high</sub> = 0.5511 V <br />
  SNM<sub>low</sub> = 0.4294 V <br />
  Read SNM = min(SNM<sub>high</sub>, SNM<sub>low</sub>) =  0.4294 V <br /><br />

3. **Write SNM**

  <img src="Prelayout/Schematic/xschem_sram_6t_cell_write_snm.png">

        $    ngspice write_snm.spice

  <img src="Prelayout/Simulations/sram_cell_6T_write_snm_waveform.JPG">
  Write SNM = 1.3494 V  <br /><br />

* **N-Curve**
  N-curve is a metric used for inline testers. It gives information for both voltage and current, and in addition it has no voltage scaling delimiter as found in SNM approach. It also has the complete information about the SRAM stability and also write ability in a single plot. N-curve can be further extended to power metrics in which both the voltage and current information are taken into consideration to provide better stability analysis of the SRAM cell.

  <img src="Prelayout/Schematic/xschem_sram_6t_cell_n_curve.png">

        $    ngspice n_curve.spice

  <img src="Prelayout/Simulations/sram_cell_6T_n_curve_waveform.JPG">

  1. **Static Voltage Noise Margin (SVNM):** It is the voltage difference between point A and B. It indicates the maximum tolerable DC noise voltage of the cell before its content changes.
  <br /> SVNM = 0.5644 V

  2. **Static Current Noise Margin (SINM):** It is the additional current information provided by the N-curve, namely the peak current located between point A and B. It can also be used to characterize the cell read stability.
  <br /> SINM = 122.6 uA

  **Note:** For better read stability, SVNM and SINM must be high value.

  3. **Write-Trip Voltage (WTV):** It is the voltage difference between point C and B. It is the voltage drop needed to flip the internal node “1” of the cell with both the bit-lines clamped to VDD.
  <br /> WTV = 0.9422 V
  
  4. **Write-Trip Current (WTI):** It is the negative current peak between point C and B. It is the amount of current needed to write the cell when both bit-lines are kept at VDD.
  <br /> WTI = -30.869 uA

## 2. Pre-charge Circuit
  This circuit block is used to pre-charge the bit-lines to Vdd or high logic during a read operation.

  Shown below is the schematic and simulation of the Pre-charge circuit.

  <img src="Prelayout/Schematic/xschem_precharge_circuit.png">

      $    ngspice precharge_circuit.spice

  <img src="Prelayout/Simulations/precharge_circuit_waveform.JPG">

## 3. Sense Amplifier
  Sense Amplifiers in SRAM generally a Differential Voltage Amplifier. They form a very important part of SRAM memory as these amplifiers define the robustness of the bit-lines sensing. The function of sense amplifier is to amplify the very small analog differential voltage between the bit-lines during a read operation and provide a digital output. This effectively reduces the time required for the read operation, as each individual cell need not fully discharge the bit line.
  * if bit > bit_bar, output is 1
  * if bit < bit_bar, output is 0

  Shown below is the schematic and simulation of a Sense Amplifier.

  <img src="Prelayout/Schematic/xschem_sense_amplifier.png">

        $    ngspice sense_amplifier.spice

  <img src="Prelayout/Simulations/sense_amplifier_waveform.JPG">

## 4. Write Driver
  As discussed in read operation, the bit-lines are pre-charged to Vdd during the read operation. If a write operation occurs, one of the bit-lines should driven back to low logic before enabling access transistors. Write drivers are used for this purpose.

  Shown below is the schematic and simulation of a Write Driver.

  <img src="Prelayout/Schematic/xschem_write_driver.png">

      $    ngspice write_driver.spice

  <img src="Prelayout/Simulations/write_driver_waveform.JPG">

## 5. Tri-State Buffer
  Tri-state buffer is a normal buffer with an extra enable input. Whenever, the enable input is high, tri-state buffer behaves as a normal buffer, otherwise it will either give high impedance or low logic as output.

  Shown below is the schematic and simulation of a Tri-State Buffer.

  <img src="Prelayout/Schematic/xschem_tristate_buffer.png">

      $    ngspice tristate_buffer.spice

  <img src="Prelayout/Simulations/tristate_buffer_waveform.JPG">

## 6. D-Flip-Flop
  Shown below is the schematic and simulation of a Positive Edge triggered D-Flip-Flop.

  <img src="Prelayout/Schematic/xschem_d_ff.png">

      $    ngspice d_ff.spice

  <img src="Prelayout/Simulations/d_ff_waveform.JPG">

## 1-bit SRAM
  1-bit SRAM comprises of a 6T SRAM cell, a sense amplifier, a write driver and a pre-charge circuit.

  <img src="Prelayout/Diagrams/sram_1bit_block_diagram.jpg">

  * Read Operation

        $    ngspice sram_1bit_read.spice

  <img src="Prelayout/Simulations/sram_1bit_cell_read_waveform.JPG">

  * Write Operation

        $    ngspice sram_1bit_write.spice

  <img src="Prelayout/Simulations/sram_1bit_cell_write_waveform.JPG">

# Layout and Post-Layout Simulations

## 6T SRAM Cell

  <img src="Postlayout/Layouts/magic_sram_6t_cell_read.JPG">
  <img src="Postlayout/Simulations/sram_6t_cell_read.JPG">

# Future Work
  Perform post-layout design and simulations. Also, configure the OpenRAM for new Sky130 PDKs and custom cells.

# References
  - VLSI System Design: https://www.vlsisystemdesign.com/
  - Efabless OpenLANE: https://github.com/efabless/openlane
  - OpenRAM: https://vlsida.github.io/OpenRAM/
  - M. Guthaus et al., “OpenRAM: An open-source memory compiler,” *2016 IEEE/ACM International Conference on Computer-Aided Design(ICCAD)*, Austin, TX, 2016, pp. 1-6.

# Acknowledgement
  - [Kunal Ghosh](https://github.com/kunalg123), Co-founder, VSD Corp. Pvt. Ltd.
  
# Contact Information
  - [Shon Taware](https://www.linkedin.com/in/Shon-Taware/), M.Tech. Embedded Systems and VLSI Design
  - [Kunal Ghosh](https://github.com/kunalg123), Co-founder, VSD Corp. Pvt. Ltd.
