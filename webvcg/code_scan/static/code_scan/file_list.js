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

function updateProgress(progressBarElement, progressBarMessageElement, progress) {
  progressBarElement.style.width = progress.percent + "%";
  progressBarMessageElement.innerHTML = progress.current + ' of ' + progress.total + ' processed.';
}

var trigger = document.getElementById('progress-bar-trigger');
trigger.addEventListener('click', function(e) {
  var bar = document.getElementById("progress-bar");
  var barMessage = document.getElementById("progress-bar-message");
  for (var i = 0; i < 11; i++) {
    setTimeout(updateProgress, 500 * i, bar, barMessage, {
      percent: 10 * i,
      current: 10 * i,
      total: 100
    })
  }
})