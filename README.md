# shodan_subdomain
This simple script fetches hackerone.com _(for example)_ subdomains from `https://www.shodan.io/domain/hackerone.com`

## Installation:

`git clone https://github.com/seqrity/shodan_subdomain.git`

`apt install python3-pip`

`pip3 install -r requirements.txt`

## Usage:

`python3 shodan.py hackerone.com`

## Warning:
There are limitation on shodan base on IP. If you don't receive subdomains might Shodan blocks your IP and should change your IP.
