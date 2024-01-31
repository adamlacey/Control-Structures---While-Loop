def get_valid_integer(prompt):
   while True:
      try:
         user_input = input(prompt)
         user_input = int(user_input) # Converting input to an integer.
         
         if user_input < -1:
            print("Please enter a non-negative integer.")
         else:
            return user_input # Return valid input if all conditions are met.
     
      except ValueError:
         print("Invalid input. Please enter a valid integer.")

def main():
   sum = 0
   count = 0

   while True:
      my_num = get_valid_integer("Please enter a valid number: ")
   
      if my_num == -1:
         break # Loop will exit if -1 is entered.

      sum += my_num
      count += 1
   
   if count > 0:
      print(f"The average is: {sum / count}")
   
if __name__ == "__main__":
   main()