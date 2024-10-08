D’accord, voici une version mise à jour du résumé, tout en conservant les termes spécifiques en anglais :

Le réseau simplifié consiste à la communication entre deux endpoints sur Internet, où chaque machine possède une adresse IP unique. Ces machines, également appelées hosts, peuvent avoir des adresses temporaires.

Client et serveur :
Ton appareil (ordinateur, téléphone) agit en tant que client, tandis que la machine distante avec laquelle tu échanges des données est le serveur. Le client initie toujours la communication, car le serveur ne peut pas contacter directement le client.

Quelle machine :
Lorsque le client veut interagir avec un serveur, il ne connaît généralement pas son adresse IP mais son nom (hostname), comme “example.com”, contenu dans une URL.

Hostname resolving :
Le client utilise un DNS pour convertir le hostname en une adresse IP. Ce processus est appelé “name resolving”. Le DNS renvoie une ou plusieurs adresses IP correspondant au hostname demandé.

Establish a connection :
Avec les adresses IP obtenues, le client essaie d’établir une connexion TCP ou QUIC avec le serveur. Si une adresse échoue, il tente la suivante jusqu’à ce qu’une connexion soit réussie ou que toutes échouent.

Connect to port numbers :
Chaque protocole utilise un port spécifique. Par exemple, HTTP utilise par défaut le port 80 et HTTPS le port 443. Un port personnalisé peut également être inclus dans l’URL.

Security :
Une fois la connexion TCP établie, si une sécurité supplémentaire est nécessaire (comme avec HTTPS), un “TLS handshake” est effectué pour sécuriser la connexion.

Transfer data :
Après l’établissement de la connexion, les données peuvent être échangées entre le client et le serveur via un protocole. Un download (téléchargement) fait référence au transfert de données du serveur vers le client, tandis qu’un upload (envoi) correspond au transfert du client vers le serveur.

Disconnect :
Après le transfert des données, la connexion peut être réutilisée pour d’autres transferts ou être fermée.