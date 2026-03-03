# 6-5. Rivers:

# Write a program to use a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'. 
# Use a loop to print a sentence about each river, such as "The Nile runs through Egypt." Use a loop to print the name of each river included in the dictionary. 
# Use a loop to print the name of each country included in the dictionary. 
# Take a screenshot of that code and output. 
#  Paste the screenshot into a document. Label these screenshots “6-5. Rivers.”
#  Upload the document AND the python program. 
# You should have your project uploaded to your GitHub account. Please make sure that I am a collaborator to your account (or at least each folder for the course).

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers included in the dictionary:")
for river in rivers.keys(): 
    print(river.title())

print("\nCountries included in the dictionary:")
for country in rivers.values():
    print(country.title())  
