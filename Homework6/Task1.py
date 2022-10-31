#text = 'ываабв лповап абвцукв алоабвабв ываываыв'
#print(text)

#elem = input('Введите искомый элемент: ')
#def deltext(text):
#    text = [i for i in text.split() if elem not in i]
#    return " ".join(text)

#text = deltext(text)
#print(text)

text = 'ываабв лповап абвцукв алоабвабв ываываыв'
print(text)
text = list(filter(lambda x: 'абв' not in x, text.split()))
print(f'Результат: {" ".join(text)}')




