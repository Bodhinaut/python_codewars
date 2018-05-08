"""
def expression_matter(a, b, c):
    array_of_answers = []
    sol = a * (b + c)
    sol2 = a * b * c
    sol3 = a + b * c
    sol4 = (a + b) * c
    sol5 = a + b + c
    sol6 = a * b + c
    array_of_answers.append(sol)
    array_of_answers.append(sol2)
    array_of_answers.append(sol3)
    array_of_answers.append(sol4)
    array_of_answers.append(sol5)
    array_of_answers.append(sol6)
    print (array_of_answers)
    array_of_answers = sorted(array_of_answers)
    return (array_of_answers[-1])

"""

# old method above, more efficient method below

def expression_matter(a, b, c):
    print (max(a*b*c, a+b+c, (a+b)*c, a*(b+c) ) )
    return (max(a*b*c, a+b+c, (a+b)*c, a*(b+c) ) )
    

expression_matter(2,1,2)
