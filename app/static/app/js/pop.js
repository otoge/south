$(".show-popover").on('click',function(){
	$("#myPopover").popover('show');
});
$(".hide-popover").on('click',function(){
	$("#myPopover").popover('hide');
});
$(".toggle-popover").on('click',function(){
	$("#myPopover").popover('toggle');
});
$(".dispose-popover").on('click',function(){
	$("#myPopover").popover('dispose');
});