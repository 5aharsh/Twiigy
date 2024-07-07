# Twiigy

## Requirements
1. Python 3.12+ - [Download](https://www.python.org/downloads/)
2. Poetry - [Installation guide](https://python-poetry.org/docs/)

## Getting Started

Clone the repo 
```bash
git clone https://github.com/5aharsh/Twiigy.git && cd twiggy
```

Start virtual environment
```bash
poetry shell
```

Install dependencies
```bash
poetry install
```

## Scripts

[Zerodha pulse](https://pulse.zerodha.com/) news parser. Data is stored in `twiigy.db.json` at root using `tinydb`
```bash
python twiigy/pulse_parser.py
```