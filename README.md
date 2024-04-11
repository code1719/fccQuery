# Fcc Query
The motivation behind this project is/are those random spam calls that do not get flagged by our carriers immediately. The design of the program is to take a US number that is input by the user in order to compare to the FCC Database of unwanted/spam calls. 

## Structure
The structure is pretty small and straight forward. It contains two functions, a search function to call upon the API for a request. 

### def search_number()
def search_number is the definition of the function which gathers the user input and then uses the phonenumbers module to parse the information (redundant. In future intended to be used if the number != information in the fcc data). After the information is parsed using phonenumbers module, it is then balanced to see if the caller ID matches an object within the "record". If so, the information is displayed. If not, the program will return that the information is not found in the database. 

### def get_json_data()
def get_json_data handles the response of the API which is in JSON format

### Other
The rest of the program sets up a variable for the data = response. Also defines the GUI 