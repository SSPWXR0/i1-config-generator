# IntelliStar Config Generator

Generates SCMT configuration files for the domestic IntelliStar system for anywhere in the U.S., Canada, or Mexico.

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

Copy the .py file from the output directory onto your IntelliStar's /home/dgadmin/config/current directory. Load the config via
``` runomni /twc/util/loadSCMTconfig.pyc /home/dgadmin/config/current/config.py```

## Contributing

This program is in a very primitive state as of writing. Contributions are always welcome. Please make a pull request for the changes you would like to add.
