# Clean-CSL-JSON

This repository contains the script to cleanup CSL JSON exported from Zotero, for use in our website

## Requirements

- Python 3.6+

## Usage

```
usage: main.py [-h] [--input INPUT] [--output OUTPUT]

options:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
  --output OUTPUT, -o OUTPUT
```

## Example

You can run the example with the demo file in the repository

```sh
python3 main.py -i input.demo.json -o output.de`mo.json
```

## How to use it with Zotero

1. Add your references to Zotero (better if you use the Zotero connector extension for both Chromium-based and Firefox-based browsers, and add the references directly from the article page rather than Google Scholar page)
2. Select and export your Zotero library in CSL JSON format
3. Run the script with the exported file as input
