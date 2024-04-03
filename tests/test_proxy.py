from enhanced_proxy import Proxy

def test_from_str():
    proxy_str = "http://user:password@192.168.0.1:8080"
    proxy = Proxy.from_str(proxy_str)
    assert proxy.host == "192.168.0.1"
    assert proxy.port == 8080
    assert proxy.protocol == "http"
    assert proxy.login == "user"
    assert proxy.password == "password"