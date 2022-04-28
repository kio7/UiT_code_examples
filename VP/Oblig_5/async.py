import asyncio
from random import uniform

class Counter:
    def __init__(self, count=0):
        self.__count = count

    @property
    def count(self):
        return self.__count
    
    @count.setter
    def count(self, value):
        self.count = value

    def increment(self):
        self.count += 1
    
    def __str__(self):
        return f"{self.count}"


async def digit_sum(num):
    sum = 0

    for digit in str(num): 
      sum += int(digit)      

    return sum
    

async def execute_io(number:int, counter:Counter) -> int:
    await asyncio.sleep(uniform(0, 2))
    counter.increment()
    return digit_sum(number)


async def main(tasks, num, counter):
    lis = []
    for i in range(tasks):
        task = asyncio.create_task(execute_io(num, counter))
        lis.append(task)

    return_lis = []
    async for elem in lis:
        result = await asyncio.gather(elem)
        return_lis.append(result)

    return return_lis


if __name__ == '__main__':
    counter = Counter()
    num = int(input("Enter an amount of tasks: "))
    amount = 10
    result = asyncio.run(main(amount, num, counter))

    print(f"Finished  processing, result {sum(result)}, got counter: {counter.count}")
