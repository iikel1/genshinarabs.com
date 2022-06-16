document.querySelector("form").onclick = function(e){
    const clicked_elem = e.target;
    if (clicked_elem.tagName == "BUTTON"){
        var x = document.getElementById('genshinedit')
        x.hidden = true;
    }
}