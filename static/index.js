

document.addEventListener('DomContentLoaded', function () {

    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
   
    const form = document.querySelector('form');
    form.addEventListener('submit',function(e){
        e.preventDefault()  
    })


    socket.on('connect',()=> {

       
        const chat = document.getElementById('myMessage').value;
     socket.emit('send message', { 'chat': chat });
        });
    

    socket.on('new message', data => {
        const li = document.createElement('li');
        li.innerHTML = `message:${data.chat}`;
        document.querySelector('#msg').append(li);
    });

});


