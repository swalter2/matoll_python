from nltk.corpus import stopwords
import string
STOPWORDS = stopwords.words('german')

input_text = 'UELNW ETTHE CSTEN AGSEZ UCPRL INEIE DISSS CINRA DUAZN AETTC ÜITWE ADLTG CRSNH FTULD HNIHL EATMA ZNRHS ÜEBUV TSEAN'

input_text = input_text.lower()
input_text = input_text.replace(' ','')
input_text_ord = []
for x in list(input_text):
    input_text_ord.append(ord(x))

print(input_text_ord)
#>>> chr(65)
#'A'
#>>> ord('A')
#65

#define lower and upper bound:
lower_a = ord(list(string.ascii_lowercase)[0])
upper_a = ord(list(string.ascii_lowercase)[len(list(string.ascii_lowercase))-1])
print(lower_a,upper_a)
for i in range(1,30):
    tmp_input_text_ord = input_text_ord
    for x in range(0,len(tmp_input_text_ord)):
        value = tmp_input_text_ord[x] + i
        if value > upper_a:
            value = value - upper_a
            value += lower_a
        tmp_input_text_ord[x] = value
    output = ''
    for x in tmp_input_text_ord:
        output+=chr(x)
    enable_output = False
    counter = 0
    for s in STOPWORDS:
        if s in output:
            enable_output = True
            output = output.replace(s,'__'+s+'__')
            counter += 1
    if enable_output:
        print(counter,output)


#characters = list(string.ascii_lowercase)
#characters.append('0')
#characters.append('1')
#characters.append('2')
#characters.append('3')
#characters.append('4')
#characters.append('5')
#characters.append('6')
#characters.append('7')
#characters.append('8')
#characters.append('9')
#characters.append(' ')

#for p in string.punctuation:
#    characters.append(p)

#for addition in range(0,len(characters)-1):
#    output_text = input_text
#    output_text = list(output_text)
#    for i in range(0, len(characters)-1):
#        input_character = characters[i]
#        replace_value = i+addition
#        if replace_value > len(characters)-1:
#            replace_value = replace_value - (len(characters)-1)
#        replace_character = characters[replace_value]
#        for x in range(0,len(output_text)-1):
#            if output_text[x] == input_character:
#                output_text[x] = replace_character+"_r"
#    output_plain = ''
#    for x in range(0, len(output_text) - 1):
#        output_plain+=output_text[x].replace('_r','')
#    enable_output = False
#    counter = 0
#    for s in STOPWORDS:
#        if s in output_plain:
#            enable_output = True
#            output_plain = output_plain.replace(s,'__'+s+'__')
#            counter += 1
#    if enable_output:
#        print(counter,output_plain)
#






