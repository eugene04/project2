

document.addEventListener('DomContentLoaded', function () {

    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    const chat = document.getElementById('myMessage').value;
    const form = document.querySelector('form');


    socket.on('connect', function () {


        form.addEventListener('submit', function (e) {
            e.preventDefault()

            socket.emit('send message', { 'chat': chat });
        });
    });

    socket.on('new message', data => {
        const li = document.createElement('li');
        li.innerHTML = `message:${data.chat}`;
        document.querySelector('#msg').append(li);
    });

});



