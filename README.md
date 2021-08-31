# Schlager AI

Schlager lyric generation using transformers

## Setup

**Requirements**
* Python 3.8
* pip 19.0 or later `pip install --upgrade pip`

**Environment Setup**
1. Create virtual environment
`python3 -m venv .venv`
2. Activate virtual environment
`source .venv/bin/activate` (Linux) or `source .venv/Scripts/activate` (Windows)
3. Update pip
`pip install --upgrade pip`
4. **CUDA 10.2 only** change `torch==1.8.2+cu111` to `torch==1.8.2+cu102`
5. Install requirements
`pip install -r requirements.txt -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html`
6. Install dev requirements
`pip install -r requirements-dev.txt`
7. Install schlag package in edit mode
`pip install -e .`
8. Setup Genius and Spotify developer accounts and set `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET` and `GENIUS_TOKEN` environment variables (optionally in `.env` to be used by dotenv)


## Usage

1. Scrape dataset `scripts/scraper.py`
2. Train model `scripts/train.py`
3. Generate text `scripts/generate.py`

## Repo Structure

The following is the basic structure for organizing code. It is suggested that you follow this
format to help standardize projects in the cluster. However, it is possible to add/change names of
submodules under `schlag` and to add further configuration files for other tools + Dockerfiles.

```
root/
|   requirements.txt : Required python modules and versions.
|   requirements-dev.txt : Required python modules and versions for development.
|   setup.cfg : Tool configuration file.
|   setup.py : For creating the schlag module.
|
└───schlag/ : schlag package source.
|   |   config.py : Shared config file.
|   |
|   └───data/ : Data processing pipeline code.
|
└───data/ : Raw/processed training data.
|
└───results/ : Where any training/analysis artifacts are output.
|
└───scripts/ : All CLI scripts.
```

## Development

### Git Workflow
We follow the [feature branch workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)
in this project. To contribute code, please create a branch off of `master` with a descriptive
identifier. When the code is ready and stable, please create a merge request and assign a reviewer.
Once approved, the code will be merged into `master` and the feature branch will be deleted.

### Code Formatters
* [Black](https://github.com/psf/black) is used for formatting. To use, just run
`black {source_file_or_directory}`.
* [isort](https://github.com/PyCQA/isort) is used for sorting imports. To use, just run
`isort {sorce_file_or_directory}`.

### Code Linting
* [pylint](https://www.pylint.org/) is used for linting. To use, just run
`pylint {source_file_or_directory}`.
