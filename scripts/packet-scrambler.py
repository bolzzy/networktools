#!/usr/bin/python3
#example script on randomizing packet time and order in one pcap.

from scapy.all import *
#import scapy
import argparse
import random

def main():
    parser = argparse.ArgumentParser(description='Script to randomize packet time and order in one pcap')
    parser.add_argument("-i", "--input", required=True)
    parser.add_argument("-o", "--output", required=True)
    args=parser.parse_args()

    cache=[]

    pkts=rdpcap(args.input)

    for pkt in pkts:
        pkt.time=(random.randint(1,1500000))
        cache.append(pkt)

    random.shuffle(cache)
    wrpcap(args.output, cache)

if __name__ == '__main__':
    main()
