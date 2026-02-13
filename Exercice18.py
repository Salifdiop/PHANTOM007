"""
Mini-projet de transition vers la programmation réseau 
"""
from datetime import datetime

def verifier_ipv4(ip):
    parties = ip.split(".")
    if len(parties) != 4:
        return False
    for p in parties:
        if not p.isdigit() or not 0 <= int(p) <= 255:
            return False
    return True


def verifier_port(port):
    try:
        port = int(port)
        return 1 <= port <= 65535
    except ValueError:
        return False


ip = input("Entrez une adresse IP : ")

if not verifier_ipv4(ip):
    print(" Adresse IP invalide")
    exit()

ports_simules = [22, 80, 443, 3306]
ports_ouverts = [22, 80]

with open("scan_log.txt", "a") as log:
    log.write(f"\nScan du {datetime.now()} - IP {ip}\n")

print("\nRésultats du scan :")

for port in ports_simules:
    if port in ports_ouverts:
        print(f"Port {port} : OUVERT")
        with open("scan_log.txt", "a") as log:
            log.write(f"Port {port} : OUVERT\n")

print("\nScan terminé. Résultats enregistrés.")

