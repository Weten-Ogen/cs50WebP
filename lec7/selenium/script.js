

document.addEventListener('DOMContentLoaded', function(){
    // When Increase is pressed
    document.querySelector("#increase").onclick = () =>{
        document.querySelector("h1").innerHTML ++;
    }
    document.querySelector("#decrease").onclick =()=> {
        document.querySelector("h1").innerHTML --;
    }

})