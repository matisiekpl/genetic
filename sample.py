from generator import random_program, visualize, crossover

p1 = random_program(1)
p2 = random_program(1)

visualize(p1).render('p1.pdf')
visualize(p2).render('p2.pdf')

a,b = crossover(p1, p2)
visualize(a).render('c.pdf')
