section  = document.querySelectorAll('div');
function showPage(page){
    section.forEach( div => {
        div.style.display = 'none'
    })
    div = document.querySelector(`#${page}`);
    if (div.style.display = 'none'){
        div.style.display = 'block';
    }else{
        div.style.display = 'none';
    }
    

}

document.addEventListener('DOMContentLoaded',() =>{
    document.querySelectorAll('button').forEach( btn =>{
        btn.onclick = () => {
            showPage(btn.dataset.page);
        }
    })
})