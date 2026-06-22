#def hello(hi, *names):
  #for name in names:
    #print(hi, name)

#hello("Hello", "Emil", "Tobias", "Linus")


def lam(n):
    return lambda a:a*n
mydoubler= lam(2)
print(mydoubler(10))