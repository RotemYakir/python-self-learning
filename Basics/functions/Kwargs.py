# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments

def hello(**details):
    # print("Hello " + kwargs['first'] + " " + kwargs['last']) #what if someone has a middle name?
    print("Hello ", end=" ")
    for key,value in details.items():
        print(value,end=" ")

hello(title="Mr.",first="Bro",middle="Dude",last="Code")