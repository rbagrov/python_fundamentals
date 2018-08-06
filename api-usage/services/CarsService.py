# -*- coding: utf-8 -*-

import requests


class CarsService(object):
    base_endpoint_url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas'
    cars_models_url = base_endpoint_url + '/{}/modelos'
    cars_models_years_url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas/{}/modelos/{}/anos'

    def get_service_status(self):
        service_response = requests.get(CarsService.base_endpoint_url)

        return service_response.status_code

    def get_car_makes(self):
        result = []
        service_response = requests.get(CarsService.base_endpoint_url,
                                        headers={'content-type': 'application/json'})
        service_response.encoding = 'utf-8'
        if service_response.status_code == requests.codes.ok:
            result = service_response.json()
        return result
    
    def get_car_models(self, make_id):
        result = []
        service_response = requests.get(CarsService.cars_models_url.format(make_id),
                                        headers={'content-type': 'application/json'})
        service_response.encoding = 'utf-8'
        if service_response.status_code == requests.codes.ok:
            result = service_response.json()            
        return result

    def get_car_models_years(self, make_id, model_id):
        result = []
        service_response = requests.get(CarsService.cars_models_years_url.format(make_id, model_id),
                                        headers={'content-type': 'application/json'})
        service_response.encoding = 'utf-8'
        if service_response.status_code == requests.codes.ok:
            result = service_response.json()            
        return result
