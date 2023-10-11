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
                datetime.strptime(payload_data['received_timestamp'], '%Y-%m-%d %H:%M:%S.%f')
        except ValueError:
            return {'message': f'Invalid date format used for {timestamp_field}. Expected format: %Y-%m-%d %H:%M:%S.%f'}, 400

        if isinstance(payload_data.get('component'), str):
            if len(payload_data.get('component')) > 140:
                return {'message': 'Component too big. Max 140 chars'}, 400
        else:
            return {'message': 'Component not a string'}, 400

        return None

    def get(self, transition_id=None):
        if transition_id:
            transition = TransitionModel.query.get(transition_id)
            if transition:
                return transition.json(), 200
            else:
                return {'message': 'Transition not found'}, 404
        return {'Status': 'HEALTH OK'}, 200


    def post(self):
        payload = Transitions.parser.parse_args()
        validation = self._validate_payload(payload_data=payload)
        if validation:
            return validation
        try:
            transition = TransitionModel(**payload)
            transition.save()
            return {'Status': f'POST for transition id: {transition.id} Successful.'}, 200
        except Exception as e:
            return {'message': f'An error occurred while saving the transition. Error: {str(e)}'}, 500
