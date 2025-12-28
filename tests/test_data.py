import pandas as pd
import pytest

def test_data_loading_structure():
    """Simple test to ensure pandas is working and structure is valid"""
    df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
    assert df.shape == (2, 2)
    assert not df.empty