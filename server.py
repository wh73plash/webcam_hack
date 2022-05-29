import cv2
import socket
import numpy

def ByteConvertor(client):
    size = int(client.recv(64).decode())
    context = client.recv(size)
    ret = numpy.frombuffer(data, dtype='uint8') #array to image
    frame = cv2.imdecode(ret, cv2.IMREAD_COLOR)
    return frame


def main(*args):
    ip = "127.0.0.1"
    port = 8888
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(50)
    
    client, addr = server.accept()
    
    while cv2.waitKey(2) != ord(' '):
        frame = ByteConvertor(client)
        cv2.imshow('server', frame)
        
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()