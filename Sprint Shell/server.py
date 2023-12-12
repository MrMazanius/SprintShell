import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)

    print("Listening for incoming connections...")

    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    while True:
        command = input("Enter a command (or 'exit' to close): ")
        if command.lower() == 'exit':
            break

        client_socket.send(command.encode())

        # Receive the command output from the client
        output = client_socket.recv(4096).decode()
        print(f"Command output:\n{output}")

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
