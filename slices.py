
guests = ['Chris', 'Sam', 'Katie Lauren']

# print(guests[0] + ", you are invited to dinner to meet my friends.")
# print(guests[1] + ", you are invited to dinner to meet my boyfriend.")
# print(guests[2] + ", you are invited to dinner to meet my boyfriend.")

print("I have found a larger dinner table to host more guests!")

guests.insert(0, 'Rachel')
guests.insert(2, 'Hamish')
guests.append('Ben')

guests.sort()

print(guests[0] + ", you are invited to dinner to meet my boyfriend.")
print(guests[1] + ", you are invited to dinner to meet my friends.")
print(guests[2] + ", you are invited to dinner to meet my boyfriend.")
print(guests[3] + ", you are invited to dinner to meet my boyfriend.")
print(guests[4] + ", you are invited to dinner to meet my boyfriend.")

print(guests)
print("The first three items in the list are: ")
for guest in guests[:3]:
  print(guest)

print("The items in the middle of the list are: ")
for guest in guests[1:4]:
  print(guest)

print("The last three items in the list are: ")
for guest in guests[-3:]:
  print(guest)
