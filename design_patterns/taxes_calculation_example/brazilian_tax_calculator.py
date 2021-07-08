
from taxes import ISS, ICMS

class Brazilian_tax_calculator(object):

    def tax_calculation(self, budget, tax):

        tax_calculated = tax.calculator(budget)
            
        print(tax_calculated)

if __name__ == '__main__':

    from budget import Budget

    calculator = Brazilian_tax_calculator()

    budget = Budget(50000)

    calculator.tax_calculation(budget, ISS())
    calculator.tax_calculation(budget, ICMS())
