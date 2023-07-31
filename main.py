class CommaSeperatedTxtFile():
    def __init__(self, file):
        self.f = open(file, 'r')
        self.header = self.line_to_list(self.f.readline())
        self.objects = []

        for i in self.f.readlines():
            line = self.line_to_list(i)
            self.objects.append(line)
        
        temp = []
        for i in self.objects:
            temp.append(LineObject(self.header, i))
        self.objects = temp[:]
        
    def line_to_list(self, line, delimiter = ','):
        words = []
        runningWord = ''
        for char in line.strip():
            if char != delimiter:
                runningWord += char
            else:
                words.append(runningWord)
                runningWord = ''
        words.append(runningWord)
        return words

class LineObject():
    def __init__(self, header, line):
        for i in range(len(header)):
            exec(f"self.{header[i]} = '{line[i]}'")
        self.rawLine = line

file = CommaSeperatedTxtFile('xlsx.txt')
print(file.objects[0].Lastname)
