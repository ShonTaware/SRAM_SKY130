
*********************** "cell_1rw" ******************************
.SUBCKT cell_1rw bl br wl vdd gnd
* SPICE3 file created from cell_1rw.ext - technology: sky130A

* Inverter 1
X0 Q Q_bar vdd vdd sky130_fd_pr__pfet_01v8 w=0.42u l=0.15u
X2 Q Q_bar gnd gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u

* Inverter 2
X1 vdd Q Q_bar vdd sky130_fd_pr__pfet_01v8 w=0.42u l=0.15u
X3 gnd Q Q_bar gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u

* Access transistors
X4 Q wl bl gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u
X5 Q_bar wl br gnd sky130_fd_pr__nfet_01v8 w=0.42u l=0.15u

.ENDS
