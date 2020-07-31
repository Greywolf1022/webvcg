var selDiv = "";

document.addEventListener("DOMContentLoaded", init, false);

function init() {
    document.querySelector('#id_scan_files').addEventListener('change', handleFileSelect, false);
    selDiv = document.querySelector("#selectedFiles");
}

function handleFileSelect(e) {

    if(!e.target.files) return;

    selDiv.innerHTML = "";

    var files = e.target.files;
    for(var i=0; i<files.length; i++) {
        var f = files[i];

        selDiv.innerHTML += (i + 1) + ". " + f.name + "<br/>";

    }

}

var frm = $('#scan-file-form');
frm.submit(function () {
    var frmData = new FormData(frm.get(0));
    $.ajax({
        type: frm.attr('method'),
        url: frm.attr('action'),
        data: frmData,
        processData: false,
        contentType: false,
        success: function (data) {
            console.log(data);
        },
        error: function (data) {
            console.log("Something went wrong!");
        }
    });
    return false;
});