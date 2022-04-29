"""
4 categoruy 
3 buildin per category
floors
status
"""

from random import randrange, randint, choice

categorys = [
    "admin",
    "service",
    "civil",
    "security",
    
]


buildings = {
    "admin": ["commune", "daira", "ministére"],
    "civil": ["maison", "parc", "sperette"],
    "service": ["poste", "agence de voyage", "hopital"],
    "security": ["police", "pompier", "garde forét"]
}

class Building:
    
    def __init__(self, category, name, floors, status):

        self.category = category
        self.name = name
        self.floors = floors
        self.status = status

def generate_city(size):
    
    
    city = []
    
    
    for i in range(size):
        rnd_category = categorys[randrange(0, len(categorys))]
        rnd_name = buildings[rnd_category][randrange(0, len(buildings[rnd_category]))]
        
        generated_building = Building(
            category=rnd_category,
            name=rnd_name,
            floors=randint(1, 4),
            status=choice(["build", "under building", "not built"])
        )
        
        city.extend(

            [
                f"category: {generated_building.category}",
                f"name: {generated_building.name}",
                f"floors: {generated_building.floors}",
                f"status: {generated_building.status}"
            ]
        )
        print(generated_building.category, generated_building.name,generated_building.floors, generated_building.status)
        
    return city
        
        
generate_city(20)


