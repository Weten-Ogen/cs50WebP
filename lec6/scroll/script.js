
window.onscroll = () => {
    if(window.innerHeight + window.scrollY  >= document.body.offsetHeight){
        document.querySelector('body').style.background= 'red';
        document.querySelector('body').style.color = 'black';
    }else {
        document.querySelector('body').style.background= 'black';
        document.querySelector('body').style.color = 'red';
    }
}