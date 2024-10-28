from scapy.all import sniff

def capture_packets(interface, packet_count):
    return sniff(iface=interface, count=packet_count)
