import sys
import os

# tests/test_proxy.py
import pytest
from pathlib import Path
from enhanced_proxy.proxy import Proxy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_from_str():
    proxy_str = "http://user:password@192.168.0.1:8080"
    proxy = Proxy.from_str(proxy_str)
    assert proxy.host == "192.168.0.1"
    assert proxy.port == 8080
    assert proxy.protocol == "http"
    assert proxy.login == "user"
    assert proxy.password == "password"
def test_from_str_invalid_protocol():
    proxy_str = "invalid://user:password@192.168.0.1:8080"
    with pytest.raises(ValueError, match="Invalid protocol: invalid"):
        Proxy.from_str(proxy_str)
def test_from_str_unsupported_format():
    proxy_str = "unsupported_format"
    with pytest.raises(ValueError, match=f"Unsupported proxy format: {proxy_str}"):
        Proxy.from_str(proxy_str)
def test_from_file(tmp_path):
    proxy_file = tmp_path / "proxies.txt"
    proxy_file.write_text("http://user:password@192.168.0.1:8080\nsocks5://user:password@[2001:db8::1]:1080")
    proxies = Proxy.from_file(proxy_file)
    assert len(proxies) == 2
    assert proxies[0].host == "192.168.0.1"
    assert proxies[1].host == "2001:db8::1"
def test_from_file_not_found():
    with pytest.raises(FileNotFoundError):
        Proxy.from_file("nonexistent_file.txt")
def test_as_url():
    proxy = Proxy(host="192.168.0.1", port=8080, protocol="http", login="user", password="password")
    assert proxy.as_url == "http://user:password@192.168.0.1:8080"
def test_server():
    proxy = Proxy(host="192.168.0.1", port=8080, protocol="http")
    assert proxy.server == "http://192.168.0.1:8080"
def test_repr():
    proxy = Proxy(host="192.168.0.1", port=8080, protocol="http")
    assert repr(proxy) == "Proxy(host=192.168.0.1, port=8080, protocol=http)"
def test_str():
    proxy = Proxy(host="192.168.0.1", port=8080, protocol="http", login="user", password="password")
    assert str(proxy) == "http://user:password@192.168.0.1:8080"
def test_hash():
    proxy1 = Proxy(host="192.168.0.1", port=8080, protocol="http")
    proxy2 = Proxy(host="192.168.0.1", port=8080, protocol="http")
    assert hash(proxy1) == hash(proxy2)
def test_eq():
    proxy1 = Proxy(host="192.168.0.1", port=8080, protocol="http")
    proxy2 = Proxy(host="192.168.0.1", port=8080, protocol="http")
    assert proxy1 == proxy2