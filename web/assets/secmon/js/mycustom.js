
//Init Datatable to table with the id mytable
var oTable3 = $('#mytable').dataTable( {
"sDom": "<'row'<'col-md-6'l <'toolbar'>><'col-md-6'f>r>t<'row'<'col-md-12'p i>>"
});

//Call this function on button click
function fnClickAddRow() {
   //fnAddData is a Datatable function to add a row dynamically to a table
   //fnAddData requires and array of values : the array length is equal to the number of columns in that table
   //Example ('#mytable').dataTable().fnAddData(["1","2","3"]);
    $('#mytable').dataTable().fnAddData( [
        //$("#val1").text() is the way we get value from a textfield : #val1 is a textfield
        $("#val1").text(),
        $("#val2").text(),
        $("#val3").text());     
}	