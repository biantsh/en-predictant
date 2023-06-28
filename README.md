# En-predictant

An AI model trained to predict chess Elo.

The project name is a wordplay on the chess meme "en passant".

# Setup and instructions

This project requires `python>=3.10`.  Install code and external requirements 
by running:

```shell
cd en-predictant/
pip install .
```

Download datasets in PGN format from [database.lichess.org](
https://database.lichess.org/#standard_games).

**Scripts:**

- `pgn_split.py`: To split large PGN files into individual files.
- `pgn_to_json.py`: To convert PGN files into JSON.
- `train_model.py`: To train a Keras model for Elo estimation.

