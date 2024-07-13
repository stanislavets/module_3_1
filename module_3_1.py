calls = 0

def count_calls ():
    global calls
    calls+=1

def  string_info (a):
        print((len(a), a.lower(), a.upper()))

        return count_calls()

def is_contains (string, list_to_search):
    is_true = False
    for x in list_to_search:
        if string.lower() == x.lower():
            is_true = True
    print(is_true)
   
    return count_calls()

string_info('Capybara')

string_info('Armageddon')

is_contains('Urban', ['ban', 'BaNaN', 'urBAN']) # Urban ~ urBAN

is_contains('cycle', ['recycling', 'cyclic']) # No matches

print (calls)