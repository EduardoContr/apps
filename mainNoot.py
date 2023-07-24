class Potassiums ():
    pass
OnePotassium = Potassiums()
type(OnePotassium)
class Potassiums2 ():
    maxval = 4700
    def __init__(self,maxy,abbrev):
        self.maxy = maxy
        self.abbrev = abbrev
    def clfunc(self,valueonethird,value_a):
        print(f"let us recall what our max recommended value {self.maxy} of intake "
              f"for this nutrient:  \nPotassium.  \nMeal target:  your target or one third is, \n{valueonethird}")
        print(f"and, get this!  and, you can see below you ate this percent of your meal allowance "
              f"\n{value_a/valueonethird}")

##//hi add an object method to use the 4700 val and get remainder
OnePotassium2 = Potassiums2(maxy=4700,abbrev='pass')
print(type(OnePotassium2))
print(OnePotassium2.maxy)
OnePotassium2.clfunc(1400,1200)
print(f'and your daily goal you will recall, in total is\n {Potassiums2.maxval}')

##The object oriented approach allows reuseability - reuseability may be needed as the enduser
##may require a history of the nutrients eaten over time;  with udf's the code needs to be rewritten
##for each day:  so if tomorrow the end user enters new data for breakfast, then the data of today
##may be lost as one is resetting manually the list and effectively changing the variable to another
##setting in order to keep a daily record.  yesterday, for example would be stored and today
##the code would be rewritten to capture new stored values so the variable would need to be changed
##to a new name.  In light of that using an object oriented approach would be a more readily usable
##alternative.  Solving for the amount consumed
