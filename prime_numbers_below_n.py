import datetime
starttime=datetime.datetime.now()
x=11
my_set = set()
my_set.add(2)
if x>=3:
    for numbers in range(3,x+1):
        for numerator in range(2,numbers):
                if numbers%numerator==0:
                    break
                elif(numerator+1==numbers):
                   # print(numbers)
                    my_set.add(numbers)
                else:
                    None
print(my_set)
endtime=datetime.datetime.now()
print(endtime-starttime)
print(my_set.__len__())