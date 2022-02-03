import random
import time
import matplotlib.pyplot as plt
import numpy as np
import sys

class SendBox():
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.atom_lst = []
        self.space = [[None for _ in range(w)]for __ in range(h)]

        self.epc = 0





    def add(self, atom):
        self.atom_lst.append(atom)
        if not self.space[atom.x][atom.y]:
            self.space[atom.x][atom.y] = [atom.idx, ]
        else:
            self.space[atom.x][atom.y].append(atom.idx)



    def update(self):
        for atom_idx in range(len(self.atom_lst)):

            if not self.atom_lst[atom_idx].can_move:
                continue

            curr_x = self.atom_lst[atom_idx].x
            curr_y = self.atom_lst[atom_idx].y

            a = [0, 0]

            if curr_y - 1 >= 0 and curr_y < self.h-1 and curr_x - 1 >= 0 and curr_x < self.w-1:
                print('curr_x_y', curr_x, curr_y)


                f_x = 0
                f_x += len(self.space[self.atom_lst[atom_idx].x - 1][self.atom_lst[atom_idx].y - 1]) if self.space[self.atom_lst[atom_idx].x - 1][self.atom_lst[atom_idx].y - 1] else 0
                f_x += len(self.space[self.atom_lst[atom_idx].x - 1][self.atom_lst[atom_idx].y    ]) if self.space[self.atom_lst[atom_idx].x - 1][self.atom_lst[atom_idx].y    ] else 0
                f_x += len(self.space[self.atom_lst[atom_idx].x - 1][self.atom_lst[atom_idx].y + 1]) if self.space[self.atom_lst[atom_idx].x - 1][self.atom_lst[atom_idx].y + 1] else 0

                f_x -= len(self.space[self.atom_lst[atom_idx].x + 1][self.atom_lst[atom_idx].y - 1]) if self.space[self.atom_lst[atom_idx].x + 1][self.atom_lst[atom_idx].y - 1] else 0
                f_x -= len(self.space[self.atom_lst[atom_idx].x + 1][self.atom_lst[atom_idx].y    ]) if self.space[self.atom_lst[atom_idx].x + 1][self.atom_lst[atom_idx].y    ] else 0
                f_x -= len(self.space[self.atom_lst[atom_idx].x + 1][self.atom_lst[atom_idx].y + 1]) if self.space[self.atom_lst[atom_idx].x + 1][self.atom_lst[atom_idx].y + 1] else 0

                f_y = 0
                f_y += len(self.space[self.atom_lst[atom_idx].x - 1][self.atom_lst[atom_idx].y - 1]) if self.space[self.atom_lst[atom_idx].x - 1][self.atom_lst[atom_idx].y - 1] else 0
                f_y += len(self.space[self.atom_lst[atom_idx].x    ][self.atom_lst[atom_idx].y - 1]) if self.space[self.atom_lst[atom_idx].x   ][self.atom_lst[atom_idx].y - 1] else 0
                f_y += len(self.space[self.atom_lst[atom_idx].x + 1][self.atom_lst[atom_idx].y - 1]) if self.space[self.atom_lst[atom_idx].x + 1][self.atom_lst[atom_idx].y - 1] else 0

                f_y -= len(self.space[self.atom_lst[atom_idx].x - 1][self.atom_lst[atom_idx].y + 1]) if self.space[self.atom_lst[atom_idx].x - 1][self.atom_lst[atom_idx].y + 1] else 0
                f_y -= len(self.space[self.atom_lst[atom_idx].x    ][self.atom_lst[atom_idx].y + 1]) if self.space[self.atom_lst[atom_idx].x    ][self.atom_lst[atom_idx].y + 1] else 0
                f_y -= len(self.space[self.atom_lst[atom_idx].x + 1][self.atom_lst[atom_idx].y + 1]) if self.space[self.atom_lst[atom_idx].x + 1][self.atom_lst[atom_idx].y + 1] else 0

                a = [f_x, f_y]

                print('a {}'.format(a))


            if self.atom_lst[atom_idx].v[0]!=0 or self.atom_lst[atom_idx].v[1]!=0:
                self.space[self.atom_lst[atom_idx].x][self.atom_lst[atom_idx].y].pop(self.space[self.atom_lst[atom_idx].x][self.atom_lst[atom_idx].y].index(atom_idx))

                fore_idx = (self.atom_lst[atom_idx].x, self.atom_lst[atom_idx].y)

                self.atom_lst[atom_idx].x += self.atom_lst[atom_idx].v[0]
                self.atom_lst[atom_idx].y += self.atom_lst[atom_idx].v[1]


                if self.atom_lst[atom_idx].x >= self.w-1:
                    self.atom_lst[atom_idx].x = self.w-1
                    self.atom_lst[atom_idx].can_move = False
                if self.atom_lst[atom_idx].x <= 0:
                    self.atom_lst[atom_idx].x = 0
                    self.atom_lst[atom_idx].can_move = False

                if self.atom_lst[atom_idx].y >= self.h-1:
                    self.atom_lst[atom_idx].y = self.h-1
                    self.atom_lst[atom_idx].can_move = False
                if self.atom_lst[atom_idx].y <= 0:
                    self.atom_lst[atom_idx].y = 0
                    self.atom_lst[atom_idx].can_move = False


                curr_idx = (self.atom_lst[atom_idx].x, self.atom_lst[atom_idx].y)

                print('Node {} Move from {} to {}'.format(atom_idx, fore_idx, curr_idx))

                if not self.space[self.atom_lst[atom_idx].x][self.atom_lst[atom_idx].y]:
                    self.space[self.atom_lst[atom_idx].x][self.atom_lst[atom_idx].y] = [atom_idx, ]
                else:
                    self.space[self.atom_lst[atom_idx].x][self.atom_lst[atom_idx].y].append(atom_idx)

                # self.atom_lst[atom_idx].v = [0, 0]
                self.atom_lst[atom_idx].v[0] += a[0]
                self.atom_lst[atom_idx].v[1] += a[1]

            else:
                self.atom_lst[atom_idx].v = a

    def run(self):

        x_lst = [i for i in range(1, self.w-1)]
        y_lst = [i for i in range(1, self.h-1)]

        # mode 1
        # for i in range(50):
        #     a = Atom(random.choice(x_lst), random.choice(y_lst), i)
        #     self.add(a)


        # mode2
        # a1 = Atom(15, 10, 0, v=[0, 1])
        # a2 = Atom(15, 20, 1, v=[0, -1])
        # self.add(a1)
        # self.add(a2)

        # mode 3
        # a1 = Atom(10, 10, 0, v=[0, 1])
        # a2 = Atom(20, 20, 1, v=[-1, 0])
        # self.add(a1)
        # self.add(a2)

        # mode 4
        # for i in range(50):
        #     a = Atom(random.choice(x_lst), random.choice(y_lst), i, v=[random.choice([0,-1,1]), random.choice([0,-1,1])])
        #     self.add(a)

        # # mode 5
        # a1 = Atom(11, 11, 0)
        # a2 = Atom(10, 12, 1, can_update=False)
        # a3 = Atom(10, 10, 2, can_update=False)
        # a4 = Atom(12, 10, 3, can_update=False)
        # self.add(a1)
        # self.add(a2)
        # self.add(a3)
        # self.add(a4)

        # mode 6
        # a1 = Atom(11, 11, 0)
        # a2 = Atom(10, 12, 1, can_update=False)
        # a3 = Atom(10, 10, 2, can_update=False)
        # a4 = Atom(12, 12, 3, can_update=False)
        # self.add(a1)
        # self.add(a2)
        # self.add(a3)
        # self.add(a4)

        # mode 7
        # a1 = Atom(11, 11, 0)
        # a2 = Atom(10, 12, 1)
        # a3 = Atom(10, 10, 2)
        # a4 = Atom(12, 12, 3)
        # self.add(a1)
        # self.add(a2)
        # self.add(a3)
        # self.add(a4)

        # mode 8
        for i in range(50):
            a = Atom(random.choice(x_lst), random.choice(y_lst), i, v=[random.choice([0,-1,1]), random.choice([0,-1,1])])
            self.add(a)







        print('add finished. now update..')

        while True:
            self.update()
            self.curr_state()
            time.sleep(0.1)
            print('MU: space:{} SandBox:{}'.format(sys.getsizeof(self.space), sys.getsizeof(self)))


    def curr_state(self):
        t1 = time.time()
        view = [[0 if not self.space[_][__] else 1 for _ in range(self.w)] for __ in range(self.h)]
        view = np.array(view)
        plt.figure(clear=True)
        plt.imshow(view)
        # plt.savefig()
        plt.show()
        print('time use in this epoch:{}'.format(time.time()-t1))





class Atom():
    def __init__(self, x, y, idx, v=[0,0], can_update=True):
        self.x = x
        self.y = y
        self.v = v
        self.a = 0
        self.idx = idx
        self.can_move = can_update

if __name__ == '__main__':

    send_box = SendBox(30, 30)
    send_box.run()

















