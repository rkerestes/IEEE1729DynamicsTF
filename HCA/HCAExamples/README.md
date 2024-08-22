# Running Examples

The example files are the *.ipynb files, and the *.py files contain the code used in the examples.

## Requirements to run the examples:

1. OpenDSS feeder model is located in <https://github.com/rkerestes/IEEE1729DynamicsTF/tree/main/HCA/HCABase.dss>
2. Python 64 bit (tested with versions 3.12.3 and 3.11.4)
3. Python packages are provided in the requirements.txt file in the HCAExamples folder
4. Jupyter Notebook 7.2.1

If you need more information on how to set up a Python project and a virtual environment, you can check out the following
YouTube videos:

[Python Download and Installation] (https://www.youtube.com/watch?v=uY1rvh-ozTA&list=PLhdRxvt3nJ8zlzp6b_-7s3_YwwlunTNRC&index=2)

[PyCharm Download and Installation] (https://www.youtube.com/watch?v=nR_kJi8P440&list=PLhdRxvt3nJ8zlzp6b_-7s3_YwwlunTNRC&index=3)

## Thermal HC Example

1. From a command prompt, invoke `jupyter notebook ThermalRatingHC.ipynb` to start the Notebook.
2. In the fourth code cell, change the *dss_file* assignment to match your OpenDSS feeder model's location.
3. Execute all code cells and review the documentation in the Notebook.
4. You should obtain the result *Hosting Capacity = 3.42 MW* based on thermal limits.

## Reverse Power HC Example

1. From a command prompt, invoke `jupyter notebook ReversePowerHC.ipynb` to start the Notebook. (If another Notebook is already open in your browser, you may click the Jupyter icon in its menu to open this example.)
2. In the fourth code cell, change the *dss_file* assignment to match your OpenDSS feeder model's location.
3. Execute all code cells and review the documentation in the Notebook.
4. You should obtain the result *Hosting Capacity = 0.28 MW* based on reverse power flow limits. This limit is lower than the thermal HC. Depending on the resource type, it might be increased if the coincident load is higher than 20% of peak generation, e.g., with rooftop solar generation.

## Overvoltage HC Example

1. From a command prompt, invoke `jupyter notebook OvervoltageHC.ipynb` to start the Notebook. (If another Notebook is already open in your browser, you may click the Jupyter icon in its menu to open this example.)
2. In the fourth code cell, change the *dss_file* assignment to match your OpenDSS feeder model's location.
3. Execute all code cells and review the documentation in the Notebook.
4. You should obtain the result *Hosting Capacity = 0.0 MW* based on overvoltage limits. Please note that reactive power control of the DER could mitigate this with non-unity power factor, non-zero reactive power dispatch, volt-var, autonomously adjusting reference voltage, etc. Volt-watt control could also mitigate this limit on hosting capacity.

## Authors
- Paulo Radatz - pradatz@epri.com

