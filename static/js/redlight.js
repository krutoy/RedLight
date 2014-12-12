$(function(){
		var secArea = $(".sec_content");
		var card = $(".member_item");
		var unfoldButton = $(".unfold_btn");
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

		unfoldButton.each(function(){
				$(this).bind({
						mouseenter:function(){
								$(this).parent().next().slideToggle();
						},
						mouseleave:function(){
								$(this).parent().next().slideToggle();
						}
				});
		});
});
