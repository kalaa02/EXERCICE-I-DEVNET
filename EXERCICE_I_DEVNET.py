# Ouvrir le fichier en mode lecture
with open('C:\\Users\Francel\\Desktop\\TP\\EXERCICE-I-DEVNET\\show_ip_bgp_summ.txt', 'r') as f:

    # Lire le contenu du fichier
    lines = f.readlines()

    # Extraire la première ligne et afficher le numéro AS local
    first_line = lines[0].strip()
    as_number = first_line.split()[-1]
    print("Numéro AS local :", as_number)

    # Extraire la dernière ligne et afficher l'adresse IP du pair BGP
    last_line = lines[-1].strip()
    bgp_peer_ip = last_line.split()[0]
    print("Adresse IP du pair BGP :", bgp_peer_ip)