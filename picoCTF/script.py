import json
from collections import defaultdict
from statistics import mean
data = """
{
    "tickets": [
        {
            "ticket_id": 0,
            "timestamp": "2017/06/10 07:50:14",
            "file_hash": "fb0abe9b2a37e234",
            "src_ip": "131.90.8.180",
            "dst_ip": "104.97.128.21"
        },
        {
            "ticket_id": 1,
            "timestamp": "2017/06/11 05:19:56",
            "file_hash": "f2d8740404ff1d55",
            "src_ip": "187.100.149.54",
            "dst_ip": "33.29.174.118"
        },
        {
            "ticket_id": 2,
            "timestamp": "2016/01/17 13:17:29",
            "file_hash": "f2d8740404ff1d55",
            "src_ip": "210.205.230.140",
            "dst_ip": "50.225.199.154"
        },
        {
            "ticket_id": 3,
            "timestamp": "2017/08/14 18:02:17",
            "file_hash": "1a03d0a86d991e91",
            "src_ip": "122.231.138.129",
            "dst_ip": "88.148.199.124"
        },
        {
            "ticket_id": 4,
            "timestamp": "2017/11/01 00:42:15",
            "file_hash": "c99d65ede54ac8d9",
            "src_ip": "93.124.108.240",
            "dst_ip": "108.69.9.32"
        },
        {
            "ticket_id": 5,
            "timestamp": "2015/08/17 20:48:14",
            "file_hash": "43e10d21eb3f5dc8",
            "src_ip": "210.205.230.140",
            "dst_ip": "50.225.199.154"
        },
        {
            "ticket_id": 6,
            "timestamp": "2017/04/15 12:01:55",
            "file_hash": "5b8825f908e1738b",
            "src_ip": "122.231.138.129",
            "dst_ip": "209.104.88.119"
        },
        {
            "ticket_id": 7,
            "timestamp": "2015/03/18 22:37:20",
            "file_hash": "43e10d21eb3f5dc8",
            "src_ip": "122.231.138.129",
            "dst_ip": "209.104.88.119"
        },
        {
            "ticket_id": 8,
            "timestamp": "2015/07/08 17:11:17",
            "file_hash": "fb0abe9b2a37e234",
            "src_ip": "93.124.108.240",
            "dst_ip": "33.29.174.118"
        },
        {
            "ticket_id": 9,
            "timestamp": "2015/12/10 17:28:48",
            "file_hash": "cafc9c5ec7ebc133",
            "src_ip": "210.205.230.140",
            "dst_ip": "99.31.12.3"
        }
    ]
}
"""

json = json.loads(data)

f = defaultdict(set)
for t in json['tickets']:
	f[t['file_hash']].add(t['dst_ip'])

print(mean(len(v) for k,v in f.items()))


