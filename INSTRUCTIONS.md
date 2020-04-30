# Instructions

## Setup a remote server

### Chose a hosting provider
The first step is to chose a hosting platform and set up an OpenVPN server on
that platform.

Options include (but are far from limited to):
- [AWS EC2](https://aws.amazon.com/ec2/)
- [DigitalOcean Droplets](https://www.digitalocean.com/products/droplets/)
- A spare machine running on your home network

For the rest of this guide, I'm going to be explaining how to use AWS EC2, just
because it's the most economical option for my situation.

### Start an instance
Start a new server on the hosting provider you chose. Make sure to choose an
operating server that runs the OpenVPN server software. For this guide, I'll
be using Ubuntu Server 18.04 LTS.

Make sure your instance has a public ip address, and that there aren't any
firewalls blocking the ports you need to forward (if the traffic can't even get
to your server, it definitely can't be forwarded by your server). Also make sure
ports tcp 22 (for ssh) and udp 1194 (for OpenVPN) are open.

Make sure you can access your server over SSH. I'd recommend setting up public/
private key authentication, but that's optional.

## Setup the OpenVPN server software
There's too much involved in this for me to cover, and there are already a lot
of good guides that cover this part. I reccomend you use [this](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-openvpn-server-on-ubuntu-18-04)
guide from DigitalOcean, with the modifications which I will describe below.

### Step 4: This will be your client certificate
For this application, we're only ever going to be forwarding to one client. So
the client certificate you generate in this step will be the client certificate
you end up using. So give it a good name, and **remember that name**.

### Step 5: Server Configuration
Instead of using the sample config file they describe, use the 
server config file [provided in this repository](server.conf).

### Step 5.5: Client Configuration Directory
Create the directory /etc/openvpn/ccd
```
sudo mkdir /etc/openvpn/ccd
```
In that directory, create a new file with the same name used when generating the
client certificate. So, when you ran the command
`./easy-rsa gen-req [NAME] nopass` back in step 4, you named the client `[NAME]`.
That same `[NAME]` **must** be the name of the new file.
```
sudo nano /etc/openvpn/ccd/[NAME]
```
In that file, put the following line:
```
ifconfig-push 10.8.0.201 255.255.255.0
```

### Step 8: Client Configuration
Instead of using the same sample config file they describe, use
the client config file [provided in this repository](base.conf). However, you
you should still use their script for combining the client configuration with
the client keys, just instead of using `base.conf` they desciribe, use the
`base.conf` provided here. **You will still need to edit it and set the server's ip**.

## Connect to the server
Install the OpenVPN client on your computer. Then, using a program like
[WinSCP](https://winscp.net/eng/index.php), copy the client file created in step
9 to your computer. Install the configuration as described in step 10.

Try to connect to the server. Make sure that the connection succeedes.
Troubleshoot if it does not.


## Setup port forwarding
SSH into the server and copy [this script](ports.py) to your home folder.
Then connect to the vpn.

Once you're connected to the VPN, ssh into the server and use the script to
forward the desired server ports to your computer.

The syntax of the script is:
```
python3 [port number] {tcp, udp, both}
```
The first argument `[port number]` specifies which port to forward.
The second argument, which is one of `tcp`, `udp`, or `both`, specifies what
protocol to forward.

## Finished!
That should be it! Any traffic to a forwarded port using the server's ip will be
directed to your machine, so long as you are connected to the VPN.

If you ever reboot the server (for example, after an update), you'll have to run
the port script again to forward your ports. Also, if you don't plan to forward
the port all the time, it may be more economical to only start the server
instance whenever you need it and shut it down when you're not using it.
