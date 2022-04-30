import asyncio
from random import randint
import datetime

class Counter:
    def __init__(self, count=0):
        self.__count = count

    @property
    def count(self):
        return self.__count
    
    @count.setter
    def count(self, value):
        self.__count = value

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
    await asyncio.sleep(randint(0, 2))
    counter.increment()
    return await digit_sum(number)


async def main():
    counter = Counter()
    amount = 50_000
    start = datetime.datetime.now()
    tasks = [asyncio.create_task(execute_io(i, counter)) for i in range(1, amount+1)]

    result = await asyncio.gather(*tasks)

    print(f"total time: {datetime.datetime.now() - start}")
    print(f"Finished  processing, result {sum(result)}, got counter: {counter}")

if __name__ == '__main__':
    asyncio.run(main())
