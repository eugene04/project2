

document.addEventListener('DomContentLoaded',()=>{
const form = document.querySelector('form');


var socket=io.connect(location.protocol+'//'+document.domain+':'+location.port)


    socket.on('connect', ()=> {
        form.addEventListener('submit', function(e) {
            e.preventDefault()
         let chat = document.getElementById('myMessage').value;
            socket.emit('send message',{'chat':chat});
        });
    });
socket.on('new message',data=>{
    const li = document.createElement('li');
    li.innerHTML = `message:${data.chat}`;
    document.querySelector('#myMessage').append(li)
});
    });