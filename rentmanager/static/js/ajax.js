$(document).ready(function(){
  $('.inline-form').submit(function(event){
    event.preventDefault();
    var url = $(this).attr('action');
    $.ajax({
      url: url,
      type: 'POST',
      data: $(this).serialize(),
      success: function(response){
        console.log(response.type);
        if ( response.type == "actor" ) {
          $("#id_actors").append(`
            <option value="${response.pk}" selected>${response.last_name.toUpperCase()} ${ response.last_name.charAt(0).toUpperCase() + response.last_name.slice(1) }</option>
          `)
        } else if ( response.type == "director" ) {
          $("#id_director").append(`
            <option value="${response.pk}" selected>${response.last_name.toUpperCase()} ${ response.last_name.charAt(0).toUpperCase() + response.last_name.slice(1) }</option>
          `)
        } else {
          $("#id_country").append(`
            <option value="${response.pk}" selected>${response.name.toUpperCase()}</option>
          `)
        }
      },
      error: function(response){
        console.log('error');
      }
    })
  })
})
