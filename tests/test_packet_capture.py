from src.packet_capture import capture_packets

def test_capture_packets():
    packets = capture_packets("lo", 5)  # Utilise l'interface locale pour les tests
    assert len(packets) == 5
