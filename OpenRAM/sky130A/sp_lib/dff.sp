*********************** "dff" ******************************
* Positive edge-triggered FF
.SUBCKT dff D Q clk vdd gnd

* SPICE3 file created from dff.ext - technology: sky130A

X00 vdd clk a_24_24# vdd sky130_fd_pr__pfet_01v8 w=0.55u l=0.15u
X01 a_84_296# D vdd vdd sky130_fd_pr__pfet_01v8 w=0.55u l=0.15u
X02 a_104_24# clk a_84_296# vdd sky130_fd_pr__pfet_01v8 w=0.55u l=0.15u
X03 a_140_296# a_24_24# a_104_24# vdd sky130_fd_pr__pfet_01v8 w=0.55u l=0.15u
X04 vdd a_152_16# a_140_296# vdd sky130_fd_pr__pfet_01v8 w=0.55u l=0.15u
X05 a_152_16# a_104_24# vdd vdd sky130_fd_pr__pfet_01v8 w=0.55u l=0.15u
X06 a_260_296# a_152_16# vdd vdd sky130_fd_pr__pfet_01v8 w=0.55u l=0.15u
X07 a_280_24# a_24_24# a_260_296# vdd sky130_fd_pr__pfet_01v8 w=0.55u l=0.15u
X08 a_320_336# clk a_280_24# vdd sky130_fd_pr__pfet_01v8 w=0.55u l=0.15u
X09 vdd Q a_320_336# vdd sky130_fd_pr__pfet_01v8 w=0.55u l=0.15u

X10 gnd clk a_24_24# gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X11 Q a_280_24# vdd vdd sky130_fd_pr__pfet_01v8 w=0.55u l=0.15u

X12 a_84_24# D gnd gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X13 a_104_24# a_24_24# a_84_24# gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X14 a_140_24# clk a_104_24# gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X15 gnd a_152_16# a_140_24# gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X16 a_152_16# a_104_24# gnd gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X17 a_260_24# a_152_16# gnd gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X18 a_280_24# clk a_260_24# gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X19 a_320_24# a_24_24# a_280_24# gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X20 gnd Q a_320_24# gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X21 Q a_280_24# gnd gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u

.ENDS
