from matrix import Matrix
from Client import Client

if __name__ == "__main__":
    max_creation = Matrix(10, 500)
    fm, sm = max_creation.create_matrix()
    print(f'N: {fm.shape[0]}, M: {fm.shape[1]}, L: {sm.shape[1]}')

    client = Client(('127.0.0.1', 6116))
    client.PushToServer(fm, sm)

    result = client.ReceiveFromServer()['Result']
    print(f'Результат отриманий від клієнта: {result.shape}')






