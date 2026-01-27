# IntelliStar Config Generator

Generates SCMT or XML configuration files for the IntelliStar series of systems for anywhere in the U.S., Canada, or Mexico.

- **IntelliStar 1 Domestic (Pre-WATT, 2003-2013)**: Config generation for the Domestic IntelliStars from its release in 2003 up until the major 2013 rebrand.
- **IntelliStar 1 Domestic Enhanced/WATT (2013-2015)**: Experimental support for the Domestic IntelliStars from the 2013 rebrand to the 2015 decommissioning.
- **IntelliStar 1 Weatherscan (2003-2022)**: Supports IntelliStars running the Weatherscan package.
- **IntelliStar 2 (XD/HD/Jr)**: Generates `MachineProductCfg.xml` compatible with all IntelliStar 2 systems.

## Requirements

```bash
pip install aiohttp requests
```

Python 3.10+ and `LFRecord.db` in project root.

## Usage

```bash
python3 main.py
```
Select the default option to use the `input.yaml` template. You would need to edit the file with your desired locations.

Alternatively:

Enter a location when prompted. Select the second option to build a configuration interactively.
```
Enter the location name: Saskatoon
```

Config files are generated in `output/` directory.

## Deployment

### IntelliStar 1 Weatherscan/Domestic:

Copy the .py file from the output directory onto your IntelliStar's `/home/dgadmin/config/current` directory. Load the config via
``` runomni /twc/util/loadSCMTconfig.pyc /home/dgadmin/config/current/config.py```

### IntelliStar 2 HD/Jr/xD:
Copy the .xml file from the output directory into `C:\Program Files (x86)\TWC\I2\Managed\Config\MachineProductCfg.xml`. Keep the name "MachineProductCfg.xml".

## Contributing

Contributions are always welcome. Please make a pull request for the changes you would like to add.
