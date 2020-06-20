import re

replace_LIST = [
                 ['dr\.','']
                ,['DR\.','']
                ,['m\.d\.','']
                ,['M\.D\.','']
                ,['p\.o', 'orally']
                ,['P\.O', 'orally']
                ,['q\.d\.', 'once a day']
                ,['Q\.D\.', 'once a day']
                ,['I\.M\.', 'intramuscularly']
                ,['i\.m\.', 'intramuscularly']
                ,['b\.i\.d\.', 'twice a day']
                ,['B\.I\.D\.', 'twice a day']
                ,['Subq\.', 'subcutaneous']
                ,['SUBQ\.', 'subcutaneous']
                ,['t\.i\.d\.', 'three times a day']
                ,['T\.I\.D\.', 'three times a day']
                ,['q\.i\.d\.', 'four times a day']
                ,['Q\.I\.D\.', 'four times a day']
                ,['I\.V\.', 'intravenous']
                ,['i\.v\.', 'intravenous']
                ,['q\.h\.s\.', 'before bed']
                ,['Q\.H\.S\.', 'before bed']
                ,['O\.D\.', 'in the right eye']
                ,['o\.d\.', 'in the right eye']
                ,['5X', 'a day five times a day']
                ,['5x', 'a day five times a day']
                ,['O\.S\.', 'in the left eye']
                ,['o\.s\.', 'in the left eye']
                ,['q\.4h', 'every four hours']
                ,['Q\.4H', 'every four hours']
                ,['O\.U\.', 'in both eyes']
                ,['o\.u\.', 'in both eyes']
                ,['q\.6h', 'every six hours']
                ,['Q\.6H', 'every six hours']
                ,['q\.o\.d\.', 'every other day']
                ,['Q\.O\.D\.', 'every other day']
                ,['prn\.', 'as needed']
                ,['PRN\.', 'as needed']
                ,['[0-9]+\.','']
                ,[r'\[\*.+\*\]','']
                ]
def preprocess_re_sub(x):
    processed_text = x
    for find,replace in replace_LIST:
        processed_text=re.sub(find,replace,processed_text)
    return processed_text