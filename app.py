#!/usr/bin/env python3

from twisted.application import internet
from twisted.internet import endpoints, reactor
from twisted.names import dns, server
from twisted.web.server import Site

from dnswords import WordsController


# TODO: Make config prettier
try:
    from config import config
except ImportError:
    import sys

    sys.stdout.write("\n***\nYou need to setup config.py, see config.sample.py\n***\n")
    sys.exit(1)


def main():
    from twisted.names import cache

    dns_cache = [cache.CacheResolver(verbose=config["verbose"])]
    dns_clients = []

    tcp_f = server.DNSServerFactory(
        config["zones"], dns_cache, dns_clients, config["verbose"]
    )
    udp_f = dns.DNSDatagramProtocol(tcp_f)

    tcp_s = internet.TCPServer(
        config["dnsport"], tcp_f, interface=config["dnsinterface"]
    )
    udp_s = internet.UDPServer(
        config["dnsport"], udp_f, interface=config["dnsinterface"]
    )

    # Start DNS services
    tcp_s.startService()
    udp_s.startService()

    if WordsController.data:
        # Create HTTP server endpoint only if at least a zone is registered
        endpoint = endpoints.serverFromString(reactor, config["apiendpoint"])
        endpoint.listen(Site(WordsController.app.resource()))

    print("Starting reactor")
    reactor.run()


if __name__ == "__main__":
    main()
