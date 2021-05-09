import random
from itertools import count


class Monte_Carlo():
    stop_it = 100000000

    def calc(self, points=10000, seed=0):
        try:
            points = int(points)
        except:
            error = "error converting value of points_am to int type"
            raise ValueError(error)
            return

        random.seed(seed)
        in_circle = 0
        i = points if points <= Monte_Carlo.stop_it else Monte_Carlo.stop_it
        while i >= 0:
            x = random.random()
            y = random.random()
            if x ** 2 + y ** 2 <= 1:
                in_circle += 1
            i -= 1
        pi = 4 * in_circle / points
        print("pi = {:.8f}. Total points = {} points within = {}".format(pi, points, in_circle))

    def calc_compare(self, start=10000, nul=10, stop=5):
        try:
            start = int(start)
            nul = int(nul)
            stop = int(stop)
        except:
            error = "error converting value of points_am to int type"
            raise ValueError(error)
            return

        counts = count(1)
        for iter in counts:
            if iter > stop:
                break
            print("iter: {}".format(iter))
            self.calc(start * nul ** iter)
Monte_Carlo().calc()
Monte_Carlo().calc_compare()
Monte_Carlo().calc_with_np()
Monte_Carlo().calc_compare_with_np(start=100,stop=6)