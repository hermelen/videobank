$(document).ready(function(){
  $('#inline_actor_form').submit(function(e){
    e.preventDefault();
    var url = $(this).attr('action');
    $.ajax({
      url: url,
      type: 'POST',
      data: $(this).serializeArray(),
      success: function(response){
        console.log('success');
        console.log(response);
      },
      error: function(response){
        console.log('error');
        console.log(response);
      }
    })
  })
})
