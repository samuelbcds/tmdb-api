from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

@api.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'TMDB App API'}), 200

@api.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@api.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Internal error'}), 500