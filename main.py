fibonaccies = [0, 1, 1]
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    elif len(fibonaccies) >= num:
        return fibonaccies[num-1]
    else:
        currentCalculation = fibonacci(num-1) + fibonacci(num-2)
        fibonaccies.append(currentCalculation)
        return currentCalculation
    
def printFibonacci(howMany):
    for i in range(howMany):
        print(fibonacci(i))

def main():
    printFibonacci(int(input()))

if __name__ == "__main__":
    main()
