document.querySelector("form").onclick = function(e){
    const clicked_elem = e.target;
    if (clicked_elem.tagName == "BUTTON"){
        var x = document.getElementById('genshinedit')
        x.hidden = true;
    }
}

let img = document.querySelector('character-build');

document.querySelector('#b-img-icon').onclick = () => {
    img.classList.toggle('active');
}