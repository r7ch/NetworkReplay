# NetworkReplay

## Purpose
Process a tcpdump formatted binary file and modify it in order to replay the attack on a chosen victim.

## Dependencies 
- kamene

## make_config.py
Using the given pcap file and known information about the victims, generate a config file to be used by atkGen with a given timing. These timings will be used by atkGen to determine how rapidly to send out packets in the replay.<br>
<br> *Usage:*<br>```make_config.py pcapFile timing```


## atkGen
Based on a given config file, read in a pcap file and modify the packets for replay. This includes modifying source and destination ips, macs, and ports as well as checksums. Then either print these packets out or sends out the attacking packets (when used with the -s flag) from the given host in the config file to the given victim. The timing dictates the rate at which these packets are sent out.<br>
<br>*Usage:*<br>```atkGen [-s] configFile```