'''
Used as an actual library, rather than for the physics_seeker.py client
(the original version, electric_library, parses user input instead of taking 
parameters)
'''

import math
import numbers

e = 0.0000000000000000001602 #elementary charge, e = 1.602 * 10^-19 Coulombs
k = 8988000000 #a proportionality constant, k = 8.988 * 10^9 (N*m^2)/C^2

#work needed to pull an electron (charge -e) out to distance (rf) from
# a fixed proton (charge +e) from initial distance (r0)'''
def work_needed(r0, r1):
	w = None

	#work already done
	w0 = (k*e*e)/r0
	#total work from origin
	w1 = (k*e*e)/rf

	#work needed to reach rf from r0
	w = math.fabs(w1 - w0)
	return w


#returns a capacitors charge, stored energy, or electric field,
# depending on the fourth parameter
def capacitor_info(c, v, d, *ret_type):
	#given capacitance C, applied voltage V, distance between plates d

	if(len(ret_type) != 1):
		raise Exception('capacitor_info() only takes 4 arguments. The fourth '
				'specifies whether to return charge \'q\', stored '
				'energy \'u\', or electric field \'ef\'.')

	ret_type = ret_type[0]
	dict = {}

	#charge on capacitor
	dict['q'] = c*v
	#stored energy
	dict['u'] = 0.5 * dict['q'] * v
	#electric field
	dict['ef'] = float(v)/d

	#raises ValueError if ret_type is not valid
	if(ret_type not in dict):
		raise ValueError('Fourth argument must be charge \'q\', stored '
				'energy \'u\', or electric field \'ef\'.')

	return dict[ret_type]


#returns capacitor charge. This can be used when only
# capacitance and voltage are known.
def capacitor_charge(c, v):
	return c*v


#calculate potential difference V
def potential_difference(*args):

	#check for valid arguments
	ermsg = ('potential_difference() takes 4 arguments. '
		 'arg1 and arg2 are numerical values. arg3 '
		 'and arg4 are strings specifying what arg1 '
		 'and arg2 are respectively. For example, '
		 '(7, 8, \'I\', \'R\') would represent a current '
		 'of 7 amps and a resistance of 8 ohms.')

	if(	len(args) != 4
	    or  False in [isinstance(x, numbers.Number) for x in args[0:2]]
	    or  False in [isinstance(s, basestring) for s in args[2:4]]
	  ):
		raise ValueError(ermsg)

	#connect numerical args to their string args
	dic = {}
	dic[str(args[2])] = int(args[0])
	dic[str(args[3])] = int(args[1])

	return 'test_return'
	
	#....

