def reg(regex, inp):
    if not regex:
        return True
    elif not inp:
        return False
    elif ('\\') in regex:
        try:
            slash = regex.find('\\')
            regex = regex.replace(regex[slash + 1], '.')
            c, d = regex.split(r'\\')
            regex = c + d
            return reg(regex, inp)
        except:
            return reg(regex[1:], inp)
    elif "+" in regex:
        c, d = regex.split('+')
        if inp.startswith(c) and inp.endswith(d):
            regex = ''
        else:
            regex = c + d
            inp = inp[:len(c) - 1] + inp[-len(d) + 1:]
        return reg(regex, inp)
    elif regex[0] == '^':
        return reg(regex[1:], inp[:len(regex) - 1])
    elif regex[-1] == "$":
        return reg(regex[:-1], inp[- len(regex) +1:])
    elif '?' in regex:
        c, d = regex.split('?')
        if c + d == inp:
            regex =''
        else:
            regex = c[:-1] + d
        return reg(regex, inp)
    elif '*' in regex:
        c, d = regex.split('*')
        if inp.startswith(c) and inp.endswith(d):
            regex =''
            inp = c + d
        else:
            regex = c[:-1] + d
        return reg(regex, inp)
    elif regex[0] not in ['.', '', inp[0]]:
        return reg(regex, inp[1:])
    elif regex in inp:
        return True
    else:
        return reg(regex[1:], inp[1:len(regex)+1])

#a, b = input().split('|')
#print(reg(a,b))
#task=['apple|apple', 'a|apple', '^a|apple', 'le|apple', 'le$|apple', 'apple$|apple pie', '^apple|tasty apple', '.$|apple', '^apple$|apple pie']
task = ['3\+3|3+3=6']
count=0
for x in task:
    a, b = x.split('|')
    print(f'{count}. {reg(a,b)}')
    count+=1

