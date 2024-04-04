# tests/test_proxy.py
import unittest
from unittest.mock import patch, MagicMock
import socket
from enhanced_proxy.proxy import proxy_handler, hexdump, receive_from, request_handler, response_handler

class TestProxy(unittest.TestCase):

    def setUp(self):
        self.client_socket = MagicMock()
        self.remote_host = "www.example.com"
        self.remote_port = 80

    def test_proxy_handler(self):
        # プロキシハンドラの正常系テスト
        with patch('enhanced_proxy.proxy.socket.socket') as mock_socket:
            mock_remote_socket = MagicMock()
            mock_socket.return_value = mock_remote_socket
            proxy_handler(self.client_socket, self.remote_host, self.remote_port, False)

            # クライアントからのデータ送信とリモートホストへの転送をテスト
            self.client_socket.recv.return_value = b"GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n"
            proxy_handler(self.client_socket, self.remote_host, self.remote_port, False)
            mock_remote_socket.send.assert_called_with(b"GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n")

            # リモートホストからのデータ受信とクライアントへの転送をテスト
            mock_remote_socket.recv.return_value = b"HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n"
            proxy_handler(self.client_socket, self.remote_host, self.remote_port, False)
            self.client_socket.send.assert_called_with(b"HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n")

    def test_hexdump(self):
        # hexdumpのテスト
        data = b"Hello, World!"
        with self.assertLogs() as captured:
            hexdump(data)
            self.assertEqual(len(captured.records), 1)
            self.assertIn("0000   48 65 6c 6c 6f 2c 20 57 6f 72 6c 64 21        Hello, World!", captured.records[0].getMessage())

    def test_receive_from(self):
        # receive_fromのテスト
        mock_socket = MagicMock()
        mock_socket.recv.side_effect = [b"Hello", b"", b"World"]
        buffer = receive_from(mock_socket)
        self.assertEqual(buffer, b"HelloWorld")

        # タイムアウトのテスト
        mock_socket.recv.side_effect = socket.timeout()
        buffer = receive_from(mock_socket)
        self.assertEqual(buffer, b"")

    def test_request_handler(self):
        # request_handlerのテスト
        data = b"GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n"
        result = request_handler(data)
        self.assertEqual(result, data)  # デフォルトでは変更なし

    def test_response_handler(self):
        # response_handlerのテスト
        data = b"HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n"
        result = response_handler(data)
        self.assertEqual(result, data)  # デフォルトでは変更なし

if __name__ == "__main__":
    unittest.main()
