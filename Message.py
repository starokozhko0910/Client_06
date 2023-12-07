import struct
import pickle
class Message:
    def __init__(self, socket):
        self.socket = socket
    def LoadMessage(self):
        result_data_length = int.from_bytes(self.socket.recv(5), byteorder='big')
        result_data = self.socket.recv(result_data_length)
        result = pickle.loads(result_data)
        self.socket.close()
        return result
    def PushMessage(self, fm, sm):
        data = {
            'first_matrix': fm,
            'second_matrix': sm,
        }
        serialized_data = pickle.dumps(data)
        self.socket.sendall(len(serialized_data).to_bytes(4, byteorder='big'))
        self.socket.sendall(serialized_data)