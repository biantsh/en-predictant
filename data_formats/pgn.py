"""Module for handling PGN (Portable Game Notation) data."""

from __future__ import annotations

import json

from typing import TextIO


class PGNParser:
    def __init__(self, pgn_content: str) -> None:
        components = pgn_content.split('\n\n')
        metadata, moves = components[::2], components[1::2]

        self._matches = []

        for metadata, moves in zip(metadata, moves):
            tags = metadata.split('\n')
            match = PGNMatch(tags, moves)

            self._matches.append(match)

    @classmethod
    def from_file(cls, pgn_file: TextIO) -> PGNParser:
        pgn_content = pgn_file.read()
        return cls(pgn_content)

    @property
    def matches(self) -> list[PGNMatch]:
        return self._matches


class PGNMatch:
    def __init__(self, tags: list[str], moves: str) -> None:
        self._tags = {}
        self._moves = moves

        for tag in tags:
            tag = tag.replace('[', '').replace(']', '').replace('"', '')
            tag_name, tag_value = tag.split(' ', maxsplit=1)

            self._tags[tag_name] = tag_value

    def __getitem__(self, tag_name: str) -> str:
        if not self.has_tag(tag_name):
            raise ValueError(f'PGNMatch has no tag {tag_name}')

        return self._tags[tag_name]

    @property
    def tags(self) -> dict:
        return self._tags

    @property
    def moves(self) -> str:
        return self._moves

    def to_json(self, json_file: TextIO, tag_names=None) -> None:
        if tag_names is None:
            tag_names = self._tags.keys()

        json_content = {tag: val for tag, val in self._tags.items()
                        if tag in tag_names}
        json_content.update({'Moves': self._moves})

        json.dump(json_content, json_file, indent=2)

    def has_tag(self, tag_name: str) -> bool:
        return tag_name in self._tags and '?' not in self._tags[tag_name]
