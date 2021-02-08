# Design of 1024x32 SRAM (32Kbits) using OpenRAM and SKY130 PDKs 
  This repository aims at design of 1024x32 SRAM cell array (32Kbits or 4KB) with a configuration of 1.8 V operating voltage and access time less than 2.5ns using Google SkyWater SKY130 PDKs and OpenRAM memory complier.
  
# Table of Contents
  - [Introduction To SRAM Cell Design](#introduction-to-sram-cell-design)
  - [Setting Up Environment](#setting-up-environment)
      - [Open-Source Tools Used](#open-source-tools-used)
      - [Cloning and Installing](#cloning-and-installing)
      - [Independent Installation](#independent-installation)
  - [SRAM Memory Architecture](#sram-memory-architecture)
  - [Custom Cell for OpenRAM](#custom-cells-for-openram)
      - [About OpenRAM](#about-openram)
      - [Custom Cells](#custom-cells)
  - [Pre-Layout Schematic and Simulations](#pre-layout-schematic-and-simulations)
      1. [6T SRAM Cell](#6t-sram-cell)
      2. [Sense Amplifier](#sense-amplifier)
      3. [Write Driver](#write-driver)
      4. [Tri-State Buffer](#tri-state-buffer)      
      5. [D-Flip-Flop](#d-flip-flop)      
      6. [Write Driver](#write-driver)      
      - [1-bit SRAM](#1-bit-sram)
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
    1. NGSPICE: Following commands can be used for installing only the NGSPICE tool.

        $    sudo apt-get install ngspice

    2. Xschem: Following commands can be used for installing only the Xschem Schematic Editor tool.

        $    sudo apt-get install git
        $    git clone https://github.com/StefanSchippers/xschem.git
        $    cd xschem
        $    ./configure
        $    make
        $    make install

    3. Magic: Following commands can be used for installing only the Magic Layout tool.

        $    sudo apt-get install git
        $    git clone https://github.com/RTimothyEdwards/magic.git
        $    cd magic
        $    ./configure
        $    make
        $    make install      

# SRAM Memory Architecture

# Custom Cell for OpenRAM
  
  ## About OpenRAM
  ## Custom Cells

# Pre-Layout Schematic and Simulations](#pre-layout-schematic-and-simulations)
  1. 6T SRAM Cell

    ### Schematic

    ### Read Operation

      <img src="Prelayout/Simulations/sram_cell_6T_read_waveform.JPG">

    ### Write Operation

      <img src="Prelayout/Simulations/sram_cell_6T_write_waveform.JPG">

    ### Static Noise Margin

      * Hold SNM
      * Read SNM
      * Write SNM

    ### N-Curve 

  2. Sense Amplifier
  3. Write Driver
  4. Tri-State Buffer
  5. D-Flip-Flop
  6. Write Driver
  ## 1-bit SRAM

# Future Work
  

# References
  - VLSI System Design: https://www.vlsisystemdesign.com/

# Acknowledgement
  - [Kunal Ghosh](https://github.com/kunalg123), Co-founder, VSD Corp. Pvt. Ltd.
  
# Contact Information
  - [Shon Taware](https://www.linkedin.com/in/Shon-Taware/), M.Tech. Embedded Systems and VLSI Design
  - [Kunal Ghosh](https://github.com/kunalg123), Co-founder, VSD Corp. Pvt. Ltd.
