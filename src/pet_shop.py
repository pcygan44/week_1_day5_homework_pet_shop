# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name( shop):
   
    return shop["name"]


def get_total_cash(shop):
    
    return  shop["admin"]["total_cash"]


def add_or_remove_cash (shop, amount):
    
    shop["admin"]["total_cash"] += amount
    
def get_pets_sold (shop):
    return shop["admin"]["pets_sold"]
   

def increase_pets_sold (shop, new_pets):
    shop["admin"]["pets_sold"] += new_pets

    
def get_stock_count (shop,):
    return len(shop["pets"])

    
def get_pets_by_breed(shop, breed):
    breed_count = []
    for pet in shop["pets"]:
        if pet["breed"] == breed: 
            breed_count.append(shop["pets"])

    return breed_count

def find_pet_by_name (shop, pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(shop, remove_pet_name):
    # pet_to_deleat = None
    find_pet = find_pet_by_name(shop, remove_pet_name)

    if find_pet["name"] == remove_pet_name:
        shop["pets"].remove(find_pet)
        pet_to_deleat = find_pet
        return find_pet["name"]
    
def add_pet_to_stock (shop, add_new_pet):
    shop["pets"].append(add_new_pet)


def get_customer_cash (customer):
    return customer["cash"]

def remove_customer_cash (customer, amount_of_removerd_moeny):
    customer["cash"] = customer["cash"] - amount_of_removerd_moeny
    return customer["cash"]

def get_customer_pet_count(custoemr):
    total_customer_pets = len(custoemr["pets"])
    return total_customer_pets

def add_pet_to_customer(customer, new_pet):


