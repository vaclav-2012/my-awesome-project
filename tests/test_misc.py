from unittest.mock import Mock, call


def test_mock():
    """Test mock."""
    my_mock = Mock()

    my_mock.method("test")

    assert my_mock.method.call_args == call("test")
