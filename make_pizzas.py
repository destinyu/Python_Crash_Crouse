#import pizza
#pizza.make_pizza(16,'pepperoni')
#pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')

from pizza import make_pizza as mp
mp(16,'a')

import pizza as p
p.make_pizza(12,'b')

from pizza import *