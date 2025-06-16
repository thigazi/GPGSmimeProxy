from multiprocessing import Process
from ProxyEngine import PEngine
from QueueFilter import QFilter


class Sample(object):
    def __init__(self):
        print("Hallo")


if __name__ == '__main__':
    AppObjects = {0: Sample, 1: Sample, }
    processes = []

    for i in range(len(AppObjects)):
        if AppObjects[i] != None:
            pro = Process(target=AppObjects[i])
            processes.append(pro)
            pro.start()

    for prox in processes:
        prox.join()
