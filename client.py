import cv2
import socket
import numpy

def FrameToBytesAndSend(client, frame):
    ret, bin = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY),64])
    array = np.array(bin)
    client.send(str(len(array)).ljust(64).encode())
    client.send(array)

def main(*args):
    IP = "127.0.0.1"
    PORT = 8080

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT))

    capture = cv2.VideoCapture(0)

    while True:
        ret, frame = capture.read()
        FrameToBytesAndSend(client, frame)

    capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()