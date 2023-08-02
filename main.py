class CommaSeperatedTxtFile():
    def __init__(self, file):
        self.f = open(file, 'r')
        self.header = self.line_to_list(self.f.readline())
        self.objects = [self.line_to_list(i) for i in self.f.readlines()]

        temp = [LineObject(self.header, i) for i in self.objects]
        self.objects = temp[:]
        self.f.close()

    def line_to_list(self, line): return line.strip().split(',')

class LineObject():
    def __init__(self, header, line):
        for i in range(len(header)):
            exec(f"self.{header[i]} = '{line[i]}'")
