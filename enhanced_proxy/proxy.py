import ipaddress
import re
from pathlib import Path
from typing import List, Literal, Union

from pydantic import BaseModel


Protocol = Literal["http", "https", "socks4", "socks5"]
PROXY_FORMATS_REGEXP = [
    re.compile(r'^(?:(?P<protocol>https?|socks[45])://)?(?P<login>[^:]+):(?P<password>[^@|:]+)[@|:](?P<host>[^:]+):(?P<port>\d+)$'),
    re.compile(r'^(?:(?P<protocol>https?|socks[45])://)?(?P<host>[^:]+):(?P<port>\d+)[@|:](?P<login>[^:]+):(?P<password>[^:]+)$'),
    re.compile(r'^(?:(?P<protocol>https?|socks[45])://)?(?P<host>[^:]+):(?P<port>\d+)$'),
    re.compile(r'^(?:(?P<protocol>https?|socks[45])://)?(?:\[(?P<host>[^]]+)\]):(?P<port>\d+)[@|:](?P<login>[^:]+):(?P<password>[^:]+)$'),
    re.compile(r'^(?:(?P<protocol>https?|socks[45])://)?(?P<login>[^:]+):(?P<password>[^@|:]+)[@|:](?:\[(?P<host>[^]]+)\]):(?P<port>\d+)$'),
    re.compile(r'^(?:(?P<protocol>https?|socks[45])://)?(?:\[(?P<host>[^]]+)\]):(?P<port>\d+)$'),
]

def _load_lines(filepath: Path | str) -> List[str]:
    try:
        with open(filepath, "r") as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")
    except IOError as e:
        raise IOError(f"Error reading file: {filepath} - {str(e)}")


class Proxy(BaseModel):
    host: str
    port: int
    protocol: Protocol
    login:    str | None = None
    password: str | None = None

    @classmethod
    def from_str(cls, proxy: Union[str, "Proxy"]) -> "Proxy":
        if type(proxy) is cls or issubclass(type(proxy), cls):
            return proxy

        for pattern in PROXY_FORMATS_REGEXP:
            match = pattern.match(proxy)
            if match:
                groups = match.groupdict()
                return cls(
                    host=groups["host"],
                    port=int(groups["port"]),
                    protocol=Protocol(groups.get("protocol", "http")),
                    login=groups.get("login"),
                    password=groups.get("password"),
                )

        raise ValueError(f'Unsupported proxy format: {proxy}')

    @classmethod
    def from_file(cls, filepath: Path | str) -> List["Proxy"]:
        return [cls.from_str(proxy) for proxy in _load_lines(filepath)]

    @property
    def as_url(self) -> str:
        try:
            ipaddress.ip_address(self.host)
            host = f"[{self.host}]" if ":" in self.host else self.host
        except ValueError:
            host = self.host
        return (f"{self.protocol}://"
                + (f"{self.login}:{self.password}@" if self.login and self.password else "")
                + f"{host}:{self.port}")

    @property
    def server(self) -> str:
        try:
            ipaddress.ip_address(self.host)
            host = f"[{self.host}]" if ":" in self.host else self.host
        except ValueError:
            host = self.host
        return f"{self.protocol}://{host}:{self.port}"

    def __repr__(self):
        return f"Proxy(host={self.host}, port={self.port}, protocol={self.protocol})"

    def __str__(self) -> str:
        return self.as_url

    def __hash__(self):
        return hash((self.host, self.port, self.protocol, self.login, self.password))

    def __eq__(self, other):
        if isinstance(other, Proxy):
            return (
                self.host == other.host
                and self.port == other.port
                and self.protocol == other.protocol
                and self.login == other.login
                and self.password == other.password
            )
        return False
