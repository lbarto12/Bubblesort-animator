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
        for i in range(self.data_size):
            self.__datapoints.append(i)

        rand.shuffle(self.__datapoints)

        self.title('Bubblesort Animator')
        self.geometry('800x500')
        self.canvas.pack()

    def run(self):
        self.sort()
        print('done')
        self.mainloop()

    def sort(self):
        n = len(self.__datapoints)
        for i in range(n):
            self.draw()
            for j in range(0, n - i - 1):
                if self.__datapoints[j] > self.__datapoints[j + 1]:
                    self.swap(j)
                    self.update()

    def swap(self, j):
        self.__datapoints[j], self.__datapoints[j + 1] = \
            self.__datapoints[j + 1], self.__datapoints[j]

    def draw(self):
        self.canvas.delete('all')
        for i in range(self.data_size):
            rect = self.canvas.create_rectangle(
                i * (self.winfo_width() / self.data_size),
                self.winfo_height(),
                (i + 1) * (self.winfo_width() / self.data_size),
                self.winfo_height() - (self.__datapoints[i] / self.data_size) * self.winfo_height()
            )
        self.canvas.update()


    @staticmethod
    def main():
        Sort().run()


if __name__ == '__main__':
    Sort.main()


