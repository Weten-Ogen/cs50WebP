red = document.querySelector('#red');
blue = document.querySelector('#blue');
green = document.querySelector('#green');
txt = document.querySelector('h1');
btn = document.querySelectorAll('button');
slt = document.querySelector('select');
document.addEventListener('DOMContentLoaded',function()
{
    // for each btn , set the color accordingly
    btn.forEach(btn => {
        btn.onclick = () => txt.style.color = btn.dataset.color;
         
    })

    // for each select
    slt.onchange = function () {
        txt.style.color  = this.value;
    } 
})