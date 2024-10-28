from packet_capture import capture_packets
from packet_analysis import analyze_packet, get_packet_dataframe
import yaml
import matplotlib.pyplot as plt
import pandas as pd

def main():
    # Charger la configuration
    with open("config/config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)
        
    # Capturer les paquets
    packets = capture_packets(config["interface"], config["packet_count"])
    
    # Analyser les paquets
    for packet in packets:
        analyze_packet(packet)
        
    df = get_packet_dataframe()
    
    show_statistics(df)
        
def show_statistics(df):
    # Graphique du nombre de paquets par protocole
    protocol_counts = df["protocol"].value_counts()
    protocol_counts.plot(kind="bar", color="skyblue")
    plt.title("Nombre de paquets par protocole")
    plt.xlabel("Protocole")
    plt.ylabel("Nombre de paquets")
    plt.show()

    # Graphique des ports les plus utilisés (destination)
    top_ports = df["destination_port"].value_counts().head(10)
    top_ports.plot(kind="bar", color="orange")
    plt.title("Top 10 des ports de destination")
    plt.xlabel("Port")
    plt.ylabel("Nombre de paquets")
    plt.show()


    # Graphique de la taille moyenne des paquets par protocole
    packet_size_by_protocol = df.groupby("protocol")["packet_size"].mean()
    packet_size_by_protocol.plot(kind="bar", color="purple")
    plt.title("Taille moyenne des paquets par protocole")
    plt.xlabel("Protocole")
    plt.ylabel("Taille moyenne des paquets (octets)")
    plt.show()

    # Graphique de la distribution des drapeaux TCP
    if "tcp_flags" in df.columns:
        tcp_flags_counts = df["tcp_flags"].value_counts().head(5)  # Top 5 des drapeaux TCP les plus fréquents
        tcp_flags_counts.plot(kind="bar", color="red")
        plt.title("Distribution des drapeaux TCP")
        plt.xlabel("Drapeaux TCP")
        plt.ylabel("Nombre de paquets")
        plt.show()

    # Réinitialiser l'index pour éviter tout impact dans d'autres traitements
    df.reset_index(drop=True, inplace=True)

if __name__ == "__main__":
    main()
