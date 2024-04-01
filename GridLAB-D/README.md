# GridLAB-D (GLD)

## GLD730_x64_20230616.zip
- This zip package, provided by Dr. Francis K Tuffner, includes the compiled GLD: GridLAB-D 5.0.0-19508 (346842f9:feature/730) 64-bit WINDOWS RELEASE.
- GridLAB-D v5.2 Release (Oct 12, 2023): https://github.com/gridlab-d/gridlab-d/releases/tag/v5.2
- Note that "connect_type WYE_WYE;" means "It’s implied to be grounded" for both sides.

## IEEE 4 Node Test Feeder/ieee_4-node.glm
- GLD model file of the IEEE 4-Node Test System.
- Power flow results have been verified, with respect to the "Solutions" (Page 6) of "IEEE 4 Node Test Feeder Revised Sept. 19, 2006.doc".

## Modified 6-Node Base Case
- "modified_6-node.glm" is the GLD model file of the Modified 6-Node Test System, see "IEEE 6 Bus (Mod 4 Bus) Test System.docx" for details.
- Power flow results of GLD are compared with the solutions of OpenDSS and Simscape in "Power Flow Results of Base Case.docx".
- "DSS Model and Result Files" is the folder of the DSS model and results files.

## Modified 6-Node PV Case
- "modified_6-node_pv_static.glm" is the GLD model file of the Modified 6-Node Test System with PV added on Node 5.
- Power flow results of GLD are stored in the folder "GLD Results", while voltages and currents are reported in "Power Flow Results of PV Case.docx".

## Modified 6-Node IM Case
- The power flow results do not look very good.
- The motor model of GLD may need some revisions before it can be used for the studies here.