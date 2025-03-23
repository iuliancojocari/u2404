import subprocess

def configure_resolv_conf():
    """
    Problème sur Ubuntu 24.04 LTS
    La configuration réseau pour les serveur dns ne sont
    pas appliquées dans le fichier resolv.conf
    Par conséquent, le serveur n'arrive pas à résoudre le dns
    """
    try:
        print("************* start configure_resolv_conf *************\n")
        subprocess.run("sudo rm -f /etc/resolv.conf", shell=True, check=True)
        print("Le fichier resolv.conf a été supprimé.")

        subprocess.run("sudo ln -s /run/systemd/resolve/resolv.conf /etc/resolv.conf", shell=True, check=True)
        print("Un lien symbolique a été créé pour le fichier resolv.conf")
        print("/run/systemd/resolve/resolv.conf /etc/resolv.conf")

        subprocess.run("sudo netplan apply", shell=True, check=True)
        print("La configuration réseau a été appliquée en utilisant netplan")

        result = subprocess.run("sudo cat /etc/resolv.conf \n", shell=True, check=True, text=True, capture_output=True)
        print(f"Contenu du fichier resolv.conf : \n\n {result.stdout}")
        print("\n************* end configure_resolv_conf *************")

    except subprocess.CalledProcessError as e : 
        print(f"Une erreur est survenue : {e}")
        print(f"Message d'erreur : {e.stderr}")

def main():
    configure_resolv_conf()


if __name__ == "__main__":
    main()