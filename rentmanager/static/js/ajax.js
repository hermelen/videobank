// $(document).ready(function(){
//   $('#inline_actor_form').submit(function(event){
//     event.preventDefault();
//     var url = $(this).attr('action');
//     $.ajax({
//       url: url,
//       type: 'POST',
//       data: $(this),
//       success: function(response){
//         console.log('success');
//         console.log(response);
//       },
//       error: function(response){
//         console.log('error');
//         console.log(response);
//       }
//     })
//   })
// })


// $('#id_actors').append(`
//   <option value="${response.pk}" selected>${response.last_name.toUpperCase()} ${ response.last_name.charAt(0).toUpperCase() + response.last_name.slice(1) }</option>
// `)
