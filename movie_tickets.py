# 7-5. Movie Tickets: 

# Write a program for a movie theater that charges different ticket prices depending on a person’s age. 
#  If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 
# The program will prompt the user for the number of tickets.  Write a loop which asks the user for the ages of the ticket holders, and then tells them the total cost of their movie tickets. 
# Take a screenshot of that code and output.  Paste the screenshot into a document.  Label the screenshot “7-5. Movie Tickets.” 
# Upload the document AND the program. 
# You should have your project uploaded to your GitHub account. Please make sure that I am a collaborator to your account (or at least each folder for the course).

def calculate_ticket_price(age):
    if age < 3:
        return 0
    elif 3 <= age <= 12:
        return 10
    else:
        return 15
    
def main():
    total_cost = 0
    num_tickets = int(input("How many tickets do you need? "))
    
    for i in range(num_tickets):
        age = int(input(f"Enter the age of ticket holder {i + 1}: "))
        total_cost += calculate_ticket_price(age)
    
    print(f"The total cost of the movie tickets is: ${total_cost}")

if __name__ == "__main__":
    main()
