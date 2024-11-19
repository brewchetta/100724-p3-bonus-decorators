class Bird:

    things_that_make_a_bird = 'hollow bones'
    # if we overwrite this in an instance, the instance attribute takes precedence

    BRAIN_SIZE = 'tiny'
    # BRAIN_SIZE is a constant for ALL birds

    all_birds = []
    all_flying_birds = []
    all_water_birds = []


    @classmethod
    def number_of_birds(cls): # cls is Bird
        return len( cls.all_birds )
    

    @classmethod
    def flying_bird_names(cls):
        bird_names = [] # this is the list we will return

        for bird in cls.all_flying_birds:
            bird_names.append( bird.name )

        return bird_names
    

    @classmethod
    def water_bird_names(cls):
        return [ bird.name for bird in cls.all_water_birds ] # list comprehension


    def __init__(self, name, category="flying"):
        self.name = name
        Bird.all_birds.append(self)
        if category == "flying":
            Bird.all_flying_birds.append(self)
        if category == "water":
            Bird.all_water_birds.append(self)

    def __repr__(self):
        return f"Bird(name={self.name})"

    def tweet(self):
        return f"{self.name} is posting many controversial tweets"
    
# BIRD CLASS ENDS HERE