const btn = document.querySelector('button');
 if(!localStorage.getItem('count')){
    localStorage.setItem('count', 0);
 }

function counter(){
    let counted = localStorage.getItem('count');
    counted++;
    document.querySelector('h1').innerHTML = counted;
    localStorage.setItem('count',counted);
}

document.addEventListener('DOMContentLoaded',() =>{
    btn.onclick = () => {
        setInterval(counter,1000);
    }
})