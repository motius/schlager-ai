# -*- coding: utf-8 -*-
"""schlag module config

Includes paths related to project directory
"""
import os
from pathlib import Path

from dotenv import load_dotenv

# Project Directory paths
ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"
RESULTS_DIR = ROOT_DIR / "results"
RESOURCES_DIR = ROOT_DIR / "resources"


# Loads environment variable secrets
load_dotenv(ROOT_DIR / ".env")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
GENIUS_TOKEN = os.getenv("GENIUS_TOKEN")
