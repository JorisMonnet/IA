import copy

class State(object):

    def __init__(self, values, parent=None):
        self.values = values
        self.parent = parent

    def legal(self):
        return True

    def final(self, final_values):
        return self.values == final_values

    def __hash__(self):
        return str(self).__hash__()

    def __str__(self):
        return str(self.values)

    def __eq__(self, other):
        return self.values == other.values

    def emptySpace(self) :
        for i in range(len(self.values)) :
            for j in range(len(self.values)) :
                if (self.values[i][j] == 0) :
                    return i,j
        raise Exception("No empty space")


    def inLimits(self, x, y) :
        return x in range(0,len(self.values)) and y in range(0,len(self.values)) 

    @staticmethod
    def swap(values, x1, y1, x2, y2):
        new_values = copy.deepcopy(values)
        new_values[x2][y2],new_values[x1][y1] = values[x1][y1],values[x2][y2]
        return new_values

    def applicable_operators(self):
        #list of new values after the application of possible operators
        ops = []
        posXempty,posYempty = self.emptySpace()

        for(moveX,moveY) in [(posXempty,posYempty+1),(posXempty,posYempty-1),(posXempty-1,posYempty),(posXempty+1,posYempty)]:
            if self.inLimits(moveX,moveY):
                ops.append(State.swap(self.values, posXempty,posYempty,moveX,moveY))

        return ops

    def apply(self, op):
        return State(op, self)
