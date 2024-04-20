document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('colorForm').addEventListener('submit', function(event) {
      event.preventDefault();
      var color = document.getElementById('colorInput').value;
      document.getElementById('header').style.color = color;
    });
});
