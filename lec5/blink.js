txt = document.querySelector('h1');
function blink() {
    if(txt.style.visibility == 'hidden'){
        txt.style.visibility = 'visible';
    }else{
        txt.style.visibility = 'hidden';
    }
    
}

document.addEventListener('DOMContentLoaded',() => {
    setInterval( blink, 100)
})