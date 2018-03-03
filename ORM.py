class categoria:
	def __init__(self,_id,_nombre,_desc,_status):
		self.id = _id
		self.nombre = _nombre
		self.desc = _desc
		self.status = _status
	def __JSON__(self):
<<<<<<< HEAD
		return "{ \"id\" : "+self.id+"},\n"+"\"nombre\":\""+self.nombre+"\",\n"+"\"status\":\""+self.desc+"\",\n"+ "\"status\":\""+self.status+"\"\n}"

class administrador:
	def __init__ (self,_id,_id_sucursal,_correo,_status,_nombre,_password,_telefono):
		self.id=_id
		self.id_sucursal=_id_sucursal
		self.correo=_correo
		self.status=_status
		self.nombre=_nombre
		self.password=_password
		self.telefono=_telefono
		pass
	def __JSON__(self):
		return "{ \"id\" : "+self.id+"},\n"+"{\"id_sucursal\":\""+self.id_sucursal+"},\n"+"\"correo\":\""+self.correo+"\",\n"+ "\"status\":\""+self.status+"\",\n"+ "\"nombre\":\""+self.nombre+"\",\n"+ "\"password\":\""+self.password+"\",\n" + "\"telefono\":\""+self.telefono+"\"\n}"
		

class ciudad:
	def __init__ (self,_id_ciudad,_id_estado,_ciudad,_codigo_ciudad,_estatus):
		self.id_ciudad=_id_ciudad
		self.id_estado=_id_estado
		self.ciudad=_ciudad
		self.estatus=_estatus
		pass
	def __JSON__ (self):
		return "{ \"id_ciudad\" : "+self.id_ciudad+"},\n"+"{\"id_estado\":\""+self.id_estado+"},\n"+"\"ciudad\":\""+self.ciudad+"\",\n"+ "\"status\":\""+self.status+"\"\n}"
		

class clasificacion:
	def __init__ (self,_id_categoria,_id_producto):
		self.id_categoria=_id_categoria
		self.id_producto=_id_producto
		pass
	def __JSON__ (self):
		return "{ \"id_categoria\" : "+self.id_categoria+"},\n"+"{\"id_producto\":\""+self.id_producto+"},\n"
	
=======
		return "{ \"id\" : " + self.id + "},\n" + "\"nombre\":\"" + self.nombre + "\",\n" + "\"status\":\"" + self.status + "\",}"
>>>>>>> c41958fded96d4033741f90a4c0859996d790454

class cliente:
	def __init__ (self,_id_cliente,_apellido1,_apellido2,_correo,_estatus,_nombre,_password,_telefono,_direcciones):
		self.id_cliente=_id_cliente
		self.apellido1=_apellido1
		self.apellido2=_apellido2
		self.correo=_correo
		self.estatus=_estatus
		self.nombre=_nombre
		self.password=_password
		self.telefono=_telefono
		self.direcciones=_direcciones
		pass
	def __JSON__ (self):
		return "{ \"id_cliente\" : "+self.id_cliente+"},\n"+"\"apellido1\":\""+self.apellido1",\n"+"\"apellido2\":\""+self.apellido2+"\",\n"+ "\"correo\":\""+self.correo+"\",\n"+ "\"estatus\":\""+self.estatus+"\",\n"+ "\"nombre\":\""+self.nombre+"\",\n"+ "\"password\":\""+self.password+"\",\n"+ "\"telefono\":\""+self.telefono+"\",\n"+ "\"direcciones\":\""+self.direcciones+"\"\n}"

class clientes_bloqueados:
	def __init__ (self,_id_cliente,_id_empresa,_fecha,_motivo):
		self.id_cliente=_id_cliente
		self.id_empresa=_id_empresa
		self.fecha=_fecha
		self.motivo=_motivo
		pass
	def __JSON__ (self):
		return "{ \"id_cliente\" : "+self.id_cliente+"},\n"+"{\"id_empresa\":\""+self.id_empresa+"},\n"+"\"fecha\":\""+self.fecha"\",\n" + "\"motivo\":\""+self.motivo"\"\n}"

class codigo_postal:
	def __init__ (self,_codigo_postal,_id_cp,_estatus):
		self.codigo_postal=_codigo_postal
		self.id_cp=_id_cp
		self.estatus=_estatus
		pass
	def __JSON__ (self):
		return "{ \"id_cp\" : "+self.id_cp+"},\n"+"\"codigo_postal\":\""+self.codigo_postal"\",\n"+"\"estatus\":\""+self.estatus"\"\n}"
	
class colonia:
	def __init__ (self,_id_colonia,_id_cp,_id_estado,_colonia,_estatus):
		self.id_colonia=_id_colonia
		self.id_cp=_id_cp
		self.id_estado=_id_estado
		self.colonia=_colonia
		self.estatus=_estatus
		pass
	def __JSON__ (self):
		return "{ \"id_colonia\" : "+self.id_colonia+"},\n"+"{\"id_cp\":\""+self.id_cp+"},\n"+"{\"id_estado\":\""+self.id_estado+"},\n"+
		"\"colonia\":\""+self.colonia"\",\n" + "\"estatus\":\""+self.estatus"\"\n}"
	
	
