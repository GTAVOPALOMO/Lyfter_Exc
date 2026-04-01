#Dada una lista de ventas con la siguiente información: Cree un diccionario que guarde el total de ventas de cada UPC
sales = [
	{
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
]
print(f"Dada una lista de ventas con la siguiente información:{sales} Cree un diccionario que guarde el total de ventas de cada UPC")

new_dic = {}
for dic in sales:
    temp_list = dic.get("items")
    for item in temp_list:
        upc = item.get("upc")
        if upc not in new_dic:
            new_dic[upc] = 0
        new_dic[upc] += item.get("unit_price")
print(f"Total de ventas: \n{new_dic}")

#Agrupar empleados por departamento
print("Agrupar empleados por departamento")
employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

dep_emp = {}
for emp in employees:
    key = emp.get("department")
    if key not in dep_emp:
            dep_emp[key] = []
    dep_emp[key].append(emp)
print(dep_emp)


#Dada una lista de productos vendidos, donde cada uno tiene categoría y precio, cree un diccionario que acumule el total por categoría.
print("Dada una lista de productos vendidos, donde cada uno tiene categoría y precio, cree un diccionario que acumule el total por categoría.")

products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

category_total = {}
for product in products:
    key = product.get("category")
    if key not in category_total:
        category_total[key] = 0
    category_total[key] += product.get("price")
print(category_total)


