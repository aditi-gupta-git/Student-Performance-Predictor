import os
import tempfile

from src.utils import save_object, load_object


def test_save_and_load_object_roundtrip():
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'obj.pkl')
        data = {'a': 1, 'b': [1, 2, 3]}
        save_object(path, data)
        loaded = load_object(path)
        assert loaded == data
