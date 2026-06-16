Band ={
    "Albumnamen":  "The Dark Side of the Moon",
    "Künstler"  :  "Pink Floyd",
    "Veröffentlichung": 1973,
    "Trackliste": ["Speak to Me","Breathe","On the Run","Time","The Great Gig in the Sky","Money","Us and Them","Any Colour You Like","Brain Damage","Eclipse"]
}

for key, value in Band.items():
    print(f"{key}: {value}")
    print("    ")

del Band[ "Veröffentlichung"]
del Band["Trackliste"]

Band["Veröffentlichung"] = "1. März 1973"


for key, value in Band.items():
    print(f"{key}: {value}")
    print("    ")

print(Band.get("Trackliste"))