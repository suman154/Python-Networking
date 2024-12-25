import socket

def start_server():
    host = '127.0.0.1'  # Localhost
    port = 5001  # Port to listen on

    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Allow only one connection
    print(f"Server started and listening on {host}:{port}")

    # Wait for a client to connect
    conn, addr = server_socket.accept()
    print(f"Connection from: {addr}")

    while True:
        # Receive data from the client
        data = conn.recv(1024).decode()
        if not data:
            break  # Exit the loop if no data is received
        print(f"Received from client: {data}")

        # Process the received data (e.g., echo in uppercase)
        response = f"Server response: {data.upper()}"
        conn.send(response.encode())  # Send the response back to the client

    conn.close()  # Close the connection
    print("Server closed connection")

if __name__ == "__main__":
    start_server()
