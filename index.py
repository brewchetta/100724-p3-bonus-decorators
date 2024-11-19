from classes.bird import Bird
from classes.fish import Fish

cardinal = Bird(name="cardinal")
woodpecker = Bird(name="woodpecker")
yellow_breasted_tit = Bird(name="yellow breasted tit")
blue_footed_booby = Bird(name="blue footed booby", category="water")
egret = Bird(name="egret", category="water")
egret.BRAIN_SIZE = 'gigantic' # overwrites the constant JUST for the very smart egret