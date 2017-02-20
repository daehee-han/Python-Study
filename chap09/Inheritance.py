class Logger:
    def WriteOnFile(self):
        print('WriteOnFile() call')

class NetworkLogger(Logger):
    def WriteOnNetwork(self):
        print('WriteOnNetwork() call')

if __name__ == '__main__':
    network = NetworkLogger()
    network.WriteOnFile()
    network.WriteOnNetwork()