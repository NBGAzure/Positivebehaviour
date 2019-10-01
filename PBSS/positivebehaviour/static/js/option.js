$(document).ready(function() {

    $("#behaviour").change(function() {
        var val = $(this).val();
        if (val == "behaviour1") {
            $("#boptions").html("<option value='behaviouroptions1'>Select one</option>");
            $("#ageoptions").html("<option value='ageoptions1'>Select one</option>");
            $("#interactionoptions").html("<option value='interactionoptions1'>Select one</option>");
            $("#observationoptions").html("<option value='observationoptions1'>Select one</option>");
            $("#enganingoptions").html("<option value='enganingoptions1'>Select one</option>");
            $("#responseoptions").html("<option value='responseoptions1'>Select one</option>");
            $("#consequensesoptions").html("<option value='consequensesoptions1'>Select one</option>");
            $("#alternativeoptions").html("<option value='alternativeoptions1'>Select one</option>");
            $("#functionoptions").html("<option value='functionoptions1'>Select one</option>");

        } else if (val == "behaviour2") {


            $("#boptions").html("<option value='behaviouroptions1'>Select one</option><option value='behaviouroptions2'>familiar</option><option value='behaviouroptions3'>unfamiliar</option>");
            $("#ageoptions").html("<option value='ageoptions1'>Select one</option><option value='ageoptions2'>Adult</option><option value='ageoptions3'>Child</option><option value='ageoptions4'>Student</option>");
            $("#interactionoptions").html("<option value='interactionoptions1'>Select one</option><option value='interactionoptions2'>directs them to start or continue with a disliked task</option><option value='interactionoptions3'>directs them to stop a liked task</option><option value='interactionoptions4'>does not respond to their approach</option>");
            $("#observationoptions").html("<option value='observationoptions1'>Select one</option><option value='observationoptions2'>is off task but remains seated or in appropriate area</option><option value='observationoptions3'>is off task and distracting other students</option>");
            $("#enganingoptions").html("<option value='enganingoptions1'>Select one</option><option value='enganingoptions2'>given a verbal direction to stop the behaviour</option><option value='enganingoptions3'>given more information or clarification of the direction or request</option>");
            $("#responseoptions").html("<option value='responseoptions1'>Select one</option><option value='responseoptions2'>repeat request or question.</option><option value='responseoptions3'>accept refusal.</option>");
            $("#consequensesoptions").html("<option value='consequensesoptions1'>Select one</option><option value='consequensesoptions2'>ask for help.</option><option value='consequensesoptions3'>tell adult they are uncomfortable.</option>");
            $("#alternativeoptions").html("<option value='alternativeoptions1'>Select one</option><option value='alternativeoptions2'>ask for help.</option><option value='alternativeoptions3'>tell adult they are uncomfortable.</option>");
            $("#functionoptions").html("<option value='functionoptions1'>Select one</option><option value='functionoptions2'>Escape/Avoid stimulation or sensation</option><option value='functionoptions3'>Escape/Avoid stimulation or sensation</option>");

        } else if (val == "behaviour3") {

            $("#boptions").html("<option value='behaviouroptions3'>unfamiliar</option><option value='test2'>item3: test 2</option>")

        }
    });
});

$(document).ready(function() {
$('.mdb-select').materialSelect();
});
