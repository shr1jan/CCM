import sys
import os
from pathlib import Path

root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

import pytest

@pytest.fixture
def test_corpus():
    """Provides a test corpus for citation verification"""
    return {
        "Section 88": True,
        "Article 45": True,
        "National Civil Code 2074": True
    }

@pytest.fixture
def sample_texts():
    """Provides sample texts with and without citations"""
    return {
        "with_valid": "According to Section 88, this is allowed.",
        "with_invalid": "According to Section 999, this is not allowed.",
        "without": "This text has no legal citations."
    }