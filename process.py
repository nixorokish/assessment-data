log_file = open("um-server-01.txt") # opens the file and sets it equal to a variable called log_file


def sales_reports(log_file): # defines a fxn called sales report that takes in one argument 'log_file'
    for line in log_file: # for loop iterating through log file, assigning the item it's iterating at as 'line'
        line = line.rstrip() # removes the line break character and whatever else at the end
        day = line[0:3] # takes the items from the first (0 inclusive) to the third (4th, exclusive) index and puts them in a new variable called 'day'
        if day == "Mon": # checks if 'day' is equal to 'Mon'
            print(line) # prints the line


sales_reports(log_file) # runs the fxn on our file
