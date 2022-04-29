# city generator
from random import randrange, choice, randint

categorys = ["administrative", "civil", "service", "securité"]

Buildings = {
    "administrative": ["commune", "daira", "ministére"],
    "civil" : ["maison", "parc", "sperette"], 
    "service":["poste", "agence de voyage", "hopital"],
    "securité":["police", "pompier", "garde forét"]
}



class Building:
    
    def __init__(self, category, name, floors, status):
        self.category = category
        self.name = name
        self.floors = floors
        self.status = status


def generate_city(city_size):
    
    city = []
    
    
    while city_size > 0 :
        
        rnd_category = categorys[randrange(0, len(categorys))]
        
        rnd_name = randrange(0,3)
        
        created_building = Building(
            
            category=rnd_category,
            name=Buildings[rnd_category][rnd_name],
            floors=randint(1, 5),
            status=choice(["under building", "build"])
        
        )
        
        city.extend(
            
            [
                f"category: {created_building.category}",
                f"name: {created_building.name}",
                f"floors: {created_building.floors}",
                f"status: {created_building.status}"
            ]
        )  
        city_size -= 1
    
    return city       



generate_city(10) 