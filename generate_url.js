//Iterate over img tag containing .rg-i class 
//Used window object to create a csv file containing all google images

urls = Array.from(
    document.querySelectorAll('.rg_i')).
    map(el=> el.hasAttribute('data-src')    ?  el.getAttribute('data-src')  :   el.getAttribute('data-iurl'));

//generate csv file to download

window.open('data:text/csv;charset=utf-8,' + escape(urls.join('\n')));