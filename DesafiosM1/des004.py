v = input('Insira alguma coisa: ')
print('O tipo primitivo de {0} é {1}'.format(v, type(v)))
print('{0} só tem \033[4mEspaços\033[m? {1}'.format(v, v.isspace()))
print('{0} é um \033[4mNúmero\033[m? {1}'.format(v, v.isnumeric()))
print('{0} é uma \033[4mLetra\033[m? {1}'.format(v, v.isalpha()))
print('{0} é \033[4mAlfanumérico\033[m? {1}'.format(v, v.isalnum()))
print('{0} está em \033[4mMaiúsculas\033[m? {1}'.format(v, v.isupper()))
print('{0} está em \033[4mMinusculas\033[m? {1}'.format(v, v.islower()))
print('{0} está \033[4mCapitalizada\033[m? {1}'.format(v, v.istitle()))
print('{0} é \033[4mASCII\033[m? {1}'.format(v, v.isascii()))
print('{0} é \033[4mDecimal\033[m? {1}'.format(v, v.isdecimal()))
print('{0} é \033[4mDígito\033[m? {1}'.format(v, v.isdigit()))
print('{0} é \033[4mIdentifier\033[m? {1}'.format(v, v.isidentifier()))
print('{0} é \033[4mPrintavel\033[m? {1}'.format(v, v.isprintable()))