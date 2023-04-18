import json
import sys


def sort_key(feature):
    return feature['properties']['SSID']


def format_and_sort_geojson(input_file):
    with open(input_file, 'r') as f:
        geojson_data = json.load(f)

    for feature in geojson_data['features']:
        if 'Notes' in feature['properties'] and not feature['properties']['Notes']:
            del feature['properties']['Notes']

    sorted_features = sorted(geojson_data['features'], key=sort_key)
    geojson_data['features'] = sorted_features

    with open(input_file, 'w') as f:
        json.dump(geojson_data, f, indent=2)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python format.py <input_geojson_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    format_and_sort_geojson(file_path)
    print(f"Formatted GeoJSON file: {file_path}")
