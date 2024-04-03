# Enhanced Proxy

[![PyPI version](https://img.shields.io/pypi/v/enhanced-proxy.svg)](https://pypi.org/project/enhanced-proxy/)
[![Python versions](https://img.shields.io/pypi/pyversions/enhanced-proxy.svg)](https://pypi.org/project/enhanced-proxy/)
[![License](https://img.shields.io/pypi/l/enhanced-proxy.svg)](https://github.com/tsutomu-n/enhanced_proxy/blob/main/LICENSE)
[![GitHub repository](https://img.shields.io/badge/GitHub-enhanced--proxy-blue?logo=github)](https://github.com/tsutomu-n/enhanced_proxy)

`enhanced_proxy` は、Python でプロキシを簡単かつ柔軟に管理するためのライブラリです。このライブラリを使用すると、さまざまな形式のプロキシ文字列からプロキシオブジェクトを作成し、それらを操作することができます。

> プロキシとは、インターネット上で別のコンピュータの代わりに動作するサーバーのことです。プロキシは、元のコンピュータのIPアドレスを隠したり、インターネットトラフィックをフィルタリングしたり、パフォーマンスを向上させたりするために使用されます。

## enhanced_proxy の特徴

- プロキシをオブジェクトとして表現する `Proxy` クラスを提供します。
- さまざまな形式のプロキシ文字列からプロキシオブジェクトを作成できます。
- IPv4 と IPv6 の両方のプロキシをサポートしています。
- プロキシオブジェクトをハッシュ化し、セットで管理できます。
- ファイルからプロキシのリストを読み込むことができます。
- 非同期 HTTP クライアントライブラリと互換性があります。

## インストール

ソースコードからenhanced_proxyをインストールするには、以下の手順に従ってください:

1. リポジトリをクローンします:
   ```
   git clone https://github.com/tsutomu-n/enhanced_proxy.git
   ```

2. クローンしたディレクトリに移動します:
   ```
   cd enhanced_proxy
   ```

3. (オプション) 仮想環境を作成します:
   ```
   python -m venv venv
   source venv/bin/activate  # Unix/Linuxの場合
   venv\Scripts\activate.bat  # Windowsの場合
   ```

4. 必要な依存関係をインストールします:
   ```
   pip install -r requirements.txt
   ```

5. enhanced_proxyをインストールします:
   ```
   python setup.py install
   ```

これらの手順に従うことで、enhanced_proxyがインストールされ、Pythonプロジェクトで使用できるようになります。

## プロキシ文字列の例

プロキシ文字列は、プロキシサーバーの詳細を含む文字列です。enhanced_proxy は、以下のようなさまざまな形式のプロキシ文字列をサポートしています。

- `host:port:login:password`
- `host:port@login:password`
- `host:port|login:password`
- `login:password@host:port`
- `login:password:host:port`
- `host:port`

また、IPv4 と IPv6 の両方のプロキシをサポートしています。IPv6 アドレスは角括弧 `[]` で囲む必要があります。

```
IPv4 (HTTP): http://user:password@192.168.0.1:8080
IPv6 (HTTP): http://user:password@[2001:db8::1]:8080
IPv4 (SOCKS5): socks5://user:password@192.168.0.1:1080
IPv6 (SOCKS5): socks5://user:password@[2001:db8::1]:1080
IPv4 (認証なし): http://192.168.0.1:8080
IPv6 (認証なし): socks5://[2001:db8::1]:1080
```

## コード例

以下は、enhanced_proxy を使用してプロキシオブジェクトを作成し、操作する方法の例です。

```python
from enhanced_proxy import Proxy

# 文字列からプロキシオブジェクトを作成する
http_proxy = Proxy.from_str('http://user:password@192.168.0.1:8080')
socks5_proxy = Proxy.from_str('socks5://user:password@[2001:db8::1]:1080')

# プロキシのプロパティにアクセスする
print(http_proxy.host)  # 出力: 192.168.0.1
print(socks5_proxy.port)  # 出力: 1080
print(http_proxy.protocol)  # 出力: http
print(socks5_proxy.protocol)  # 出力: socks5

# aiohttp と aiohttp_socks を使用する
import aiohttp
from aiohttp_socks import ProxyConnector

async def fetch(url, proxy):
    connector = ProxyConnector.from_url(proxy.as_url)
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url) as response:
            return await response.text()

# HTTP プロキシを使用してウェブページを取得する
result = await fetch('https://example.com', http_proxy)
```

このコード例では、以下のことを行っています。

1. `Proxy.from_str()` メソッドを使用して、文字列からプロキシオブジェクトを作成しています。
2. プロキシオブジェクトのプロパティ（`host`、`port`、`protocol`）にアクセスしています。
3. `aiohttp` と `aiohttp_socks` を使用して、プロキシ経由で非同期にウェブページを取得しています。

## まとめ

enhanced_proxy は、Python でプロキシを簡単かつ柔軟に管理するためのライブラリです。このライブラリを使用すると、さまざまな形式のプロキシ文字列からプロキシオブジェクトを作成し、それらを操作することができます。また、IPv4 と IPv6 の両方のプロキシをサポートし、非同期 HTTP クライアントライブラリと互換性があります。

プロキシは、インターネット上で別のコンピュータの代わりに動作するサーバーであり、元のコンピュータのIPアドレスを隠したり、インターネットトラフィックをフィルタリングしたり、パフォーマンスを向上させたりするために使用されます。enhanced_proxy を使用すると、これらのプロキシを簡単に管理し、Python のプロジェクトに統合することができます。