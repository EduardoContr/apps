# apps
Full documentation here:  

Requirements
track nutritional value by nutrient, by meal

Design
UDF's capture requirements
Class reuses code for daily tracker establishing value by meal and estimate to complete

Test
See snapshots

Code:

##The daily noot diary app shows what enduser ate by name, eg., a muffin,
##a 7 grain cereal from Bob's Redmill not sold here, and cup of milk
diarylist = ['muffin','7grainscereal','milk']
strvar = 'muffin'
strvar2 = '7grainscereal'
strvar3 = 'milk'
##Next let us assign these for overhead efficiency to a variable, as shown above; and
##let's just assign them to a value for its nutritional content-item, potassium
potassiumlist = [(strvar,3),(strvar2,8),(strvar3,9)]
print(potassiumlist)
print(potassiumlist[0])
##Enduser output for these items will show (from above) the items and values, as well as the
##very first index value for testing.  Test today at 11:00 a.m. E.S.T. showed the list was printed with success
## as [('muffin',3),('7grainscereal', 8),('milk',9)] and ('muffin', '3') the test value of an index or
## first slice (index[1] shows slice two or ('7grainscereal',8) employing the tuple object type.

def funcsx(potassiumlist):
    nest = []
    for vars, vals in potassiumlist:
        print (vals)
        nest.append(vals)
        print(nest)
        print (sum(nest))
    return (sum(nest))

funcsx(potassiumlist)
results1ofPotassium = funcsx(potassiumlist)
print (results1ofPotassium)
##using a user defined function (UDF) we are able to do some work to automate; using a loop for each item
##entered as user input in the app *by customer (fn), the item's tuple object at position or slice pertaining
##to that item is included, returned at the end of the iterations over the list as sum.  Test passed 12:30 toeday
## E.S.t.
def xfunc(vars1):
    potassmax = 100
    potassmaxcalc = potassmax - vars1
    print(potassmaxcalc)
    resultsof1 = potassmaxcalc
    print(resultsof1)
    return(resultsof1)


xfunc(results1ofPotassium)

maxresultofPotassium = xfunc(results1ofPotassium)
print(maxresultofPotassium)

##In section shown above, the second of two UDF's is shown so that one enduser can calculate the
##a second value, the quantity remaining of the nutrient tracked in this session, namely, potassium
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
