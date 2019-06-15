$(document).ready(function(){
$('#buta').on('click', function() {
  alert("butaクリックされました");
  if($(this).hasClass("disabled")){
  alert("buta has dis");
  }else {
  alert("buta dont");
  }

    });
});