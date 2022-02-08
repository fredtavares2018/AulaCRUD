// Call the dataTables jQuery plugin
$(document).ready(function() {
  var table = $('#dataTable').DataTable( {
    lengthChange: false,
    buttons: [ 'copy', 'excel', 'pdf', 'colvis' ]
} );

table.buttons().container()
    .appendTo( '#example_wrapper .col-md-6:eq(0)' );
});
