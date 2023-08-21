import json
import os
from argparse import ArgumentParser
from hashlib import md5

argparser = ArgumentParser()
argparser.add_argument("--input", "-i", type=str, default="input.json")
argparser.add_argument("--output", "-o", type=str, default="output.json")
args = argparser.parse_args()

# Check if input file exists
if not os.path.exists(args.input):
    print(f"Input file not found: {args.input}")
    exit(1)
elif not os.path.isfile(args.input):
    print(f"Input file is not a file: {args.input}")
    exit(1)

# Try to load input file
try:
    with open(args.input, "r") as f:
        data = json.load(f)
except Exception as e:
    print(f"Could not load input file: {e}")
    exit(1)

# Check if input file is valid
if not isinstance(data, list) or not data:
    print(f"Input file is not a list or empty: {args.input}")
    exit(1)


# Format items
def format_item(item: dict):
    item = {k: v for k, v in item.items() if k not in ["abstract"]}
    item["id"] = md5(item["title"].encode()).hexdigest()
    return item


data = [format_item(entry) for entry in data]

# Write output file
with open(args.output, "w") as f:
    json.dump(data, f, indent=2)

# Get stats
intput_file_size = os.path.getsize(args.input)
output_file_size = os.path.getsize(args.output)

print(
    f"Successfully formatted {len(data)} items in {args.input}: {intput_file_size}B -> {output_file_size}B ({output_file_size/intput_file_size*100:.2f}%)"
)
