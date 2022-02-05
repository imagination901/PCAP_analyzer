# MVP network analyzer for PCAP and CAP files.

## Main idea

This tool was meant as a proof of concept to perform basic network traffic analysis using PCAP files as a source. 

The output would be:

- top 10 Source and Destinaiton packer emitters summarized in two tables;  

- a structural representation traceroute of the top 1 source.

## ## Example of the output:

```
Please enter the PCAP file path: /Users/bogdanyavorskyy/Desktop/temp/pcap/captures/qi_local_SYNACK_slashdot_redirect.pcap

Source packets: 
Source packets from IP: 185.6.85.2, count: 876
Source packets from IP: 10.0.1.4, count: 343
Source packets from IP: 216.34.181.45, count: 42
Source packets from IP: 173.194.65.97, count: 28
Source packets from IP: 74.125.136.95, count: 24

Destination packets: 
Destination packets from IP: 10.0.1.4, count: 970
Destination packets from IP: 185.6.85.2, count: 268
Destination packets from IP: 216.34.181.45, count: 29
Destination packets from IP: 173.194.65.97, count: 23
Destination packets from IP: 74.125.136.95, count: 23

Structured representation of "185.6.85.2 as the top source of packets: 

Begin emission:
Finished sending 32 packets.
...*.*.*.*...*....*......*.*.*.*..*...*..*.*..*..*...*..*...*...*..*.*..*..*..*...*.*.*.*.*...
Received 94 packets, got 30 answers, remaining 2 packets
   185.6.85.2:tcp80   
1  192.168.0.1     11 
2  5.58.128.1      11 
3  172.21.255.2    11 
4  217.196.160.129 11 
6  80.93.127.226   11 
7  213.249.121.129 11 
9  213.19.193.26   11 
10 185.6.87.225    11 
11 185.6.85.129    11 
12 185.6.85.2      SA 
```

## Usage 

You should run this program as follows:
```
cd dest_directory

pip3 install scapy

sudo python3 main.py

Enter the path to the PCAP file after the prompt:

Please enter the PCAP file path: /File/path/file_to_analyze.pcap
```

## License

All of the PCAP files used are open sourced
