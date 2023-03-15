class Tesla():
    def __init__(self, model, zto60, dRange, base_price):
        self.model = model
        self.zto60 = zto60
        self.dRange = dRange
        self.base_price = base_price

    def show_range(self, dRange):
        return self.dRange
    
    def profile(self):
        return f"TESLA PROFILE:\nModel: {self.model}\nZero to 60: {self.zto60}\nRange: {self.dRange}\nBase Price: ${self.base_price:,.2f}\n" 

    def __str__(self):
        return f"Tesla model {self.model} instance. Run 'profile' method for complete profile.\n"

andys_tesla = Tesla("S", 3.1, 405, 89990)

print(andys_tesla)

print(andys_tesla.profile())

# Call and print the range for andys_tesla

# Create an instance of your own Tesla (choose a different model)

# Print the string method of the Tesla you created (__str__); remember, you don't have to call
# the __str__ method. You just print the instance of the object.

# Print the profile of the Tesla you created

# Create another instance of a Tesla

# Now, calculate and print the average range of the three Teslas created in this code (using OOP; do not hardcode the values)
