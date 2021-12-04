def custom_iterator(content):
  """ Defines a custom iterator that has to iterate through any type of       input 
  """
  print ("Iterating through ...")

  for item in content:
    print (item)

def define_list():
  my_list = [1, 2, 3, 4, 5]
  my_list2 = ["arthi", "parthiban", "agaran"]
  custom_iterator(my_list)
  custom_iterator(my_list2)

def define_tuple():
  my_tuple = (1, 2, 3, 4, 5)
  custom_iterator(my_tuple)


def define_set():
  my_set = {1, 2, 3}
  custom_iterator(my_set)


def compute_all(all_methods):
  print ("****** Hello welcome to my world ******* \n\n\n")
  for item in all_methods:
    print (f"Invoking {item.__name__}()")
    item()
    print("\n")

if __name__ == "__main__":
  all_methods = (define_list, define_set, define_tuple)
  compute_all(all_methods)