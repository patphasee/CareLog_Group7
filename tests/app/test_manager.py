import pytest
import os
import json
from src.app.manager import Manager


def read_json(path: Path) -> dict:
    return json.loads(path.read_text())
