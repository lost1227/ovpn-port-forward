#!/usr/bin/python3
import argparse
import subprocess

DEFAULT_CLIENT_IP = "10.8.0.201"
DEFAULT_SERVER_IP_VPN = "10.8.0.1"

# List rules: sudo iptables -t nat -L --line-numbers
# Delete rule: sudo iptables -t nat -D (PREROUTING|POSTROUTING) 1

parser = argparse.ArgumentParser(description="Forward a port.")
parser.add_argument("port", type=int, help="the port to forward")
parser.add_argument("protocol", choices=["tcp","udp","both"], help="the protocol to forward")
parser.add_argument("--client", default=DEFAULT_CLIENT_IP, help="the client ip address to forward to")
parser.add_argument("--server-vpn", default=DEFAULT_SERVER_IP_VPN, help="the server ip address in the vpn network")

args = parser.parse_args()

if args.protocol == "tcp" or args.protocol == "both":
    dnat = "sudo iptables -t nat -A PREROUTING -p tcp --dport {} -j DNAT --to-dest {}:{}".format(args.port, args.client, args.port)
    snat = "sudo iptables -t nat -A POSTROUTING -d {} -p tcp --dport {} -j SNAT --to-source {}".format(args.client, args.port, args.server_vpn)

    print(dnat)
    subprocess.run(dnat.split())

    print(snat)
    subprocess.run(snat.split())

if args.protocol == "udp" or args.protocol == "both":
    dnat = "sudo iptables -t nat -A PREROUTING -p udp --dport {} -j DNAT --to-dest {}:{}".format(args.port, args.client, args.port)
    snat = "sudo iptables -t nat -A POSTROUTING -d {} -p udp --dport {} -j SNAT --to-source {}".format(args.client, args.port, args.server_vpn)

    print(dnat)
    subprocess.run(dnat.split())

    print(snat)
    subprocess.run(snat.split())
