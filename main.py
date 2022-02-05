from scapy.all import *
import pktcounter 

def main():

    address = input("Please enter the PCAP file path: ")
    file = rdpcap(address)

    counter = pktcounter.PacketCounter()

    for pkt in file:
        counter.add_packet(ip=pkt[IP].src, type="source")
        counter.add_packet(ip=pkt[IP].dst, type="destination")

    counter.print_packets(type="source")
    counter.print_packets(type="destination")

    counter.trace_top_source()


if __name__ == "__main__":
    main()
