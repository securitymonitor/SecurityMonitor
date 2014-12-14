			<!-- END PAGE CONTENT -->
		</div>
	</div>
	<!-- END PAGE CONTAINER -->
</div>


<!-- CORE scripts -->
<script src="{{ url('assets', filepath='plugins/jquery-1.8.3.min.js') }}" type="text/javascript"></script> 
<script src="{{ url('assets', filepath='plugins/jquery-ui/jquery-ui-1.10.1.custom.min.js') }}" type="text/javascript"></script> 
<script src="{{ url('assets', filepath='plugins/bootstrap/js/bootstrap.min.js') }}" type="text/javascript"></script> 
<script src="{{ url('assets', filepath='plugins/breakpoints.js') }}" type="text/javascript"></script> 
<script src="{{ url('assets', filepath='plugins/jquery-unveil/jquery.unveil.min.js') }}" type="text/javascript"></script> 
<script src="{{ url('assets', filepath='plugins/jquery-block-ui/jqueryblockui.js') }}" type="text/javascript"></script> 

<!-- Data tables scripts -->
<script src="{{ url('assets', filepath='plugins/jquery-scrollbar/jquery.scrollbar.min.js') }}" type="text/javascript"></script>    
<script src="{{ url('assets', filepath='plugins/jquery-block-ui/jqueryblockui.js') }}" type="text/javascript"></script>
<script src="{{ url('assets', filepath='plugins/jquery-numberAnimate/jquery.animateNumbers.js') }}" type="text/javascript"></script>
<script src="{{ url('assets', filepath='plugins/bootstrap-select2/select2.min.js') }}" type="text/javascript"></script>
<script src="{{ url('assets', filepath='plugins/jquery-datatable/js/jquery.dataTables.min.js') }}" type="text/javascript" ></script>
<script src="{{ url('assets', filepath='plugins/jquery-datatable/extra/js/dataTables.tableTools.min.js') }}" type="text/javascript" ></script>
<script type="text/javascript" src="{{ url('assets', filepath='plugins/jquery-datatable/extra/js/dataTables.tableTools.min.js') }}"></script>
<script type="text/javascript" src="{{ url('assets', filepath='plugins/datatables-responsive/js/lodash.min.js') }}"></script>

<!-- Notification scripts -->
<script src="{{ url('assets', filepath='plugins/jquery-scrollbar/jquery.scrollbar.min.js') }}" type="text/javascript"></script>
<script src="{{ url('assets', filepath='plugins/pace/pace.min.js') }}" type="text/javascript"></script>  
<script src="{{ url('assets', filepath='plugins/jquery-numberAnimate/jquery.animateNumbers.js') }}" type="text/javascript"></script>
<script src="{{ url('assets', filepath='plugins/jquery-notifications/js/messenger.min.js') }}" type="text/javascript"></script>
<script src="{{ url('assets', filepath='plugins/jquery-notifications/js/messenger-theme-future.js') }}" type="text/javascript"></script>	
<script type="text/javascript" src="{{ url('assets', filepath='plugins/jquery-notifications/js/demo/location-sel.js') }}"></script>
<script type="text/javascript" src="{{ url('assets', filepath='plugins/jquery-notifications/js/demo/theme-sel.js') }}"></script>
<script type="text/javascript" src="{{ url('assets', filepath='js/notifications.js') }}"></script>
<script src="{{ url('assets', filepath='js/datatables.js') }}" type="text/javascript"></script>

<!-- More core scripts -->
<script src="{{ url('assets', filepath='js/core.js') }}" type="text/javascript"></script> 
<script src="{{ url('assets', filepath='js/demo.js') }}" type="text/javascript"></script> 

<!-- Notification JS -->
% if defined('notification'):
	<script type="text/javascript" >
	$(function(){
	  Messenger().post("{{notification}}");

	  var loc = ['bottom', 'right'];
	  var style = 'flat';

	  var $output = $('.controls output');
	  var $lsel = $('.location-selector');
	  var $tsel = $('.theme-selector');

	  var update = function(){
	    var classes = 'messenger-fixed';

	    for (var i=0; i < loc.length; i++)
	      classes += ' messenger-on-' + loc[i];

	    $.globalMessenger({ extraClasses: classes, theme: style });
	    Messenger.options = { extraClasses: classes, theme: style };

	    $output.text("Messenger.options = {\n    extraClasses: '" + classes + "',\n    theme: '" + style + "'\n}");
	  };

	  update();

	  $lsel.locationSelector()
	    .on('update', function(pos){
	      loc = pos;

	      update();
	    })
	  ;

	  $tsel.themeSelector({
	    themes: ['flat', 'future', 'block', 'air', 'ice']
	  }).on('update', function(theme){
	    style = theme;

	    update();
	  });

	});
	</script>
% end
</body>
</html>