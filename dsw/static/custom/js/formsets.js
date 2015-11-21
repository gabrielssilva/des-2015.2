function addGameForm() {

  $.ajax({
      url: '/game/get_game_form/',
      type: 'post',
      data: $('#ad-form').serializeArray(),
  }).done(function(response) {
      $('#ad-form-container').html(response);
  });
}


$('.add-form-btn').click(function() {
    return addGameForm();
});
