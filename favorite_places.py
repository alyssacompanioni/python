# 6-9. Favorite Places:

# Write a program to use a dictionary called favorite places. 
# Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
# To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places. 
# Take a screenshot of that code and output. 
#  Paste the screenshot into a document. Label these screenshots “6-9 Favorite Places". 
# Upload the document AND the python program. 
# You should have your project uploaded to your GitHub account. Please make sure that I am a collaborator to your account (or at least each folder for the course).

favorite_places = {
    'alice': ['paris', 'new york', 'tokyo'],
    'bob': ['london', 'sydney'],
    'charlie': ['rome'],
}

for person, places in favorite_places.items():
    print(f"{person.title()}'s favorite places are:")
    for place in places:
        print(f" - {place.title()}")
