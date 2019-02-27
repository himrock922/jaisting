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

## LICENSE for other packages

### Django

https://github.com/django/django/blob/master/LICENSE

### gitdb

https://github.com/gitpython-developers/gitdb/blob/master/LICENSE

### GitPython

https://github.com/gitpython-developers/GitPython/blob/master/LICENSE

### libioc

https://github.com/bsdci/libioc/blob/master/LICENSE.txt

### py-freebsd_sysctl

https://github.com/gronke/py-freebsd_sysctl/blob/master/LICENSE.txt

### py-jail

https://github.com/gronke/py-jail/blob/master/LICENSE.txt

### py-libzfs

https://github.com/freenas/py-libzfs/blob/0d930aabd7b9a58efd63f2348f09bb73af135a39/setup.py

### psycopg2

http://initd.org/psycopg/docs/license.html?highlight=license

### smmap

https://github.com/gitpython-developers/smmap/blob/master/LICENSE

## Reference

* [Django](https://github.com/django/django)
* [gitdb](https://github.com/gitpython-developers/gitdb)
* [GitPython](https://github.com/gitpython-developers/GitPython)
* [libioc](https://github.com/bsdci/libioc)
* [py-freebsd_sysctl](https://github.com/gronke/py-freebsd_sysctl)
* [py-jail](https://github.com/gronke/py-jail)
* [py-libzfs](https://github.com/freenas/py-libzfs)
* [psycopg2](http://initd.org/psycopg/)
* [smmap](https://github.com/gitpython-developers/smmap)

jaisting is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for the full license text.