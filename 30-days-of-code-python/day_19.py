class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def getDivisors(self, n):
        if n == 1:
            return [1]

        maximum, num = n, 2
        result = [1, n]
 
        while num < maximum:
            if not n % num:
                if num != n/num:
                    result.extend([num, n//num])
                else:
                    result.append(num)
                maximum = n//num
            num += 1
        return result

    def divisorSum(self, n):
        return sum(self.getDivisors(n))


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)