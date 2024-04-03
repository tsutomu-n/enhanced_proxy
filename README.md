# Enhanced Proxy

[![PyPI version](https://img.shields.io/pypi/v/enhanced-proxy.svg)](https://pypi.org/project/enhanced-proxy/)
[![Python versions](https://img.shields.io/pypi/pyversions/enhanced-proxy.svg)](https://pypi.org/project/enhanced-proxy/)
[![License](https://img.shields.io/pypi/l/enhanced-proxy.svg)](https://github.com/tsutomu-n/enhanced_proxy/blob/main/LICENSE)
[![GitHub repository](https://img.shields.io/badge/GitHub-enhanced--proxy-blue?logo=github)](https://github.com/tsutomu-n/enhanced_proxy)

`enhanced_proxy` is a library for easy and flexible management of proxies in Python. With this library, you can create proxy objects from various formats of proxy strings and manipulate them.

[日本語訳](./README.ja.md)

## What is a Proxy?

A proxy is a server that acts on behalf of another computer on the internet. Proxies are used to hide the original computer's IP address, filter internet traffic, or improve performance.

## Features of enhanced_proxy

- Provides a `Proxy` class to represent proxies as objects.
- Supports creating proxy objects from various formats of proxy strings.
- Supports both IPv4 and IPv6 proxies.
- Allows hashing of proxy objects and managing them in sets.
- Supports loading a list of proxies from a file.
- Compatible with asynchronous HTTP client libraries.

## Installation

To install enhanced_proxy, you can use pip:

```
pip install enhanced-proxy
```

Alternatively, you can install it using poetry:

1. Clone the repository:
   ```
   git clone https://github.com/tsutomu-n/enhanced_proxy.git
   ```

2. Navigate to the cloned directory:
   ```
   cd enhanced_proxy
   ```

3. Install the package and its dependencies using poetry:
   ```
   poetry install
   ```

## Running Tests and Quality Checks

To run tests and quality checks, you can use tox:

```
tox
```

This will run the tests using pytest, perform type checking using mypy, and check code formatting using black.

## Examples of Proxy Strings

A proxy string is a string that contains the details of a proxy server. `enhanced_proxy` supports various formats of proxy strings, such as:

- `host:port:login:password`
- `host:port@login:password`
- `host:port|login:password`
- `login:password@host:port`
- `login:password:host:port`
- `host:port`

It also supports both IPv4 and IPv6 proxies. IPv6 addresses need to be enclosed in square brackets `[]`.

```
IPv4 (HTTP): http://user:password@192.168.0.1:8080
IPv6 (HTTP): http://user:password@[2001:db8::1]:8080
IPv4 (SOCKS5): socks5://user:password@192.168.0.1:1080
IPv6 (SOCKS5): socks5://user:password@[2001:db8::1]:1080
IPv4 (No Authentication): http://192.168.0.1:8080
IPv6 (No Authentication): socks5://[2001:db8::1]:1080
```

## Code Examples

Here are some examples of how to create and manipulate proxy objects using enhanced_proxy:

```python
from enhanced_proxy import Proxy

# Create proxy objects from strings
http_proxy = Proxy.from_str('http://user:password@192.168.0.1:8080')
socks5_proxy = Proxy.from_str('socks5://user:password@[2001:db8::1]:1080')

# Access proxy properties
print(http_proxy.host)  # Output: 192.168.0.1
print(socks5_proxy.port)  # Output: 1080
print(http_proxy.protocol)  # Output: http
print(socks5_proxy.protocol)  # Output: socks5

# Use with aiohttp and aiohttp_socks
import aiohttp
from aiohttp_socks import ProxyConnector

async def fetch(url, proxy):
    connector = ProxyConnector.from_url(proxy.as_url)
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url) as response:
            return await response.text()

# Fetch a web page using the HTTP proxy
result = await fetch('https://example.com', http_proxy)
```

In this code example, we:

1. Use the `Proxy.from_str()` method to create proxy objects from strings.
2. Access the properties of the proxy objects (`host`, `port`, `protocol`).
3. Use `aiohttp` and `aiohttp_socks` to asynchronously fetch a web page through the proxy.

## Contributing

We welcome contributions to enhanced_proxy! If you have an idea for a new feature, or have found a bug, please open an issue on the GitHub repository.

If you would like to contribute code, please fork the repository and create a pull request with your changes. Make sure to follow the existing code style and include tests for any new functionality.

## Support and Feedback

If you have any questions, issues, or feedback regarding enhanced_proxy, please open an issue on the GitHub repository or contact the maintainers at [t_n@seimou.net].

## License

enhanced_proxy is released under the [MIT License](https://github.com/tsutomu-n/enhanced_proxy/blob/main/LICENSE).

## Conclusion

enhanced_proxy is a library for easy and flexible management of proxies in Python. It allows you to create proxy objects from various formats of proxy strings and manipulate them. It supports both IPv4 and IPv6 proxies and is compatible with asynchronous HTTP client libraries.

Proxies are servers that act on behalf of another computer on the internet and are used to hide the original computer's IP address, filter internet traffic, or improve performance. With enhanced_proxy, you can easily manage these proxies and integrate them into your Python projects.
