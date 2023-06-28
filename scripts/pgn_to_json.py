"""Convert a PGN dataset of chess matches to JSON.

Each match is written in a separate JSON file, which has the benefit of being
able to load matches individually without loading the entire dataset.

Example usage:
    python3 pgn_to_jon.py  \
      --pgn_dir pgn_datasets/  \
      --output_dir json_dataset/
"""

import argparse
import glob
import os

from data_formats.pgn import PGNParser

TAGS = ['Event', 'WhiteElo', 'BlackElo']
MATCH_TYPE = 'Rated Blitz game'


def main(pgn_dir: str, output_dir: str) -> None:
    pgn_paths = glob.glob(f'{pgn_dir}/*.pgn')
    json_count = 0

    for pgn_path in pgn_paths:
        with open(pgn_path, 'r', encoding='ISO-8859-1') as pgn_file:
            pgn_parser = PGNParser.from_file(pgn_file)

        for pgn_match in pgn_parser.matches:
            if not all(pgn_match.has_tag(tag) for tag in TAGS):
                continue

            if pgn_match['Event'] != MATCH_TYPE:
                continue

            if '{' in pgn_match.moves:
                continue

            json_name = f'{json_count:010}.json'
            json_count += 1

            output_path = os.path.join(output_dir, json_name)
            with open(output_path, 'w') as json_file:
                pgn_match.to_json(json_file, tag_names=TAGS)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--pgn_dir', type=str, required=True)
    parser.add_argument('-o', '--output_dir', type=str, required=True)

    args = parser.parse_args()
    main(args.pgn_dir, args.output_dir)
