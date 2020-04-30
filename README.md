# ovpn-port-forward

## Purpose
I often find myself in the situation where I would like to forward a tcp or udp 
port to my device, but I am not in control of the wifi network I am currently
connected to. Usually, the process for forwarding a port to your device involves
reconfiguring the gateway of the network you're currently connected to. This
becomes unfeasible if you're not in control of that network.

Sometimes I want to spin up a quick, short-lived minecraft server so that I can 
get online with my friends. Sometimes times I want to test an API callback to a
web service running on my local machine. Sometimes I want to transfer a large
file over the internet, and the best solution is to just host a temporary web
server. These all require port forwarding.

When I'm at college, or at a hotel, or at a friend's house, I do not have
control of the network I am currently connected to. This makes traditional port
forwarding impossible, since I cannot configure the network gateway.

## Solution
My solution is to rent a cheap server instance and host an OpenVPN server, then
configure that server to forward traffic to a specific client. I've found that
an AWS EC2 t2.micro instance running on the free tier is the cheapest option
(it's free!), but I've also had this working on a DigitalOcean droplet using
promotional credit.

## Instructions
I've written up the full instructions in a [separate document](INSTRUCTIONS.md).
