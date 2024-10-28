# Network Sniffer

Un réseau sniffer simple développé en Python qui capture et analyse le trafic réseau. Ce projet utilise la bibliothèque `Scapy` pour la capture de paquets et `Pandas` pour l'analyse des données.

## Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Technologies Utilisées](#technologies-utilisées)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [Tests](#tests)
- [Contributions](#contributions)
- [License](#license)

## Fonctionnalités

- Capture des paquets sur une interface réseau spécifiée.
- Analyse des paquets capturés pour extraire des informations utiles (adresse IP source et destination, ports, protocole, taille du paquet).
- Affichage de graphiques statistiques sur le trafic réseau capturé.

## Technologies Utilisées

- [Python](https://www.python.org/) - Langage de programmation
- [Scapy](https://scapy.readthedocs.io/en/latest/) - Bibliothèque de manipulation de paquets
- [Pandas](https://pandas.pydata.org/) - Bibliothèque pour l'analyse de données
- [Matplotlib](https://matplotlib.org/) - Bibliothèque pour la création de graphiques
- [PyYAML](https://pyyaml.org/) - Bibliothèque pour la gestion des fichiers YAML

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/yourusername/network_sniffer.git
   cd network_sniffer
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Avant de lancer le programme, vous devez configurer l'interface réseau et le nombre de paquets à capturer dans le fichier `config/config.yaml`. Voici un exemple de configuration :

```yaml
interface: "MediaTek MT7921 Wi-Fi 6 802.11ax PCIe Adapter"
packet_count: 1000
```

Assurez-vous que l'interface réseau que vous avez spécifiée est correcte et qu'elle est disponible sur votre machine.

## Utilisation

Pour lancer le sniffer, exécutez le script principal :

```bash
bash run_sniffer.sh
```

Assurez-vous d'avoir les permissions nécessaires pour exécuter le script en tant que super utilisateur (sudo).

## Tests

Le projet inclut des tests unitaires pour vérifier le bon fonctionnement des fonctions principales. Pour exécuter les tests, utilisez la commande suivante :

```bash
python -m unittest discover -s tests
```

## Contributions

Les contributions sont les bienvenues ! Veuillez ouvrir une issue ou soumettre une demande de tirage pour discuter des changements que vous souhaitez apporter.

## License

Ce projet est sous la [MIT License](LICENSE).
