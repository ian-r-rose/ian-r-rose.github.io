import sympy
from fractions import Fraction

class Parameter( object ):
    def __init__(self, symbol, units):
        self.units = units
        self.symbol = symbol

def construct_dimension_matrix( parameters ):
    units = set()
    for p in parameters:
        for key in p.units:
            units.add(key)

    units =list(units)
    units.sort()

    dimension_matrix = sympy.zeros( len(units), len(parameters) )
    
    for i,u in enumerate(units):
        for j,p in enumerate(parameters):
            entry = p.units[u] if u in p.units else 0. 
            dimension_matrix[i,j] = entry

    return units, dimension_matrix

def integrify_basis( basis ):
    def _gcd(a, b):
	"""Return greatest common divisor using Euclid's Algorithm."""
	while b:
	    a, b = b, a % b
	return a

    def _lcm(a, b):
	"""Return lowest common multiple."""
	return a * b // _gcd(a, b)

    def _lcmm(*args):
	"""Return lcm of args."""   
	return reduce(_lcm, args)

    new_basis = []
    for vec in basis:
        #Make a list of the denominators
        denominators = [sympy.fraction(e)[1] for e in vec]
        #Find the least common multiple
        least_common_multiple = _lcmm( *denominators )
        #Multiply all the entries by that, make it a python Fraction object
        new_vec = [ Fraction( int(e*least_common_multiple), 1 ) for e in vec]
        new_basis.append(new_vec)

    return new_basis

def parse_nondimensional_number( parameters, nondim ):
    numerator_values = ''
    denominator_values = ''

    for p,n in zip(parameters,nondim):
        if n == 0:
            continue #Do nothing if the parameter is not present in this number

        #If the exponent is one, we do not need to write it
        if n == 1 or n == -1:
            parsed_parameter = p.symbol
        #If the exponent is a whole number, we do not need to represent it as a fraction
        elif n.denominator == 1 or n.denominator == -1:
            parsed_parameter = p.symbol + '^{%i}'%(abs(n.numerator))
        #Otherwise, represent it as a fraction
        else:
            parsed_parameter = p.symbol + '^{%i/%i}'%(abs(n.numerator), abs(n.denominator))
        
        if n > 0: # The exponent is positive, put it in the numerator
            numerator_values = ' '.join( [numerator_values, parsed_parameter] )
        elif n < 0: #The exponent is negative, put it in the denominator
            denominator_values = ' '.join( [denominator_values,parsed_parameter])

    #If nothing is in the numerator, make it a one
    if numerator_values == '':
        parsed_number = '\\frac{1}{'+denominator_values+'}'
    #If nothing is in the denominator, no need to make it a fraction
    elif denominator_values == '':
        parsed_number = numerator_values
    #Otherwise, make a fraction of the numerator and denominator
    else:
        parsed_number = '\\frac{' + numerator_values + '}{'+denominator_values+'}'

    return parsed_number

def find_nondimensional_numbers( parameters ):
    units, dimension_matrix = construct_dimension_matrix( parameters )

    nullspace = dimension_matrix.nullspace()
    integrified_nullspace = integrify_basis( nullspace )
    nondimensional_basis = integrified_nullspace #Rename

    nondimensional_numbers = []
    for nondim in nondimensional_basis:
        nondimensional_numbers.append( parse_nondimensional_number( parameters, nondim ) )

    return nondimensional_numbers

velocity = Parameter('u', {'m' :  1,\
                           's' : -1})

density = Parameter(u'\\rho', {'kg' :  1,\
                               'm'  : -3} )

length = Parameter('L', {'m' : 1} )

viscosity = Parameter( '\\eta', {'kg' :  1,\
                                 'm'  : -1,\
                                 's'  : -1} )


parameters = [velocity, density, length, viscosity]

nondimensional_numbers = find_nondimensional_numbers(parameters)
for n in nondimensional_numbers:
  print n
