import os

def test_synthetic_data_file_exists():
    assert os.path.exists("data/synthetic_events.json")
