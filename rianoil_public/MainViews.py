from pyramid.view import view_config
from .MainController import MainController
from .ErrorCodeController import ErrorCodeController
from .WebParameters import WebParameters
from pyquery import PyQuery as pq

from .Scrapper import Scrapper, urlencode
import  base64

import logging
log = logging.getLogger(__name__)

class MainViews(object):
    def __init__(self, request):
        self.request = request
        self.reqon = MainController( request )

    @view_config(route_name='home', renderer='templates/mytemplate.jinja2')
    def my_view(self):
        return {'project': 'rianoil-public'}

    @view_config(route_name='lion-search', renderer='jsonp')
    def lion_search(self):
        try:
            self.reqon.checkComplete(self.reqon.REQ_IGNITE_SEARCH)

            scrapper = Scrapper()
            url = 'https://secure2.lionair.co.id/lionairibe2/OnlineBooking.aspx'
            response_data = scrapper.requestData(url=url, file_log_name="lion1.html")

            web_parameters = WebParameters()
            web_parameters.setDepartureCityCode(self.request.params['departure_city_code'])
            web_parameters.setDestinationCityCode(self.request.params['destination_city_code'])
            web_parameters.setDepartureDate(self.request.params['departure_date'])
            web_parameters.setReturnDate(self.request.params['return_date'])
            web_parameters.setTripType(self.request.params['round_trip'])
            web_parameters.setAdultNumber(self.request.params['adult_count'])
            web_parameters.setChildNumber(self.request.params['child_count'])
            web_parameters.setInfantNumber(self.request.params['infant_count'])
            
            values = web_parameters.paramsForLion()
            urlref = url + '?{}'.format(urlencode(values))
            response_data = scrapper.requestData(referer = urlref, url = urlref, file_log_name="lion2.html")

            response_data = scrapper.requestData(referer = urlref, url = url, file_log_name="lion3.html")
            
            if response_data is None or response_data == b'':
                raise Exception('Result is None')
            
            result_html = ''
            
            for per_content in pq(response_data)('.content')('.flight-matrix-container'):
                result_html += pq(per_content).html()

            result = base64.b64encode(result_html.encode()).decode()
            return {'code' : 'OK', 'message' : 'result is base64 encoded', 'content' : result}

        except Exception as e:
            log.exception('Error ignite_search')
            
            err_conf = ErrorCodeController( exception = e )
            err_code_no = err_conf.getErrorCodeNo()
            err_code_status = err_conf.getErrorStatus()
            message_to_end_user = err_conf.getMessage2EndUser()
            
            if message_to_end_user is None:
                message_to_end_user = 'Gagal ignite_search. Kode {}'.format(err_code_no)
            
            return {'status' : err_code_status, 'message' : message_to_end_user, 'content' : None}



