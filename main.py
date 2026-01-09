import re
import os

num = str(input('Enter the phone number in the format +309834784XXX or +3474XXX9993: '))
num = num.upper()

with open(f"contact_list.vcf", "w") as output:
    output.write("")  

pattern = r"X"  
matches = re.findall(pattern, num)

numbers = []  

def generate_number(n: int, m: int, prefix=None, result=""):
    prefix = prefix or []
    if m == 0:  
        if "X" not in result:  
            write_contact(result)
            numbers.append(result)
        return

    for digit in range(n):
        prefix.append(digit)
        if len(prefix) <= len(matches):  
            new_result = result.replace("X", str(prefix[-1]), 1)  
        else:
            new_result = result
        generate_number(n, m - 1, prefix, new_result)
        prefix.pop()

def write_contact(number):
    with open("contact_list.vcf", "a") as output:
        contact = f"BEGIN:VCARD\nVERSION:2.1\nN:;search_{number};;;\nFN:search_{number}\nTEL;CELL;search_{number}\nEND:VCARD"
        output.write(contact + "\n")

generate_number(10, len(matches), result=num)

print('All numbers are saved in contact_list.vcf')

