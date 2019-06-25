import sys
from kamene.all import rdpcap

if len(sys.argv) < 3:
    print("Improper arguments: make_config.py pfile time_val")
    sys.exit(-1)

pfile = sys.argv[1]
time_val = sys.argv[2]

print(pfile)
packet = rdpcap(pfile)
p = packet[0]

# victim data
print(p.payload.dst)
print(p.dst)
print(p.payload.payload.dport)

# attacker data
print(p.payload.src)
print(p.src)
print(p.payload.payload.sport)

# new victim data
vic_dic = {'ftp': '192.168.3.51\n00:50:56:9a:13:47', 'ssh': '192.168.3.52\n00:50:56:9a:35:5c',
            '3way': '192.168.3.52\n00:50:56:9a:35:5c', 'telnet': '192.168.3.53\n00:50:56:9a:42:52',
            'finger': '192.168.3.54\n00:50:56:9a:03:ad', 'buffov': '192.168.3.54\n00:50:56:9a:03:ad',
            'www': '192.168.3.55\n00:50:56:9a:47:de'}
for k in vic_dic:
    if k in pfile:
        print(vic_dic[k])
print(p.payload.dport)

# my data
print("192.168.2.119")
print("00:24:e8:fc:88:0f")
print(p.payload.payload.sport)

# other data
print("enp0s25")
print(time_val)
