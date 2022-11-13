const form  = document.querySelector('form');
const ul = document.querySelector('ul');
btn = document.querySelector('#submit');

document.addEventListener('DOMContentLoaded', function(){
    form.onsubmit = () => {
        btn.disabled = true;
        document.querySelector('#name').onkeyup = () => {
            btn.disabled = false;
        }
        const val = document.querySelector('#name').value;
        li = document.createElement('li');
        if (val.length != 0){
            li.innerHTML = val;
            ul.append(li);
            
        }
       
        document.querySelector('#name').value = '';
        btn.disabled = true;
        

        

        return false;

    }
    
})