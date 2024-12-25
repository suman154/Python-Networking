import socket

def start_client():
    host = '127.0.0.1'  # Server address
    port = 5001  # Server port

    # Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))  # Connect to the server

    print("Connected to server. Type 'q' to quit.")
    message = input("Type message: ")

    while message.lower() != 'q':
        # Send data to the server
        client_socket.send(message.encode())

        # Receive response from the server
        data = client_socket.recv(1024).decode()
        print(f"Received from server: {data}")

        # Prompt for the next message
        message = input("Type message: ")

    client_socket.close()  # Close the connection
    print("Disconnected from server")

if __name__ == "__main__":
    start_client()
