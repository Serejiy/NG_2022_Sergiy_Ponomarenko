alphabet =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
shift = int(input('Step: '))
text = input("Text for decipher: ").upper()
out = ''
for i in text:
  position = alphabet.find(i)
  new_position = position + shift
  if i in alphabet:
    out += alphabet[new_position]
  else:
    out += i
print (out)