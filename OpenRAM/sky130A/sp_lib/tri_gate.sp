*********************** tri_gate ******************************

.SUBCKT tri_gate in out en enb vdd gnd

* SPICE3 file created from tri_gate.ext - technology: scmos

X0 inb in gnd gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X1 out enb gnd gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X2 out en out1 gnd sky130_fd_pr__nfet_01v8 w=0.55u l=0.15u
X3 inb in vdd vdd sky130_fd_pr__pfet_01v8 w=0.42u l=0.15u
X4 out1 inb vdd vdd sky130_fd_pr__pfet_01v8 w=0.42u l=0.15u
X5 out enb out1 vdd sky130_fd_pr__pfet_01v8 w=0.55u l=0.15u
X6 out1 inb gnd gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u

.ENDS
