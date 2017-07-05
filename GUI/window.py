from collections import Counter

class Manager:
    def __init__(self, size=10):
        self.size = size
        self.q = [];

    def getMostFrequent(self):
        data = Counter(self.q + (self.size//5 * [2]));
        print (self.q);
        return data.most_common(1)[0][0]

    def add(self, event):
        if event in [2,5,9,12]: event = 2;
        self.q.append(event)
        n = len(self.q)
        print(n)
        if n == self.size + 1: self.q.pop(0);
        most_frequent = self.getMostFrequent()
        return most_frequent
        