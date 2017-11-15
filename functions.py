'''
def my_function():
	print("Hello, I'm a function")

my_function()

def grand_total(product_cost,shipping_cost):
	grand_total = product_cost + shipping_cost
	print(str(grand_total))
grand_total(23,2)

def return_function():
	example_text = "This is a return function"
	return example_text
return_function()

text_to_print = return_function()
print(text_to_print)

def list_to_dictionnary(parameters_list):
	dictionnary = {}
	results_list = []
	for i,j in parameters_list:
		dictionnary[i] = j
	return(dictionnary)
tupled_list = [('Buenas','tardes'),('Buenas','noches'),('Buenos','días')]
print(list_to_dictionnary(tupled_list))

input(float)
'''

print set[set('Buenas','tardes'),set('Buenas','noches'),set('Buenos','dias')]