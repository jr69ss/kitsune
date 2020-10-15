import random
import socket
import sleep


# Check if website has CloudFlare
def ifCloudFlare(siteURL):
    parsedUri = urlparse(siteURL)
    domain = "{uri.netloc}".format(uri=parsed_uri)
    try:
        origin = socket.gethostbyname(domain)
        iprange = requests.get("https://www.cloudflare.com/ips-v4").text
        ipv4 = [row.rstrip() for row in iprange.splitlines()]
        for i in range(len(ipv4)):
            if ipaddress.ip_address(origin) in ipaddress.ip_network(ipv4[i]):
                print(
                "The site is protected by CloudFlare. Now attempting to find origin servers of website."
                )
                sleep(1)
    except socket.gaierror:
        return False




# Get Random IP
def RandomIP():
    ip = []
    for _ in range(0, 4):
        ip.append(str(random.randint(1, 255)))
    return ".".join(ip)
