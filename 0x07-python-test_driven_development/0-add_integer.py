<<<<<<< HEAD
def add_integer(a, b=98):
    if not isinstance (a, (int, float)):
	    raise TypeError("a must be an integer")
    elif not isinstance (b, (int, float)):
	    raise TypeError("b must be an integer")
    return (int(a) + int(b))
=======
#!/usr/bin/python3
def add_integer(a, b=98):

	if not isinstance (a, (int, float)):
			raise TypeError("a must be an integer")
	elif not isinstance (b, (int, float)):
			raise TypeError("b must be an integer")
	return (int(a) + int(b))

>>>>>>> c9bc5cb54d3ac1ab326cd635121e84390bf0f761
