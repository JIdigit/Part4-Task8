import math


class MoneyFmt:

    def __init__(self, money):
        self.dollar = money
        self.dollar_list = [i for i in str(round(money,2))]
        self.final_string = '$'+str(self.dollar)
        
    def update(self, money):
        self.dollar = round(money,2)
        self.dollar_list = str(self.dollar).split('.')
        temp_list = [i for i in self.dollar_list[0]]
        len_temp  = len(temp_list)

        if len_temp <=3:
            final = '$'+str(round(self.dollar,2))
            return ''.join(final)
        num_of_commas = len_temp//3
        counter = -3

        while num_of_commas:
            temp_list.insert(counter, ',')
            counter-=4
            num_of_commas -=1

        temp_list.append('.')
        final = '$' + ''.join(temp_list) + str(self.dollar_list[1])
        self.final_string = final
        return final
 
        

    def repr(self):
        return self.dollar

    def str(self):
        return self.final_string


    