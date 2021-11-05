import socket, socks
import requests

archivo = open("/home/francisco/Descargas/nombresURL.txt", "r")
lista = archivo.readlines()
archivo.close()




def separaLista(lista):
    paresLista = []
    imparesLista = []
    for i in range(len(lista)):
        if i % 2 == 0:
            paresLista.append(lista[i])
        else:
            imparesLista.append(lista[i])
    return paresLista, imparesLista

listaURL = separaLista(lista)[1]
gente = separaLista(lista)[0]


k = 0

for url in listaURL:

    try:
        url = url.strip("\n")
        
        # Create a TCP/IP socket
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
        #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock = socks.socksocket()

        # Bind the socket to the port
        
        server_address = (url, 8000)
        sock.connect(server_address)


        a = sock.recv(4096).decode()
        if "ftp" in a.lower():
            print("owner {} tiene el servicio ftp".format(gente[k].strip("\n")))
            k = k+1
            sock.close()
        elif "ssh" in a.lower():
            print("owner {} tiene el servicio ssh".format(gente[k].strip("\n")))
            k = k+1
            sock.close()
        else:
            sock.close()
            print("owner {} tiene otro servicio".format(gente[k].strip("\n")))
            k = k+1
            #
            try:
                sock = socks.socksocket()
                server_address = (url, 443)
                sock.connect(server_address)
                print("Puerto 443 abierto!")
                print("Servidor de tipo: {}".format(requests.get("https://{}".format(url)).headers["server"]))
            except:
                
                pass
            try:
                sock = socks.socksocket()
                server_address = (url, 80)
                sock.connect(server_address)
                print("Puerto 80 abierto!")
                print("Servidor de tipo: {}".format(requests.get("http://{}".format(url)).headers["server"]))
            except:
                
                pass
    except:
        print("owner {} no tiene el host accesible".format(gente[k].strip("\n")))
        k = k+1
        pass

