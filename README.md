# jaisting

This is hosting system of jail of paravirtualization system  for FreeBSD.

## Requirements

* FreeBSD (=> 11.2-RELEASE)
* Python (=> 3.6)
* iocage
* libioc
* yarn
* postgresql-server

## Install

```bash
% sudo pkg update
% sudo pkg install python37 py36-psycopg2 py36-ucl yarn postgresql11-server rsync
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

## iocage activate

This project needs activate a zpool.
Click here for more info.

* https://github.com/iocage/iocage

```bash
% git clone https://github.com/iocage/iocage.git
% cd iocage
% sudo make install
% sudo python3.6 -m pip install -r requirements.txt
% sudo python3.6 -m pip install -r requirements-dev.txt
% sudo iocage activate ZPOOL
% sudo iocage fetch
```

## Optional

If package version and Django version wants separate for Python of environments,
It can used venv like below setting.

```bash
% python3.7 -m venv jaisting
% soucrce jaisting/bin/activate (zsh)
```

## Setting

Please change line of following file that your server name or ip by address.

* https://github.com/himrock922/jaisting/blob/master/jaisting/settings.py#L28
* https://github.com/himrock922/jaisting/blob/master/frontend/packs/store/index.js#L13

## Usage

```bash
% cd server/jaisting
% pip install Cython==0.29.3
% pip install -r requirements.txt
% yarn install
% ./node_modules/.bin/webpack --config webpack.config.js --mode=development
% sudo python3.7 manage.py runserver 0.0.0.0:8080
```

## LICENSE

### jaisting

```bash
Copyright (c) 2019, himrock922
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies,
either expressed or implied, of the FreeBSD Project.
```

### iocage

```bash
Copyright (c) 2014-2019, iocage
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted providing that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
```

### libioc

```bash
Copyright (c) 2017-2019, Stefan Grönke
Copyright (c) 2014-2018, iocage
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted providing that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
```

## Reference

* [iocage](https://github.com/iocage/iocage)
* [libioc](https://github.com/bsdci/libioc)
