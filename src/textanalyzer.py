#count_char method.
#which count the total value 
def count_char(text, char):
    
    count = 0
    for c in text:
        if( c == char):
            count += 1
    
    return count;

#insert filename
filename = str(raw_input("Enter filename: "))

#read data
with open(filename) as data:
    text = data.read();
    
    #print data
    #print(text);
    
    #search for the value
    count = str(count_char(text, "v"))
    print("Counted value: " + count)
    
    
#print pecentage
for char in "abcdefghijklmnopqrstuvwxyz":
    percentage = 100 * count_char(text, char) / len(text)
    
    print("{0} = {1}%" .format(char, round(percentage, 2)))
    
    
    
    
