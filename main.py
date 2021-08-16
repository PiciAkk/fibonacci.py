fibonaccies = []
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    elif len(fibonaccies) >= num:
        return fibonaccies[num]
    else:
        currentCalculation = fibonacci(num-1) + fibonacci(num-2)
        fibonaccies.append(currentCalculation)
        return currentCalculation
    
def printFibonacci(howMany):
    for i in range(howMany):
        print(fibonacci(i))

printFibonacci(100)
