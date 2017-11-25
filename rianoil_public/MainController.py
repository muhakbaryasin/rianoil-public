from .RequestController import RequestController

class MainController(RequestController):
	
	def __init__(self, request):
		RequestController.__init__(self, request)
		
		# Add your request controller tuple under this code
		self.REQ_IGNITE_SEARCH = ( ('departure_date', self.ISODATE), ('return_date', self.ISODATE) , \
			('round_trip', self.BOOLEAN), ('departure_city_code', self.CITY_CODE), \
			('destination_city_code', self.CITY_CODE), ('adult_count', self.NUMERIC), ('child_count', self.NUMERIC), \
			('infant_count', self.NUMERIC) )
		
	
