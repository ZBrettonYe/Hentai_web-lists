var url,title;

$('#bookmarkme').click(function(e){
    addFavorite(url, title);
    e.preventDefault();
});

function addFavorite(url, title) {
    if(window.external && 'addFavorite' in window.external){
        window.external.addFavorite(url, title);
    } else if(window.sidebar && window.sidebar.addPanel) {
        window.sidebar.addPanel(url, title);
    } else if(window.opera && window.print) {
        this.title = title;
        return true;
    } else {
        alert('Press ' + (navigator.userAgent.toLowerCase().indexOf('mac') != - 1 ? 'Command/Cmd' : 'CTRL') + ' + D to bookmark this page.');
    }
}