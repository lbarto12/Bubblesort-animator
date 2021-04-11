from tkinter import Tk, Canvas
import random as rand

class Sort(Tk):
    def __init__(self):
        super().__init__()
        self.data_size = 1000
        self.__datapoints = []

        self.canvas = Canvas(self, height=500, width=800)
        self.init()

    def init(self):
        for _ in range(self.data_size):
            self.__datapoints.append(rand.randint(0, self.data_size))

        self.title('Bubblesort Animator')
        self.geometry('800x500')
        self.canvas.pack()
        self.update()
        pass

    def run(self):
        self.sort()
        print('done')
        self.mainloop()
        pass

    def sort(self):
        n = len(self.__datapoints)
        for i in range(n):
            self.draw()
            for j in range(0, n - i - 1):
                if self.__datapoints[j] > self.__datapoints[j + 1]:
                    self.swap(j)
                    self.update()
                    pass
                pass
            pass
        pass

    def swap(self, j):
        self.__datapoints[j], self.__datapoints[j + 1] = \
            self.__datapoints[j + 1], self.__datapoints[j]
        pass

    def draw(self):
        self.canvas.delete('all')
        for i in range(self.data_size):
            self.canvas.create_rectangle(
                i * (self.winfo_width() / self.data_size),
                self.winfo_height(),
                (i + 1) * (self.winfo_width() / self.data_size),
                self.winfo_height() - (self.__datapoints[i] / self.data_size) * self.winfo_height()
            )
            pass
        self.canvas.update()
        pass


    @staticmethod
    def main():
        animate = Sort()
        animate.run()
        pass

    pass





if __name__ == '__main__':
    Sort.main()


