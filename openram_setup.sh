#!/bin/bash

function addbashaliases() {
  # Add source bash_aliases on .bashrc
  cat >> ~/.bashrc << EOT
export OPENRAM_HOME="$(pwd)/OpenRAM/compiler"
export OPENRAM_TECH="$(pwd)/OpenRAM/technology"

export PYTHONPATH="$PYTHONPATH:$OPENRAM_HOME"
EOT

  # Reload current environment
  source ~/.bashrc
}


git clone https://github.com/VLSIDA/OpenRAM.git

# Execute the function                                                                                                                                                                                                                                                         
addbashaliases