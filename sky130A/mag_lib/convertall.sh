magic -T ../tech/sky130A.tech -dnull -noconsole << EOF
load dff
gds write ../gds_lib/dff.gds
load cell_1rw
gds write ../gds_lib/cell_1rw.gds
load replica_cell_1rw
gds write ../gds_lib/replica_cell_1rw.gds
load sense_amp
gds write ../gds_lib/sense_amp.gds
load tri_gate
gds write ../gds_lib/tri_gate.gds
load write_driver
gds write ../gds_lib/write_driver.gds
EOF
