





     var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
     
     

    
    socket.on('connect',()=> {
    document.getElementById('new_msg').onsubmit=()=>{
        const chat = document.getElementById('myMessage').value; 
         socket.emit('send message', { 'chat': chat });
         
         document.querySelector('#myMessage').value="";
        return false;
        

        };
    
    });
    {socket.on('new message', data => {
        const p = document.createElement('p');
        p.innerHTML = `${data.chat}`;
        document.querySelector('#msg').append(p);
        hr = document.createElement('hr');
        document.querySelector('#msg').append(hr);
    });
};
