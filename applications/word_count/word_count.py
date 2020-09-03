def word_count(s):
    # Your code here
    dicti = {}
    ss = s.split()
    y = r'" : ; , . - + = / \ | [ ] { } ( ) * ^ &'
    ys = y.split()
    empty = False
    for i in ss:
        a = i.lower()
        for c in ys:
            b = a.find(c)
            if b != -1:
                empty = True
                a = a.replace(c, '')
        if len(dicti) == 0:
            dicti[a] = 1
        else:
            f = dicti.get(a)
            if f == None:
                dicti[a] = 1
            else:
                dicti[a] += 1
    if empty == False:
        dicti = {}
        return dicti
    else:
        return dicti




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))