class CommaSeperatedTxtFile():
    def __init__(self, file):
        self.f = open(file, 'r')
        self.header = self.line_to_list(self.f.readline())
        self.objects = []

        for i in self.f.readlines():
            objectdict = {}
            line = self.line_to_list(i)
            for i in range(len(self.header)):
                headerElement = self.header[i]
                lineElement = line[i]
                objectdict[headerElement] = lineElement
            self.objects.append(objectdict)
        
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

file = CommaSeperatedTxtFile('xlsx.txt')
print(file.objects[0]['Firstname'])
