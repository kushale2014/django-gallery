$(document).ready(function(){

	$('#album_items').on('click', 'a.nav-link', function(e){
		e.preventDefault();
		url = this.href;
		$.ajax({
			url: url,
			type: 'GET',
			success: function(res){
				$('#album_items').empty();
				$('#album_items').hide().fadeIn(500).html(res);
			},
			error: function(){
				alert('Error');
			}
		});
	});

});