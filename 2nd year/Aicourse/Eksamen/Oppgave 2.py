class MyIterable:

    def __init__(self,maxval):
        self.maxval = maxval
        self.value = 0
    
    def __iter__(self):
        while True:
            self.value += 7
            if self.value > self.maxval:
                # raise StopIteration # Eller break
                break
            yield self.value
    
iter = MyIterable(30)

for i in iter:
    print(i)
