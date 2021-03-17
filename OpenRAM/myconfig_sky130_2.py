# Data word size
word_size = 2

# Number of words in the memory
num_words = 16

# Technology to use in $OPENRAM_TECH
tech_name = "sky130A"

# You can use the technology nominal corner only
# nominal_corner_only = True

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
