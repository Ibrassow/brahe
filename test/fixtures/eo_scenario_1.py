import json
import pytest

import brahe.data_models as bdm
from .paths import TEST_DATA

# Load Spacecraft
@pytest.fixture
def eo1_spacecraft():
    filepath = TEST_DATA / 'spacecraft.json'
    spacecraft_json = json.load(open(filepath, 'r'))
    yield [bdm.Spacecraft(**s) for s in spacecraft_json]

# Load Stations
@pytest.fixture
def eo1_stations():
    filepath = TEST_DATA / 'stations.json'
    station_json = json.load(open(filepath, 'r'))
    yield [bdm.Station(**s) for s in station_json]

# Load Tiles
@pytest.fixture
def eo1_tiles():
    # filepath = TEST_DATA / 'tiles.json'
    # tile_json = json.load(open(filepath, 'r'))
    # yield [bdm.Tile(**t) for t in tile_json]
    pass

# Load Contacts
@pytest.fixture
def eo1_contacts():
    # filepath = TEST_DATA / 'contacts.json'
    # contact_json = json.load(open(filepath, 'r'))
    # yield [bdm.Contact(**t) for c in contact_json]
    pass

# Load Collects
@pytest.fixture
def eo1_collects():
    # filepath = TEST_DATA / 'collects.json'
    # collect_json = json.load(open(filepath, 'r'))
    # yield [bdm.Collect(**t) for c in collect_json]
    pass