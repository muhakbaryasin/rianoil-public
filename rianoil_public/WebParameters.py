import datetime
import time

class WebParameters(object):
	def __init__(self):
		self.web_parameters = {
			'trip_type' : None,
			'date_flexibility' : None,
			'departure_city_code' : None,
			'departure_city_name' : None,
			'destination_city_code' : None,
			'destination_city_name' : None,
			'departure_date' : None,
			'return_date' : None,
			'adult_number' :  None,
			'child_number' : None, 
			'infant_number' : None,
		}
	
	def setParameters(self, trip_type, date_flexibility, departure_city_code, departure_city_name, destination_city_code, destination_city_name, departure_date, return_date, adult_number, child_number, infant_number) :
		self.setTripType(trip_type)
		self.setDateFlexibility(date_flexibility)
		self.setDepartureCityCode(departure_city_code)
		self.setDepartureCityName(departure_city_name)
		self.setDestinationCityCode(destination_city_code)
		self.setDestinationCityName(destination_city_name)
		self.setDepartureDate(departure_date)
		self.setReturnDate(return_date)
		self.setAdultNumber(adult_number)
		self.setChildNumber(child_number)
		self.setInfantNumber(infant_number)
	
	def getParameters(self):
		return self.web_parameters
	
	def setTripType(self, trip_type):
		self.web_parameters['trip_type'] = int(trip_type)
		
	def setDateFlexibility(self, date_flexibility):
		self.web_parameters['date_flexibility'] = date_flexibility
		
	def setDepartureCityCode(self, departure_city_code):
		self.web_parameters['departure_city_code'] = departure_city_code.upper()
	
	def setDepartureCityName(self, departure_city_name):
		self.web_parameters['departure_city_name'] = departure_city_name
	
	def setDestinationCityCode(self, destination_city_code):
		self.web_parameters['destination_city_code'] = destination_city_code.upper()
		
	def setDestinationCityName(self, destination_city_name):
		self.web_parameters['destination_city_name'] = destination_city_name
		
	def setDepartureDate(self, departure_date):
		self.web_parameters['departure_date'] = datetime.datetime.strptime(departure_date, '%Y-%m-%d')
		
	def setReturnDate(self, return_date):
		try:
			self.web_parameters['return_date'] = datetime.datetime.strptime(return_date, '%Y-%m-%d')
		except:
			self.web_parameters['return_date'] = datetime.datetime.now()
		
	def setAdultNumber(self, adult_number):
		self.web_parameters['adult_number'] = int(adult_number)
		
	def setChildNumber(self, child_number):
		self.web_parameters['child_number'] = int(child_number)
	
	def setInfantNumber(self, infant_number):
		self.web_parameters['infant_number'] = int(infant_number)
		
	def getTripType(self):
		return self.web_parameters['trip_type']
		
	def getDateFlexibility(self):
		return self.web_parameters['date_flexibility']
		
	def getDepartureCityCode(self):
		return self.web_parameters['departure_city_code']
		
	def getDepartureCityName(self):
		return self.web_parameters['departure_city_name']
		
	def getDestinationCityCode(self):
		return self.web_parameters['destination_city_code']
		
	def getDestinationCityName(self):
		return self.web_parameters['destination_city_name']
		
	def getDepartureDate(self):
		return self.web_parameters['departure_date']
		
	def getReturnDate(self):
		return self.web_parameters['return_date']
		
	def getAdultNumber(self):
		return self.web_parameters['adult_number']
		
	def getChildNumber(self):
		return self.web_parameters['child_number']
	
	def getInfantNumber(self):
		return self.web_parameters['infant_number']
		
	def paramsForLion(self):
		params = {}
		params['trip_type'] = 'one way'
		
		if self.getTripType() > 0:
			params['trip_type'] = 'return'
		
		params['date_flexibility'] = 'fixed'
		params['depart'] = self.getDepartureCityCode()
		params['dest.1'] = self.getDestinationCityCode()
		params['date.0'] = self.getDepartureDate().strftime('%d%b').upper()
		params['date.1'] = self.getReturnDate().strftime('%d%b').upper()
		params['persons.0'] = str(self.getAdultNumber())
		params['persons.1'] = str(self.getChildNumber())
		params['persons.2'] = str(self.getInfantNumber())
		params['origin'] = 'EN'
		params['usercountry'] = 'ID'
		
		return params
	
	def paramsForSriwijaya(self):
		#id - one way
		# OLD website
		"""
		if self.getTripType() == 'oneway':
			self.setTripType('false')
		else: self.setTripType('true')
		params = {
			'isReturn' : self.getTripType(), 'from' : self.getDepartureCityCode(), 'to' : self.getDestinationCityCode(),
			'departDate1' : self.getDepartureDate().strftime('%d'), 'departDate2' : str(int(self.getDepartureDate().strftime('%m')) - 1) + self.getDepartureDate().strftime('-%Y'),
			'returnDate1' : self.getReturnDate().strftime('%d'), 'returnDate2' : str(int(self.getReturnDate().strftime('%m')) - 1) + self.getReturnDate().strftime('-%Y'),			
			'adult' : str(self.getAdultNumber()), 'child' : str(self.getChildNumber()), 'infant' : str(self.getInfantNumber()),
			'returndaterange' : '0', 'Submit' : 'Cari'
		}
		
				roundTrip:NO
				typeAction:search_flight
				TheCheckBox:on
				fromSrc:CGK
				fromSrc2:CGK
				toSrc:DPS
				toSrc2:DPS
				departureDate:01-Apr-2017
				AdultSrc:1
				ChildSrc:0
				InfantSrc:0
				PromoCode:
				departureDate:01-Apr-2017
				returnDate:
		"""

		
		if self.getTripType() == 'oneway':
			self.setTripType('NO')
		else:
			self.setTripType('YES')
		
		params = {
			'roundTrip': self.getTripType(),
			'typeAction': 'search_flight',
			'fromSrc': self.getDepartureCityCode(),
			'fromSrc2': self.getDepartureCityCode(),
			'toSrc' : self.getDestinationCityCode(),
			'toSrc2' : self.getDestinationCityCode(),
			'departureDate' : self.getDepartureDate().strftime('%d-%b-%y'),
			'AdultSrc':str(self.getAdultNumber()),
			'ChildSrc':str(self.getChildNumber()),
			'InfantSrc':str(self.getInfantNumber()),
			'PromoCode': '',
			'returnDate': '',
			
		}
		
		if self.getTripType() == 'YES':
			params['returnDate'] = self.getReturnDate().strftime('%d-%b-%y')
		
		
		print(params)
			
		"""	
		params = {
			'vSub' : 'YES',	'return' : 	self.getTripType(),	'ruteBerangkat'	: self.getDepartureCityCode(),
			'ruteTujuan' : self.getDestinationCityCode(), 'tanggalBerangkat' : self.getDepartureDate().strftime('%d-%b-%y'),
			'ADT' : str(self.getAdultNumber()), 'CHD' : str(self.getChildNumber()), 'INF' : str(self.getInfantNumber()),
			'tanggalTujuan' : self.getReturnDate().strftime('%d-%b-%y'), 'returndaterange' : '0',
		}
		"""
		return params
		
	def paramsForgaruda(self):
			#id - one way
			#import pdb
			#pdb.set_trace()
			if self.getTripType() == 'return':
				self.setTripType('R')
			else:
				self.setTripType('O')
			params = {
				'departure_station' : self.getDepartureCityCode(),
				'arrival_station' : self.getDestinationCityCode(),
				'departure_date' : self.getDepartureDate().strftime('%d-%m-%Y'),
				'departure_date_garuda' : self.getDepartureDate().strftime('%d%b'),
				'arrival_date' : self.getReturnDate().strftime('%d-%m-%Y'),
				'arrival_date_garuda' : self.getReturnDate().strftime('%d%b'),
				'adult' : self.getAdultNumber(),
				'child' : self.getChildNumber(),
				'infant' : self.getInfantNumber(),
				'trip_type' : self.getTripType(),
				
			}
			return params
			
			
	def paramsForgarudaApi(self):
			#id - one way
			if self.getTripType() == 'return':
				self.setTripType('roundtrip')
			else:
				self.setTripType('oneway')
			params = {
				'des' : self.getDestinationCityCode(),
				'ori' : self.getDepartureCityCode(),
				'from_date' :self.getDepartureDate().strftime('%Y-%m-%d'),
				'to_date' : self.getReturnDate().strftime('%Y-%m-%d'),
				'adult' : self.getAdultNumber(),
				'child' : self.getChildNumber(),
				'infant' : self.getInfantNumber(),
				'trip_type' : self.getTripType(),
				
			}
			return params

	def paramsForIataApi(self):
			#id - one way
			if self.getTripType() == 'return':
				self.setTripType('roundtrip')
			else:
				self.setTripType('oneway')
			params = {
				'des' : self.getDestinationCityCode(),
				'ori' : self.getDepartureCityCode(),
				'from_date' :self.getDepartureDate().strftime('%Y-%m-%d'),
				'to_date' : self.getReturnDate().strftime('%Y-%m-%d'),
				'adult' : self.getAdultNumber(),
				'child' : self.getChildNumber(),
				'infant' : self.getInfantNumber(),
				'trip_type' : self.getTripType(),
				
			}
			return params
		
	def paramsForCitilink(self):
		if self.getTripType() == 'oneway':
			self.setTripType('OneWay')
		else: self.setTripType('RoundTrip')		
		params = {
			'pageToken' : '',
			'AvailabilitySearchInputSearchVieworiginStation1' : self.getDepartureCityCode(),
			'AvailabilitySearchInputSearchView$TextBoxMarketOrigin1' : self.getDepartureCityCode(),
			'AvailabilitySearchInputSearchViewdestinationStation1' : self.getDestinationCityCode(),
			'AvailabilitySearchInputSearchView$TextBoxMarketDestination1' : self.getDestinationCityCode(),
			'AvailabilitySearchInputSearchVieworiginStation2' : '',
			'AvailabilitySearchInputSearchView$TextBoxMarketOrigin2' : '',
			'AvailabilitySearchInputSearchView$TextBoxMarketDestination2' : '',
			'AvailabilitySearchInputSearchOnlyView$TextBoxMarketDestination2' : '',
			'AvailabilitySearchInputSearchView$DropDownListMarketDay1' : self.getDepartureDate().strftime('%d'),
			'AvailabilitySearchInputSearchView$DropDownListMarketMonth1': self.getDepartureDate().strftime('%Y-%m'),
			'date_picker' : self.getDepartureDate().strftime('%Y-%m-%d'),
			'AvailabilitySearchInputSearchView$DropDownListMarketDay2' : self.getReturnDate().strftime('%d'),
			'AvailabilitySearchInputSearchView$DropDownListMarketMonth2' : self.getReturnDate().strftime('%Y-%m'),
			'date_picker' : self.getReturnDate().strftime('%Y-%m-%d'),
			'AvailabilitySearchInputSearchView$DropDownListPassengerType_ADT' : str(self.getAdultNumber()),
			'AvailabilitySearchInputSearchView$DropDownListPassengerType_CHD' : str(self.getChildNumber()),
			'AvailabilitySearchInputSearchView$DropDownListPassengerType_INFANT' : str(self.getInfantNumber()),
			'AvailabilitySearchInputSearchView$DdlCurrencyDynamic' : 'IDR',
			'AvailabilitySearchInputSearchView$RadioButtonMarketStructure' : self.getTripType(),
			'AvailabilitySearchInputSearchView$DropDownListSearchBy' : 'columnView',
			'AvailabilitySearchInputSearchView$ButtonSubmit' : 'Find Flights',
			'from_date' : self.getDepartureDate().strftime('%Y-%m-%d'),
			'to_date' : self.getReturnDate().strftime('%Y-%m-%d')
		}
		return params
		
		
	def paramsForKalstar(self):
		#id - one way
		if self.getTripType() == 'oneway':
			self.setTripType('0')
		else: self.setTripType('1')
		params = {
			'action' : "GET_FLIGHT",
			'org' : self.getDepartureCityCode(),
			'des' : self.getDestinationCityCode(),
			'dep_date' : self.getDepartureDate().strftime('%Y%m%d'),
			'ret_date' : self.getReturnDate().strftime('%Y%m%d'),
			"class": 'Y',
			'pax_adult' : self.getAdultNumber(),
			'pax_child' : self.getChildNumber(),
			'pax_infant' : self.getInfantNumber(),
			'return_flight' : self.getTripType(),
			'server_id' : 'Dd6MPkHdh9-1438077321-43',
		}
		return params
	
	def paramsForAviastar(self):
		#id - one way
		if self.getTripType() == 'return':
			self.setTripType('1')
		else:
			self.setTripType('0')
		params = {
			'action' : "GET_FLIGHT",
			'org' : self.getDepartureCityCode(),
			'des' : self.getDestinationCityCode(),
			'dep_date' : self.getDepartureDate().strftime('%Y%m%d'),
			'ret_date' : self.getReturnDate().strftime('%Y%m%d'),
			"class": 'Y',
			'pax_adult' : self.getAdultNumber(),
			'pax_child' : self.getChildNumber(),
			'pax_infant' : self.getInfantNumber(),
			'return_flight' : self.getTripType(),
			
		}
		return params
	
	def paramsForAirAsia(self):
		"""
		if self.getTripType() == 'oneway':
			self.setTripType('OneWay')
		else: self.setTripType('RoundTrip')
		
		params = {
			'pageToken' : '',
			'MemberLoginSearchView$HFTimeZone' : '420',
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$RadioButtonMarketStructure' : self.getTripType(),
			'oneWayOnly' : '1',
			'ControlGroupSearchView_AvailabilitySearchInputSearchVieworiginStation1' : self.getDepartureCityCode(),
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$TextBoxMarketOrigin1' : self.getDepartureCityCode(),
			'ControlGroupSearchView_AvailabilitySearchInputSearchViewdestinationStation1' : self.getDestinationCityCode(),
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$TextBoxMarketDestination1' : self.getDestinationCityCode(),
			'ControlGroupSearchView$MultiCurrencyConversionViewSearchView$DropDownListCurrency' : 'default',
			'date_picker' : self.getDepartureDate().strftime('%m/%d/%Y'),
			'date_picker' : '',
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$DropDownListMarketDay1' : self.getDepartureDate().strftime('%d').lstrip('0'),
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$DropDownListMarketMonth1' : self.getDepartureDate().strftime('%Y-%m'),
			'date_picker' : self.getReturnDate().strftime('%m/%d/%Y'),
			'date_picker' : '',
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$DropDownListMarketDay2' : self.getReturnDate().strftime('%d').lstrip('0'),
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$DropDownListMarketMonth2' : self.getReturnDate().strftime('%Y-%m'),
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$DropDownListPassengerType_ADT' : str(self.getAdultNumber()),
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$DropDownListPassengerType_CHD' : str(self.getChildNumber()),
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$DropDownListPassengerType_INFANT' : str(self.getInfantNumber()),
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$DropDownListSearchBy' : 'columnView',
			'ControlGroupSearchView$ButtonSubmit' : 'Search'
		}
		"""
		
		
		params = {
			'o1' : self.getDepartureCityCode(),
			'd1' : self.getDestinationCityCode(),
			'dd1' : self.getDepartureDate().strftime('%Y-%m-%d'),
			'ADT' : str(self.getAdultNumber()),
			'CHD' : str(self.getChildNumber()),
			'inl' : str(self.getInfantNumber()),
			's' : 'true',
			'mon' : 'true',
			'cc' : 'IDR'
		}
		
		if self.getTripType() == 'oneway':
			self.setTripType('false')
		else:
			self.setTripType('true')
			params['dd2'] = self.getReturnDate().strftime('%Y-%m-%d')
			params['r'] = self.getTripType()

		return params
		
		
	def paramsForTigerAir(self):
		params = {
			'pageToken' : '',
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$RadioButtonMarketStructure' : 'OneWay',
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$HiddenFieldExternalRateId' : '',
			'ControlGroupSearchView_AvailabilitySearchInputSearchVieworiginStation1' : self.getDepartureCityCode(),
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$TextBoxMarketOrigin1' : self.getDepartureCityCode(),
			'ControlGroupSearchView_AvailabilitySearchInputSearchViewdestinationStation1' : self.getDestinationCityCode(),
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$TextBoxMarketDestination1' : self.getDestinationCityCode(),
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$DropDownListMarketDay1' : self.getDepartureDate().strftime('%d').lstrip('0'),
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$DropDownListMarketMonth1' : self.getDepartureDate().strftime('%Y-%m'),
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$DropDownListMarketDateRange1' : '1|1',
			'date_picker' : self.getDepartureDate().strftime('%Y-%m-%d'),
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$HiddenFieldExternalRateId' : '',
			'ControlGroupSearchView_AvailabilitySearchInputSearchVieworiginStation2' : '',
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$TextBoxMarketOrigin2' : '',
			'ControlGroupSearchView_AvailabilitySearchInputSearchViewdestinationStation2': '',
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$DropDownListMarketDay2' : self.getDepartureDate().strftime('%d').lstrip('0'),
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$DropDownListMarketMonth2' : self.getDepartureDate().strftime('%Y-%m'),
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$DropDownListMarketDateRange2' : '1|1',
			'date_picker' : self.getDepartureDate().strftime('%Y-%m-%d'),
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$DropDownListPassengerType_ADT' : self.getAdultNumber(),
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$DropDownListPassengerType_CHD' : self.getChildNumber(),
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$DropDownListPassengerType_INFANT' : self.getInfantNumber(),
			'hiddendAdultSelection' : self.getAdultNumber(),
			'hiddendChildSelection': self.getChildNumber(),
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$HIDDENPROMOCODE' : '',
			'ControlGroupSearchView$AvailabilitySearchInputSearchView$DropDownListMCCCurrency' : 'default',
			'ControlGroupSearchView$ButtonSubmit': 'get flights'
		}
		return params
		
	def paramsForExpress(self):
		
		if self.getTripType() == 'oneway':
			self.setTripType('1')
		else:
			self.setTripType('0')
			
			
		params = {
			'__VIEWSTATEGENERATOR' : '16C1DB0E',
			'ctl00$ScriptManager1' : '',
			'ctl00$ContentPlaceHolder1$hfOutboundFlight' : '',
			'ctl00$ContentPlaceHolder1$hfHomeboundFlight' : '',
			'ctl00$ContentPlaceHolder1$hfOutboundClass' : '3',
			'ctl00$ContentPlaceHolder1$hfHomeboundClass' : '',
			'ctl00$ContentPlaceHolder1$hfOutboundETA' : '',
			'ctl00$ContentPlaceHolder1$hfHomeboundETD' : '',
			'ctl00$ContentPlaceHolder1$hfOutboundDate' : '',
			'ctl00$ContentPlaceHolder1$hfHomeboundDate' : '',
			'ctl00$ContentPlaceHolder1$hfOutboundRebookRule' : '',
			'ctl00$ContentPlaceHolder1$hfHomeboundRebookRule' : '',
			'ctl00$ContentPlaceHolder1$hfOutboundLowestCommonClass' : '0',
			'ctl00$ContentPlaceHolder1$hfHomeboundLowestCommonClass' : '',
			'HoursFromGMT' :'7',
			'MinutesFromGMT' :'1',
			'TotalFareCopy' : '',
			'ctl00$ContentPlaceHolder1$hfOrigin' : self.getDepartureCityName() + ' ' + self.getDepartureCityCode(),
			'ctl00$ContentPlaceHolder1$HfDestination' : self.getDestinationCityName() + ' ' + self.getDestinationCityCode(),
			'rblDirection' : self.getTripType(),
			'ctl00$ContentPlaceHolder1$Curr' : 'IDR',
			'OutboundDate' : self.getDepartureDate().strftime('%d/%m/%Y'),
			'HomeboundDate' : self.getReturnDate().strftime('%d/%m/%Y'),
			'ctl00$ContentPlaceHolder1$Adults' : str(self.getAdultNumber()), 
			'ctl00$ContentPlaceHolder1$Children' : str(self.getChildNumber()),
			'ctl00$ContentPlaceHolder1$Infants' : str(self.getInfantNumber()),
			'ctl00$ContentPlaceHolder1$Voucher' : '',
			'ctl00$ContentPlaceHolder1$VoucherPINCode' : '',
			'ctl00$ContentPlaceHolder1$search' : 'CARI',
	
		}
		
		return params

