# IntelliStar Config Generator

Generates SCMT or XML configuration files for the IntelliStar series of systems for anywhere in the U.S., Canada, or Mexico.

## Requirements

```bash
pip install aiohttp requests
```

Python 3.10+ and `LFRecord.db` in project root.

## Usage

```bash
python3 main.py
```

Enter a location when prompted. Be specific for the best results:
```
Enter the location name: Saskatoon, SK, Canada
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
