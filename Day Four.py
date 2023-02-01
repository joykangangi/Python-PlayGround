def register_check(dictionary: dict):
    count = 0
    for value in dictionary.values():
        if value == 'Yes'.casefold():
            count = count +1
    return "Pupils Present is: {}".format(count)    

pupil_register = {'Kimemia': 'yes', 'Tania':'no','Mike':'yes','Whitney':'yes'}
register_check(pupil_register)           
