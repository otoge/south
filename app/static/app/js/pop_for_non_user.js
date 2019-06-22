$(document).ready(function(){
    $("#non_user").click(function(){


      if($(this).hasClass("disabled")){
        void(0);
      }else{
//      $("[data-toggle='popover']").popover('show');

       $("#non_user").popover('show');




        setTimeout(function(){
             $("#non_user").popover('dispose');
        },3000);

//        $(this).addClass("disabled");
//
//        $(this).text("お気に入りに追加済み");


      }

    });
});