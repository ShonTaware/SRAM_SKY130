*********************** Write_Driver ******************************
.SUBCKT write_driver din bl br en vdd gnd

X0 dinbb dinb vdd vdd sky130_fd_pr__pfet_01v8 w=0.42u l=0.15u
X1 br out1 gnd gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X2 dinb din vdd vdd sky130_fd_pr__pfet_01v8 w=0.42u l=0.15u
X3 out1 en gnd gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X4 out2 en gnd gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X5 dinb din gnd gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X6 dinbb dinb gnd gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X7 out2 en 5 vdd sky130_fd_pr__pfet_01v8 w=0.42u l=0.15u
X8 out2 dinbb gnd gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X9 5 dinbb vdd vdd sky130_fd_pr__pfet_01v8 w=0.42u l=0.15u
X10 out1 en 4 vdd sky130_fd_pr__pfet_01v8 w=0.42u l=0.15u
X11 4 dinb vdd vdd sky130_fd_pr__pfet_01v8 w=0.42u l=0.15u
X12 bl out2 gnd gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X13 out1 dinb gnd gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u



.ENDS   $ write_driver
