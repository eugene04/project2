const form = document.querySelector('form')
const msg = document.getElementById('msg')
var socket=io.connect(location.protocol+'//'+document.domain+':'+location.port)

    socket.on('connect', ()=> {
        socket.emit('new_message',)
    });
    form.addEventListener('submit', function(e) {
        e.preventDefault()
    
      })