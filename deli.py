# 7-8. Deli:

# Write a program that uses a list called sandwich orders and fill it with the names of various sandwiches. 
# Then make an empty list called finished sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. 
# As each sandwich is made, move it to the list of finished sandwiches. 
# After all the sandwiches have been made, print a message listing each sandwich that was made. 
# Take a screenshot of that code and output. Paste the screenshot into a document. Label the screenshot “7-8. Deli Sandwiches” 
# Upload the document AND the program. 
# You should have your project uploaded to your GitHub account. Please make sure that I am a collaborator to your account (or at least each folder for the course).

sandwich_orders = ['tuna', 'ham', 'veggie', 'chicken']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("Finished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
