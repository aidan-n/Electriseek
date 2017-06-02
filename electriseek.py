'''
Assume SI units for all variables.
'''

import math
import numbers

#constants
e = 0.0000000000000000001602 #elementary charge, e = 1.602 * 10^-19 Coulombs
k = 8988000000 #a proportionality constant, k = 8.988 * 10^9 (N*m^2)/C^2


#work needed to pull an electron (charge -e) out to distance (rf) from
# a fixed proton (charge +e) at initial distance (r0)
def work_needed(r0, r1):
	w = None

	#work already done
	w0 = (k*e*e)/r0
	#total work from origin
	w1 = (k*e*e)/rf

	#work needed to reach rf from r0
	w = math.fabs(w1 - w0)
	return w


#calculate potential difference V
def potential_difference(*args):

	#check for valid arguments
	ermsg = ('potential_difference() takes 4 or 6 arguments. Arguments in the '
		 'first half are numerical values. Arguments in the second half '
	         'are strings, specifying what the numerical values are respectively. '
        	 'For example, (7, 8, \'I\', \'R\') would represent a current '
		 'of 7 amps and a resistance of 8 ohms.')

	length = len(args)
	half = len(args)/2

	if(
	    length not in [4, 6]
	    or  False in [isinstance(x, numbers.Number) for x in args[ 0 : half ]]
	    or  False in [isinstance(s, basestring) for s in args[ half : length ]]
	  ):
		raise ValueError(ermsg)


	#connect (lower-case) string args to their numerical args
	dic = {}
	for i in range(half):
		dic[str.lower(str(args[ half + i ]))] = int(args[i])


	#potential difference v
	if length == 4:

		if('e' in dic and 'x' in dic):
			v = (-1) * dic['e'] * dic['x']
			return v

		if('i' in dic and 'r' in dic):
			v = dic['i'] * dic['r']
			return v

		if('p' in dic and 'i' in dic):
			v = float(dic['p']) / dic['i']
			return v

		if('w' in dic and 'q' in dic):
			v = float(dic['w']) / dic['q']
			return v

		if('q' in dic and 'c' in dic):
			v = float(dic['q']) / dic['c']
			return v

		if('p' in dic and 'r' in dic):
			if( (dic['p'] * dic['r']) < 0 ):
				ermsg = 'Can not take negative values for power or resistance.'
				raise ValueError(ermsg)
			v = math.sqrt(dic['p'] * dic['r'])
			return v

		if('u' in dic and 'q' in dic):
			v = (2 * dic['u']) / float(dic['q'])
			return v

		if('u' in dic and 'c' in dic):
			v = math.sqrt( (2 * dic['u']) / float(dic['c']) )
			return v

		raise ValueError('potential_difference() does not support calculation '
				 'based on the combination of ' + args[2] + ' and ' +
				 '' + args[3])

	''''''
	if length == 6:

		if('k' in dic and 'q' in dic and 'r' in dic):
			v = (dic['k'] * dic['q']) / float(dic['r'])
			return v

		raise ValueError('potential_difference() does not support calculation '
				 'based on the combination of ' + args[3] + ', ' +
				 args[4] + ', ' + 'and ' + args[5])


	raise ValueError('Invalid arguments.')


#returns a capacitor's charge, stored energy, or electric field,
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


def charge(*args):

	#check for valid arguments
	ermsg = ('charge() takes 4 arguments. Arguments in the '
		 'first half are numerical values. Arguments in the second half '
		 'are strings, specifying what the numerical values are respectively. '
		 'For example, (7, 8, \'V\', \'C\') would represent '
	         'a potential difference of 7 volts and a capacitance of 8 farads.')

	length = len(args)
	half = len(args)/2

	if(
	    length != 4
	    or  False in [isinstance(x, numbers.Number) for x in args[ 0 : half ]]
	    or  False in [isinstance(s, basestring) for s in args[ half : length ]]
	  ):
		raise ValueError(ermsg)


	#connect (lower-case) string args to their numerical args
	dic = {}
	for i in range(half):
		dic[str.lower(str(args[ half + i ]))] = int(args[i])



	#charge q

	if length == 4:

		if('c' in dic and 'v' in dic):
			q = dic['c'] * dic['v']
			return q

		if('w' in dic and 'v' in dic):
			q = float(dic['w']) / dic['v']
			return q

		if('u' in dic and 'v' in dic):
			q = (2 * dic['u']) / float(dic['v'])
			return q

		if('t' in dic and 'i' in dic):
			q = dic['t'] * dic['i']
			return q

		raise ValueError('charge() does not support calculation '
				 'based on the combination of ' + args[2] + ' and ' +
				 '' + args[3])


	raise ValueError('Invalid arguments.')
