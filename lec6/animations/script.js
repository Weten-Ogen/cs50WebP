const btn = document.querySelector('button'),
h1 = document.querySelector('h1');

document.addEventListener('DOMContentLoaded',function() {
    h1.style.animationPlayState = 'paused';
    btn.onclick = () => {
        if (!(h1.style.animationPlayState == 'running')){
            h1.style.animationPlayState = 'running';
        }else{
            h1.style.animationPlayState = 'paused';
        }
        
    }
    
})