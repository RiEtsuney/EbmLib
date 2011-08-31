#---------------------------------------#
#	This file is part of EbmLib.
#
#	EbmLib is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	EbmLib is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with EbmLib.  If not, see <http://www.gnu.org/licenses/>.
#---------------------------------------#
# author:
#	tllake 
# email:
#	<thomas.l.lake@wmich.edu>
#	<thom.l.lake@gmail.com>
# date:
#	2011.08.30
# file:
#	units.py
# description:
#	Several common activation functions used for energy based models.
#	The derivatives of these functions given their output.
#---------------------------------------#

import numpy

#--- ACTIVATION FUNCTIONS ---#
def pthresh(x):
	"""probabilistic step funtion of x

	:param x: input
	:type x: numpy.array
	:returns: 1 if x_i >= ~ U(0,1) else 0 for x_i \in x
	:rtype: numpy.array
	"""
	return numpy.array(sigmoid(x) >= numpy.random.random(x.shape), dtype = numpy.float32)

def sigmoid(x):
	"""logisitc sigmoid function of x

	:param x: input
	:type x: numpy.array
	:returns: 1 / (1 + e^(-x))
	:rtype: numpy.array
	"""
	return 1./(1.+numpy.exp(-x))

def tanh(x):
	"""hyperbolic tangent of x

	:param x: input
	:type x: numpy.array
	:returns: tanh(x)
	:rtype: numpy.array
	"""
	return numpy.tanh(a)

def rectlinear(x):
	"""rectified linear function of x

	:param x: input
	:type x: numpy.array
	:returns: max[0, x + ~ N(0, 1 / (1 + (e^(-x))))]
	:rtype: numpy.array
	"""
	return numpy.maximum(0., x + numpy.random.normal(0., sigmoid(x)+0.00001, a.shape))

def linear(x):
	"""identity function

	:param x: input
	:type x: numpy.array
	:returns: x
	:rtype: numpy.array
	"""
	return a

#--- DERIVATIVES ---#
def dsigmoid(y):
	"""derivative of sigmoid

	:param y: output of sigmoid
	:type y: numpy.array
	:returns: y * (1 - y)
	:rtype: numpy.array
	"""
	return y * (1 - y)

def dtanh(y):
	"""derivative of tanh

	:param y: output of tanh
	:type y: numpy.array
	:returns: 1 - y^2
	:rtype: numpy.array
	"""
	return 1 - y**2

def dlinear(y):
	"""derivative of identity

	:param y: output of identity
	:type y: numpy.array
	:returns: 1
	:rtype: float
	"""
	return 1.

def drectlinear(y):
	"""derivative of rectified linear

	:param y: output of rectified linear
	:type y: numpy.array
	:returns: 1 if y_i > 0 else 0 for y_i \in y
	:rtype: numpy.array
	"""
	return numpy.array(y > 0, dtype = numpy.float32)

# get function given the function name
unittypes = {
	'pthresh' : pthresh,
	'sigmoid': sigmoid,
	'tanh': numpy.tanh,
	'rectlinear': rectlinear,
	'linear': linear}

# get the deirvative of a function given the name
derivatives = {
	'sigmoid': dsigmoid,
	'tanh': dtanh,
	'rectlinear': drectlinear,
	'linear': dlinear}
