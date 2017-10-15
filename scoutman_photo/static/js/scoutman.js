$(document).ready(function () {	
	
	$('.nav li').hover(
		function () {
			$('ul', this).stop().slideDown(1);

		}, 
		function () {
			$('ul', this).stop().slideUp(1);
		}
	);
	
	$('.fancybox').fancybox({
		padding : 8,
		openEffect	: 'fade',
		closeEffect	: 'fade',
		openSpeed : 200,
		closeSpeed : 200,
		nextSpeed : 200,
		prevSpeed : 200,
		helpers: {
			title : {
				type : 'float'
			}
		}
	});
	
});
