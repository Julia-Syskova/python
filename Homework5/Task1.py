text = 'ываабв лповап абвцукв алоабвабв ываываыв'
print(text)

elem = input('Введите искомый элемент: ')
def deltext(text):
    text = list(filter(lambda x: elem not in x, text.split()))
    return " ".join(text)

text = deltext(text)
print(text)