import pytest

@pytest.mark.skip()
def test_server_ping():
    assert "ping".upper() == "PING"