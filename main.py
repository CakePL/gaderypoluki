def g_key():
    return 'GA-DE-RY-PO-LU-KI'


def p_key():
    return 'PO-LI-TY-KA-RE-NU'


def gen_dict(key):
    result = {}
    for word in key.split('-'):
        if len(word) != 2:
            return None
        a, b = word
        if a == b or not a.isupper() or not b.isupper() or a in result or b in result:
            return None
        result[a] = b
        result[b] = a
    return result


G_DICT = gen_dict(g_key())
P_DICT = gen_dict(p_key())


def encode(mess, dic):
    return ''.join(dic[letter] if letter in dic else letter for letter in mess.upper())


if __name__ == '__main__':
    a = input('Do you want to use GA-DE-RY-PO-LU-KI, PO-LI-TY-KA-RE-NU or a custom key? Type G/P/C...\n')
    while a not in ['G', 'P', 'C']:
        a = input("Invalid input! Type 'G', 'P' or 'C...\n")
    if a == 'G':
        dic = G_DICT
    elif a == 'P':
        dic = P_DICT
    else:
        key = input("Type your custom key. For example 'KO-NI-EC-MA-TU-RY'...\n")
        dic = gen_dict(key)
        while dic is None:
            key = input("Incorrect key!\nyour key must consist of pairs of different capital letters separated with "
                        "'-' sign.\nType correct one...\n")
            dic = gen_dict(key)
        print('Correct key!\n')
    mess = input('Type your message...\n')
    print(f'Your message encoded:\n{encode(mess, dic)}\n')
