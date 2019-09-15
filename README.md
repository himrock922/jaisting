# jaisting

This is hosting system of jail of paravirtualization system  for FreeBSD.

## Requirements

* FreeBSD (=> 11.2-RELEASE)
* Python (=> 3.6)
* libioc
* yarn
* postgresql-server

## Install

```bash
% sudo pkg update
% sudo pkg install python37 py36-psycopg2 py36-ucl yarn postgresql11-server rsync chromium
% mkdir server
% cd server
% git clone git@github.com:himrock922/jaisting.git
```

## PostgreSQL

```bash
% vim /etc/rc.conf
postgresql_enable="YES"
% sudo /usr/local/etc/rc.d/postgresql initdb
% sudo -u postgres createuser <username>
% sudo -u postgres createdb <dbname>
% sudo su - postgres psql
psql=# alter user <username> with encrypted password '<password>';
psql=# grant all privileges on database <dbname> to <username>;
% python3.7 manage.py migrate
```

### Admin User

```bash
python3.7 manage.py createsuperuser
```

## Optional

If package version and Django version wants separate for Python of environments,
It can used venv like below setting.

```bash
% python3.7 -m venv jaisting
% source jaisting/bin/activate (zsh)
```

## Setting

Please change line of following file that your server name or ip by address.

* https://github.com/himrock922/jaisting/blob/master/jaisting/settings.py#L28
* https://github.com/himrock922/jaisting/blob/master/frontend/packs/store/index.js#L13

## Usage

```bash
% cd server/jaisting
% pip install Cython==0.29.5
% pip install -r packages.txt
% yarn install
% ./node_modules/.bin/webpack --config webpack.config.js --mode=development
% sudo python3.7 manage.py runserver 0.0.0.0:8080
```

## IPFW + NAT

### Host Configuration

To start ipfw and natd services, that changes /etc/rc.conf like as below config.

```
% sudo vim /etc/rc.conf
gateway_enable="YES"
firewall_type="open"
firewall_enable="YES"
firewall_script="/etc/rc.firewall"
natd_enable="YES"
natd_interface="wan_interface"
natd_flags="-f /etc/natd.conf"


% sudo echo "net.link.ether.ipfw=1" >> /etc/sysctl.conf
% sudo echo "net.link.bridge.ipfw=1" >> /etc/sysctl.conf
% sudo echo "security.jail.allow_raw_sockets=1" >> /etc/sysctl.conf

% sudo vim /etc/natd.conf
redirect_address {lan_network} {wan_network}

% sudo service ipfw restart
% sudo service natd restart
```

To intercommunication with host and jail, it is need create brdige interface.

```
% sudo ifconfig bridge0 create
% sudo ifconfig bridge0 {brdige_ip_address}/${subnet}

# permanent settings
% sudo vim /etc/rc.conf
cloned_interfaces="bridge0"
ifconfig_bridge0="inet {bridge_ip_address} netmask {subnet}"
ifconfig_brdige0="addm wan_interface"
```

ipfw sample config

```
% sudo vim /etc/rc.firewall
${fwcmd} add 00316 allow tcp from me {port_number} to any
${fwcmd} add 00318 allow tcp from any to me {port_number}
${fwcmd} add 10010 skipto 63000 tcp from any to me {port_numbers} setup keep-state
${fwcmd} add 10011 skipto 63000 icmp from any to any setup keep-state
${fwcmd} add 64000 divert natd ip from any to any via {oif} in
${fwcmd} add 64001 divert natd ip from any to any via {oif} out
${fwcmd} add 65000 allow ip from any to any
${fwcmd} add 65535 deny ip from any to any
```

### jail Configuration

```
route add default {bridge_ipaddress}
```

jaisting is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for the full license text.
