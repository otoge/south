

$(document).ready(function(){
    $("#boke").click(function(){


      if($(this).hasClass("disabled")){
        void(0);
      }else{
//      $("[data-toggle='popover']").popover('show');

       $("#boke").popover('show');

//        setTimeout(function(){
//             $("#boke").popover('destroy');
//        },3000);

        $(this).addClass("disabled");

        $(this).text("お気に入りに追加済み");


      }

    });
});