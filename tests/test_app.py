from app import index


def test_index():
    assert index() == "Hello, World!, How are you? what about your job?"
