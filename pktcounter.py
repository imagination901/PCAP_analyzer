from dataclasses import dataclass
import itertools
from scapy.all import *


@dataclass
class PacketCounter:
    source_packets = {}
    destination_packets = {}

    def add_packet(self, ip: int, type: str):
        if type == "source":
            if ip in self.source_packets:
                self.source_packets[ip] += 1
            else:
                self.source_packets[ip] = 1
        elif type == "destination":
            if ip in self.destination_packets:
                self.destination_packets[ip] += 1
            else:
                self.destination_packets[ip] = 1
    
    def print_packets(self, type: str, slice: int=10):
        if type == "source":
            print("\nSource packets: ")
            sorted_packets = {k: v for k, v in sorted(self.source_packets.items(), key=lambda item: item[1], reverse=True)} 
            sliced_packets = dict(itertools.islice(sorted_packets.items(), slice))
            for packet in sliced_packets:
                print(f"Source packets from IP: {packet}, count: {self.source_packets[packet]}")
        elif type == "destination":
            print("\nDestination packets: ")
            sorted_packets ={k: v for k, v in sorted(self.destination_packets.items(), key=lambda item: item[1], reverse=True)} 
            sliced_packets = dict(itertools.islice(sorted_packets.items(), slice))
            for packet in sliced_packets:
                print(f"Destination packets from IP: {packet}, count: {self.destination_packets[packet]}") 
        else:
            print(f"Unknown type of packets specified: '{type}'. Please check for a typo.")

    @property
    def _top_source_ip(self):
        sorted_packets = {k: v for k, v in sorted(self.source_packets.items(), key=lambda item: item[1], reverse=True)} 
        top_source = list(sorted_packets)[0]
        return top_source

    def trace_top_source(self):
        print(f'\nStructured representation of the top IP {self._top_source_ip}: \n')
        result, unans = traceroute(self._top_source_ip, maxttl=32)
