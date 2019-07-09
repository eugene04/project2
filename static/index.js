const form = document.querySelector('form')
const msg = document.getElementById('msg')
var socket=io.connect(location.protocol+'//'+document.domain+':'+location.port)

    socket.on('connect', ()=> {msg.onsubmit=()=>
        {
            socket.emit(new_message,data)
        }})


    