class direccion_cliente:
	def __init__ (self,_id_ciudad,_id_cliente,_id_cp,_id_colonia,_id_direccion,_id_estado,_id_pais,_estatus,_nombre,_numero,_calle):
		self.id_ciudad=_id_ciudad
		self.id_cliente=_id_cliente
		self.id_cp=_id_cp
		self.id_colonia=_id_colonia
		self.id_direccion=_id_direccion
		self.id_estado=_id_estado
		self.id_pais=_id_pais
		self.estatus=_estatus
		self.nombre=_nombre
		self.numero=_numero
		self.calle=_calle
		pass
	def __JSON__ (self):
		return "{ \"id_ciudad\" : "+self.id_ciudad+"},\n"+"{\"id_cliente\":\""+self.id_cliente+"},\n"+"{\"id_cp\":\""+self.id_cp+"},\n"+
		"{\"id_colonia\":\""+self.id_colonia+"},\n"+"{\"id_direccion\":\""+self.id_direccion+"},\n"+"{\"id_estado\":\""+self.id_estado+"},\n"+
		"{\"id_pais\":\""+self.id_pais+"},\n"+"\"estatus\":\""+self.estatus"\",\n"+"\"nombre\":\""+self.nombre"\",\n"+
		"\"numero\":\""+self.numero"\",\n"+"\"calle\":\""+self.calle"\"\n}"

class empresa:
	def __init__ (self,_id_empresa,_id_giro,_estatus,_nombre_comercial,_razon_social):
		self.id_empresa=_id_empresa
		self.id_giro=_id_giro
		self.estatus=_estatus
		self.nombre_comercial=_nombre_comercial
		self.razon_social=_razon_social
		pass
	def __JSON__ (self):
		return "{ \"id_empresa\" : "+self.id_empresa+"},\n"+"{\"id_giro\":\""+self.id_giro+"},\n"+"\"estatus\":\""+self.estatus"\",\n"+
		"\"nombre_comercial\":\""+self.nombre_comercial"\",\n"+"\"razon_social\":\""+self.razon_social"\"\n}"

class estado:
	def __init__ (self,_id_estado,_id_pais,_codigo_estado,_estado,_estatus):
		self.id_estado=_id_estado
		self.id_pais=_id_pais
		self.codigo_estado=_codigo_estado
		self.estado=_estado
		self.estatus=_estatus
		pass
	def __JSON__ (self):
		return "{ \"id_estado\" : "+self.id_estado+"},\n"+"{\"id_pais\":\""+self.id_pais+"},\n"+"\"codigo_estado\":\""+self.codigo_estado"\",\n"+
		"\"estado\":\""+self.estado"\",\n"+"\"estatus\":\""+self.estatus"\"\n}"

class giro:
	def __init__ (self,_id_giro,_descripcion,_estatus,_giro):
		self.id_giro=_id_giro
		self.descripcion=_descripcion
		self.estatus=_estatus
		self.giro=_giro
		pass
	def __JSON__ (self):
		return "{ \"id_giro\" : "+self.id_giro+"},\n"+"\"descripcion\":\""+self.descripcion"\",\n"+"\"estatus\":\""+self.estatus"\",\n"+
		"\"giro\":\""+self.giro"\"\n}"
	

class marca:
	def __init__ (self,_id_marca,_descripcion,_estatus,_marca):
		self.id_marca=_id_marca
		self.descripcion=_descripcion
		self.estatus=_estatus
		self.marca=_marca
		pass
	def __JSON__ (self):
		return "{ \"id_marca\" : "+self.id_marca+"},\n"+"\"descripcion\":\""+self.descripcion"\",\n"+"\"estatus\":\""+self.estatus"\",\n"+
		"\"marca\":\""+self.marca"\"\n}"
	

class mensaje:
	def __init__ (self,_id_cliente,_id_mensaje,_id_sucursal,_fecha,_leido_cliente,_leido_empresa,_mensaje):
		self.id_cliente=_id_cliente
		self.id_mensaje=_id_mensaje
		self.id_sucursal=_id_sucursal
		self.fecha=_fecha
		self.leido_cliente=_leido_cliente
		self.leido_empresa=_leido_empresa
		self.mensaje=_mensaje
		pass
	def __JSON__ (self):
		return "{ \"id_cliente\" : "+self.id_cliente+"},\n"+"{\"id_mensaje\":\""+self.id_mensaje+"},\n"+
		"{\"id_sucursal\":\""+self.id_sucursal+"},\n"+"\"fecha\":\""+self.fecha"\",\n"+"\"leido_cliente\":\""+self.leido_cliente"\",\n"+
		"\"leido_empresa\":\""+self.leido_empresa"\",\n"+"\"mensaje\":\""+self.mensaje"\"\n}"


class pais:
	pass

class paypal:
	pass

class pedido:
	pass

class pedido_detalle:
	pass

class producto:
	pass

class repartidor:
	pass

class sucursal:
	pass
<<<<<<< HEAD

class tipo_entrega:
	pass

class tipo_pago:
=======
class colonia:
    pass
class empresa:
	pass

class ciudad:
>>>>>>> c41958fded96d4033741f90a4c0859996d790454
	pass
