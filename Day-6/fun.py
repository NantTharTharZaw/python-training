def my_function():
  print("Hello from a function")

my_function()
my_function()

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)


# parameter and argunments
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an parametert

# default parameter value
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

# Keyword Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")


# Arbitrary Arguments - *args
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Scope
def myfunc():
  x = 300
  print(x)
myfunc()

