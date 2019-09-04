

document.addEventListener('DomContentLoaded', ()=> {



    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
   
    
    socket.on('connect',()=> {
    document.getElementById('new_msg').onsubmit=()=>{
        const chat = document.getElementById('myMessage').value;
     socket.emit('send message', { 'chat': chat });
     return false;
        };
    
    });
    socket.on('new message', data => {
        const li = document.createElement('li');
        li.innerHTML = `message:${data.chat}`;
        document.querySelector('#msg').append(li);
    });

});


