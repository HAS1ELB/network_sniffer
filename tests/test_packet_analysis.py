import unittest
import pandas as pd
from scapy.layers.inet import IP, TCP, UDP
from scapy.packet import Packet
from src.packet_analysis import analyze_packet, get_packet_dataframe, packet_data

class TestPacketAnalysis(unittest.TestCase):

    def setUp(self):
        # Effacer les données capturées avant chaque test
        packet_data.clear()

    def test_analyze_tcp_packet(self):
        # Création d'un paquet TCP simulé
        packet = IP(src="192.168.1.1", dst="192.168.1.2") / TCP(sport=1234, dport=80, flags="S")
        analyze_packet(packet)
        
        # Vérifier que les informations du paquet sont extraites correctement
        self.assertEqual(len(packet_data), 1)
        self.assertEqual(packet_data[0]["source_ip"], "192.168.1.1")
        self.assertEqual(packet_data[0]["destination_ip"], "192.168.1.2")
        self.assertEqual(packet_data[0]["protocol"], "TCP")
        self.assertEqual(packet_data[0]["source_port"], 1234)
        self.assertEqual(packet_data[0]["destination_port"], 80)
        self.assertIn("tcp_flags", packet_data[0])

    def test_analyze_udp_packet(self):
        # Création d'un paquet UDP simulé
        packet = IP(src="192.168.1.3", dst="192.168.1.4", tos=4) / UDP(sport=4321, dport=53)
        analyze_packet(packet)
        
        # Vérifier que les informations du paquet sont extraites correctement
        self.assertEqual(len(packet_data), 1)
        self.assertEqual(packet_data[0]["source_ip"], "192.168.1.3")
        self.assertEqual(packet_data[0]["destination_ip"], "192.168.1.4")
        self.assertEqual(packet_data[0]["protocol"], "UDP")
        self.assertEqual(packet_data[0]["source_port"], 4321)
        self.assertEqual(packet_data[0]["destination_port"], 53)
        self.assertEqual(packet_data[0]["tos"], 4)
        self.assertIn("udp_length", packet_data[0])

    def test_analyze_packet_dataframe(self):
        # Création de deux paquets simulés
        packet1 = IP(src="192.168.1.1", dst="192.168.1.2") / TCP(sport=1234, dport=80)
        packet2 = IP(src="192.168.1.3", dst="192.168.1.4") / UDP(sport=4321, dport=53)
        
        analyze_packet(packet1)
        analyze_packet(packet2)
        
        # Convertir les données en DataFrame
        df = get_packet_dataframe()
        
        # Vérifier le format du DataFrame
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape[0], 2)  # Devrait contenir deux lignes
        self.assertIn("source_ip", df.columns)
        self.assertIn("destination_ip", df.columns)
        self.assertIn("protocol", df.columns)
        self.assertIn("packet_size", df.columns)

    def test_packet_size(self):
        # Création d'un paquet avec une certaine taille
        packet = IP(src="192.168.1.5", dst="192.168.1.6") / TCP(sport=1234, dport=80)
        analyze_packet(packet)

        # Vérifier que la taille du paquet est correcte
        self.assertEqual(packet_data[0]["packet_size"], len(packet))

if __name__ == '__main__':
    unittest.main()
