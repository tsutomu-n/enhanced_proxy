import unittest
from unittest.mock import patch, mock_open
from enhanced_proxy.proxy import EnhancedProxy

class TestEnhancedProxy(unittest.TestCase):
    def setUp(self):
        self.proxy = EnhancedProxy()

    def test_init(self):
        """EnhancedProxyクラスが正しく初期化されることをテスト"""
        self.assertIsInstance(self.proxy, EnhancedProxy)

    @patch('enhanced_proxy.proxy.EnhancedProxy.read_proxy_file')
    def test_get_proxies(self, mock_read_proxy_file):
        """get_proxiesメソッドが正しくプロキシリストを取得することをテスト"""
        mock_read_proxy_file.return_value = ['http://proxy1.com', 'http://proxy2.com']
        proxies = self.proxy.get_proxies()
        self.assertEqual(proxies, ['http://proxy1.com', 'http://proxy2.com'])

    def test_filter_proxies(self):
        """filter_proxiesメソッドが正しくプロキシをフィルタリングすることをテスト"""
        proxies = ['http://proxy1.com', 'http://proxy2.com', 'http://proxy3.com']
        filtered_proxies = self.proxy.filter_proxies(proxies, min_speed=100)
        self.assertEqual(len(filtered_proxies), 2)

    @patch('enhanced_proxy.proxy.requests.get')
    def test_check_proxy(self, mock_get):
        """check_proxyメソッドが正しくプロキシの有効性をチェックすることをテスト"""
        mock_get.return_value.status_code = 200
        is_valid = self.proxy.check_proxy('http://proxy1.com')
        self.assertTrue(is_valid)
