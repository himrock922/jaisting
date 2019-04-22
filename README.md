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
% ./node_modules/webpack/bin/webpack.js --config webpack.config.js --mode=development
% sudo python3.7 manage.py runserver 0.0.0.0:8080
```

jaisting is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for the full license text.