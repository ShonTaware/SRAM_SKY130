
*********************** "dummy_cell_1rw" ******************************
.SUBCKT dummy_cell_1rw bl br wl vdd gnd

X0 qbar wl blbar_noconn gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X1 qbar q vdd vdd sky130_fd_pr__pfet_01v8 w=0.42u l=0.15u
X2 q qbar vdd vdd sky130_fd_pr__pfet_01v8 w=0.42u l=0.15u
X3 q qbar gnd gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X4 qbar q gnd gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X5 q wl bl_noconn gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u

.ENDS
