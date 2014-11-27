$(function(){
		var secArea = $(".sec_content");
		var card = $(".member_item");
		secArea.each(function(){
				$(this).bind({
						mouseenter:function(){
								$(this).find(".sec_title").css({opacity:"0.6"});
						},
						mouseleave:function(){
								$(this).find(".sec_title").css({opacity:"0.5"});
						}
				});
		});

		card.each(function(){
				$(this).bind({
						
				});	
		});
});
