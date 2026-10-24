import socket
import time

class MoxaClient:
    def __init__(self, host: str = "127.0.0.1", port: int = 4002, timeout: float = 2.0):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = None

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(self.timeout)
        self.sock.connect((self.host, self.port))
        print(f"[+] Połączono z emulatorem MOXA pod {self.host}:{self.port}")

    def send(self, data: bytes):
        if self.sock:
            self.sock.sendall(data)
            print(f"[>] Wysłano do Pico: {data}")

    def receive(self, buffer_size: int = 1024) -> bytes:
        if self.sock:
            try:
                data = self.sock.recv(buffer_size)
                print(f"[<] Odebrano z Pico: {data}")
                return data
            except socket.timeout:
                print("[-] Timeout: Pico nie odpowiedziało w wyznaczonym czasie.")
                return b""
        return b""

    def close(self):
        if self.sock:
            self.sock.close()
            print("[+] Połączenie zamknięte.")

# --- Szybki Test Loopback ---
if __name__ == "__main__":
    moxa = MoxaClient(host="127.0.0.1", port=4002)
    moxa.connect()
    
    # Wyślij komendę testową do Pico
    moxa.send(b"PING_FROM_PYTHON\n")
    
    # Czekamy chwilę na odpowiedź UART
    time.sleep(0.2)
    response = moxa.receive()
    
    moxa.close()