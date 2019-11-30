# twisted-dnslabs

DNS testing ground based on twisted.

## Zone manager with friendly words for IPs

Assign a zone to your `/64` block and give friendly names like:

  academy-podium-medical.yggdrasil.ungleich.cloud

to your jails, virtual machines, self-hosted services, ...

This is deployed for the [yggdrasil][ygg] experimental network on
`yggdrasil.ungleich.cloud`.

In order to get a name assigned to you, execute from an [yggdrasil][ygg]
enabled system:

    curl yggdrasil.ungleich.cloud/register

This operation is idempotent and the three words are derived from your
client's IP address (*).

(*): Since the space of words is significantly smaller than that of IPs,
     this service requires some state and assigns the combination of words
     on a first-come first-served basis.
     The algorithm further iterates to try to find a name for an IP but makes
     no promises of this being possible.
     Do host your own!

## DNSEcho

Use this to, for example, echo back an IPv4 as an `A` record on IPv6-only
environments that have DNS64 and NAT64 setup.
That way, your local DNS will add `AAAA` records that will enable your
IPv6-only machines to connect to raw IPv4 addresses without domain.

This is deployed on `echo4.dnslab.evilham.com`(**), use like this:

    `host 127.0.0.8.echo4.dnslab.evilham.com`

That will return an `A` record with `127.0.0.8` as an address.
In DNS64+NAT64 environemnts you'll also see a `AAAA` record with `127.0.0.8`
embedded in your NAT64's IPv6 prefix.

(**): Hosted on a best-effort basis :-).
      Host your own if you want to depend on it.
