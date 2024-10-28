import pandas as pd
from scapy.layers.inet import IP, TCP, UDP
from datetime import datetime

# Liste pour stocker les données
packet_data = []

def analyze_packet(packet):
    if IP in packet:
        packet_info = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Horodatage de capture
            "source_ip": packet[IP].src,
            "destination_ip": packet[IP].dst,
            "protocol": None,
            "source_port": None,
            "destination_port": None,
            "packet_size": len(packet),  # Taille du paquet en octets
            "tos": packet[IP].tos if IP in packet else None  # Type de service pour IP
        }
        if TCP in packet:
            packet_info["protocol"] = "TCP"
            packet_info["source_port"] = packet[TCP].sport
            packet_info["destination_port"] = packet[TCP].dport
            packet_info["tcp_flags"] = packet[TCP].flags  # Drapeaux TCP
        elif UDP in packet:
            packet_info["protocol"] = "UDP"
            packet_info["source_port"] = packet[UDP].sport
            packet_info["destination_port"] = packet[UDP].dport
            packet_info["udp_length"] = packet[UDP].len  # Longueur du paquet UDP

        # Ajouter les infos dans la liste
        packet_data.append(packet_info)

# Convertir en DataFrame après la capture de paquets
def get_packet_dataframe():
    return pd.DataFrame(packet_data)
