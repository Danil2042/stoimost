stroka = input('Введите чтото что стоит дорого и вам не нужно:')
dlina = len(stroka)
stoimost = dlina * 60
kopeyki = str(stoimost)[-2:]
rubls = stoimost // 100
print('С вас:', rubls, "р.", kopeyki, "коп.")
