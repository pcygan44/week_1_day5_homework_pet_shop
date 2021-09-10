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