
*********************** "cell_1rw" ******************************
.SUBCKT replica_cell_1rw bl blbar wl vdd gnd
* SPICE3 file created from cell_1rw.ext - technology: sky130A

X0 vdd wl blbar gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X1 vdd q vdd vdd sky130_fd_pr__pfet_01v8 w=0.42u l=0.15u
X2 q vdd vdd vdd sky130_fd_pr__pfet_01v8 w=0.42u l=0.15u
X3 q vdd gnd gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X4 vdd q gnd gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X5 q wl bl gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u

.ENDS
