import socket
from datetime import datetime

def scan_ports(target, start_port=1, end_port=1024):
    print(f"Scanning ports on {target} from {start_port} to {end_port}...")
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Half-second timeout

        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
            open_ports.append(port)
        sock.close()

    return open_ports

def main():
    target = input("Enter target IP or hostname: ")
    start_time = datetime.now()

    try:
        open_ports = scan_ports(target)
    except KeyboardInterrupt:
        print("\nScan interrupted by user")
        return
    except socket.gaierror:
        print("Hostname could not be resolved.")
        return
    except socket.error:
        print("Could not connect to server.")
        return

    end_time = datetime.now()
    print(f"\nScan completed in: {end_time - start_time}")
    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
