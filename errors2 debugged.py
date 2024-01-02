# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = 'Lion' # runtime corrected: lion was not defined commas were added to identify as str

animal_type = "cub"
number_of_teeth = 16

'''
-logical error corrected below: 
-format string was not set up properly. f was added before the comma to format the string 
- the sentence structure corrected by switching {animal type} with {number of teeth}
'''
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" 


print (full_spec) #syntax error corrected: missing perenthesis 