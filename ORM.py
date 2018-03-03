class categoria:
	def __init__(self,_id,_nombre,_desc,_status):
		self.id=_id
		self.nombre=_nombre
		self.desc=_desc
		self.status=_status
		pass
	def __JSON__(self):
		return "{ \"id\" : "+self.id+"},\n"		+		"\"nombre\":\""+self.nombre+"\",\n"		+		"\"status\":\""+self.status+"\",}"

class cliente:
	pass

class Producto:
	pass

class sucursal:
	pass
class colonia:
    pass
class empresa:
	pass
