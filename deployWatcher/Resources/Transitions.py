from deployWatcher.Models.TransitionsModel import TransitionModel
from flask_restful import Resource, reqparse
from datetime import datetime

 
class Transitions(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('component', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('version', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('author', type=str, required=True, help="This field cannot be left blank!")
    parser.add_argument('status', type=str, required=True, help="This field cannot be left blank!")

    @staticmethod
    def _validate_payload(payload_data):
        timestamp_field = ""
        try:
            timestamp_field = "sent_timestamp"
            if payload_data.get('sent_timestamp') is not None:
                datetime.strptime(payload_data['sent_timestamp'], '%Y-%m-%d %H:%M:%S.%f')
            timestamp_field = "received_timestamp"
            if payload_data.get('received_timestamp') is not None:
                datetime.strptime(payload_data['sent_timestamp'], '%Y-%m-%d %H:%M:%S.%f')
        except ValueError:
            return {'message': f'Invalid date format used for {timestamp_field}. Expected format: %Y-%m-%d %H:%M:%S.%f'}, 500

        if isinstance(payload_data.get('component'), str):
            if len(payload_data.get('component')) > 140:
                return {'message': 'Component too big. Max 140 chars'}, 500
        else:
            return {'message': 'Component not a string'}, 500

        return 0

    def get(self):
       return {'Status': 'GET for transitions Succesful.'}, 200 

    def post(self):
        payload = Transitions.parser.parse_args()
        validation = self._validate_payload(payload_data=payload)
        if validation != 0:
            return validation
        transition = TransitionModel(**payload)
        transition.save()

        return {'Status': 'POST for transition id: {} Succesful.'.format(transition.id)}, 200
