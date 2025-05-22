def register_socket_events(socketio):
    @socketio.on('send_message')
    def handle_send_message(data):
        socketio.emit('receive_message', data, broadcast=True)