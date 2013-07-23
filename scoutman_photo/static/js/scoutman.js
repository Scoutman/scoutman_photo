$(document).ready(function () {	
	$('#slider').nivoSlider({
		effect: 'fade',
		pauseTime: 8000,
		controlNav: false,
		animSpeed: 1000,
	});
	
	$('.nav li').hover(
		function () {
			$('ul', this).stop().slideDown(1);

		}, 
		function () {
			$('ul', this).stop().slideUp(1);
		}
	);
	
});
