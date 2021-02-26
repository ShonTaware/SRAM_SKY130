magic -T ../tech/sky130A.tech -dnull -noconsole << EOF
load dff
gds write ./gds_op/dff.gds
load cell_1rw
gds write ./gds_op/cell_1rw.gds
load replica_cell_1rw
gds write ./gds_op/replica_cell_1rw.gds
load sense_amp
gds write ./gds_op/sense_amp.gds
load tri_gate
gds write ./gds_op/tri_gate.gds
load write_driver
gds write ./gds_op/write_driver.gds
EOF
