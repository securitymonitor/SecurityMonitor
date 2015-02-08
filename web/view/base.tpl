<!DOCTYPE html>
<html>
<head>

	<!-- Title block -->
	<title>Secmon | {{title or 'Security Monitor'}}</title>
	<meta http-equiv="content-type" content="text/html;charset=UTF-8" />
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
	<meta content="" name="description" />
	<meta content="" name="author" />

	<!-- Data Table Plugin CSS -->
	<link href="{{ url('assets', filepath='plugins/bootstrap-select2/select2.css') }}" rel="stylesheet" type="text/css" media="screen"/>
	<link href="{{ url('assets', filepath='plugins/jquery-datatable/css/jquery.dataTables.css') }}" rel="stylesheet" type="text/css"/>
	<link href="{{ url('assets', filepath='plugins/datatables-responsive/css/datatables.responsive.css') }}" rel="stylesheet" type="text/css" media="screen"/>

	<!-- Core Template CSS  -->
	<link href="{{ url('assets', filepath='plugins/pace/pace-theme-flash.css') }}" rel="stylesheet" type="text/css" media="screen"/>
	<link href="{{ url('assets', filepath='plugins/jquery-scrollbar/jquery.scrollbar.css') }}" rel="stylesheet" type="text/css"/>
	<link href="{{ url('assets', filepath='plugins/boostrapv3/css/bootstrap.min.css') }}" rel="stylesheet" type="text/css"/>
	<link href="{{ url('assets', filepath='plugins/boostrapv3/css/bootstrap-theme.min.css') }}" rel="stylesheet" type="text/css"/>
	<link href="{{ url('assets', filepath='plugins/font-awesome/css/font-awesome.css') }}" rel="stylesheet" type="text/css"/>
	<link href="{{ url('assets', filepath='css/animate.min.css') }}" rel="stylesheet" type="text/css"/>
	<link href="{{ url('assets', filepath='css/style.css') }}" rel="stylesheet" type="text/css"/>
	<link href="{{ url('assets', filepath='css/responsive.css') }}" rel="stylesheet" type="text/css"/>
	<link href="{{ url('assets', filepath='css/custom-icon-set.css') }}" rel="stylesheet" type="text/css"/>

	<!-- Notification CSS -->
	<link href="{{ url('assets', filepath='plugins/jquery-notifications/css/messenger.css') }}" rel="stylesheet" type="text/css" media="screen"/>
	<link href="{{ url('assets', filepath='plugins/jquery-notifications/css/messenger-theme-flat.css') }}" rel="stylesheet" type="text/css" media="screen"/>
	<link href="{{ url('assets', filepath='plugins/jquery-notifications/css/location-sel.css') }}" rel="stylesheet" type="text/css" media="screen"/>
	<script>
		function goBack() {
			window.history.back()
		}
		function goReaload() {
    		location.reload();
		}
	</script>

</head>
<body class="">

	<!-- Start top nav bar -->
	<div class="header navbar navbar-inverse"> 
		<div class="navbar-inner">
			<div class="header-seperation"> 
				<ul class="nav pull-left notifcation-center" id="main-menu-toggle-wrapper" style="display:none">	
					<li class="dropdown">
						<a id="main-menu-toggle" href="#main-menu" class="">
							<div class="iconset top-menu-toggle-white"></div>
						</a>
					</li>		 
				</ul>

				<a href="#">
					<img src="{{ url('assets', filepath='img/logo2.png') }}" class="logo" alt="" data-src="{{ url('assets', filepath='img/logo2.png') }}" data-src-retina="{{ url('assets', filepath='img/logo2.png') }}" width="106" height="21"/>
				</a>
				<ul class="nav pull-right notifcation-center">	
					<li class="dropdown" id="header_task_bar">
						<a href="{{ url('/dashboard') }}" class="dropdown-toggle active" data-toggle="">
							<div class="iconset top-home"></div>
						</a>
					</li>				        
				</ul>
			</div>
			<div class="header-quick-nav"> 
				<div class="pull-left"> 
					<ul class="nav quick-section">
						<li class="quicklinks">
							<a href="#" class="" id="layout-condensed-toggle">
								<div class="iconset top-menu-toggle-dark"></div>
							</a>
						</li>
					</ul>

					<ul class="nav quick-section">
						<li class="quicklinks"><a href="#" onclick="goReaload()" class=""><div class="iconset top-reload"></div></a></li>
					</ul>			
				</div>
			</div> 
		</div>
	</div>
	
	<!-- Start left nav structure -->
	<div class="page-container row-fluid">
		<div class="page-sidebar" id="main-menu"> 
			<div class="page-sidebar-wrapper scrollbar-dynamic" id="main-menu-wrapper">
				<div class="user-info-wrapper">	
					<div class="user-info"></div>
				</div>
				<ul>	

					%if title == 'Dashboard':
					<li class="start active">
					%else:
					<li class="">
					%end
						<a href="{{ url('/dashboard') }}">
							<i class="icon-custom-home"></i>
							<span class="title">Dashboard</span>
							<span class="selected"></span>
						</a>
					</li>

					%if title == 'Logs':
					<li class="start active">
					%else:
					<li class="">
					%end
						<a href="{{ url('/logs') }}">
							<i class="fa fa-bars"></i>
							<span class="title">Logs</span>
						</a>
					</li>

					%if title == 'Rules':
					<li class="start active">
					%else:
					<li class="">
					%end
						<a href="{{ url('/rules') }}">
							<i class="icon-custom-ui"></i>
							<span class="title">Rules</span>
						</a>
					</li>

					%if title == 'Users':
					<li class="start active">
					%else:
					<li class="">
					%end
						<a href="{{ url('/users') }}">
							<i class="fa fa-user"></i>
							<span class="title">Users</span>
						</a>
					</li>


					%if title == 'Settings':
					<li class="start active">
					%else:
					<li class="">
					%end
						<a href="{{ url('/settings') }}">
							<i class="fa fa-gear"></i>
							<span class="title">Settings</span>
						</a>
					</li>


					<li class="">
						<a href="{{ url('/logout') }}">
							<i class="fa fa-power-off"></i>
							<span class="title">Logout</span>
						</a>
					</li>

				</ul>
			</div>
		</div>

		<a href="#" class="scrollup">Scroll</a>
		<div class="footer-widget"><a href="https://github.com/zaanpenguin/SecurityMonitor" target="_blank">Version<sctrong> 1.0 beta 1</strong></a></div>
		
		{{!base}}

	</div>
</div>


	<!-- CORE JS Frameworks -->
	<script src="{{ url('assets', filepath='plugins/jquery-1.8.3.min.js') }}" type="text/javascript"></script> 
	<script src="{{ url('assets', filepath='plugins/jquery-ui/jquery-ui-1.10.1.custom.min.js') }}" type="text/javascript"></script> 
	<script src="{{ url('assets', filepath='plugins/bootstrap/js/bootstrap.min.js') }}" type="text/javascript"></script> 
	<script src="{{ url('assets', filepath='plugins/breakpoints.js') }}" type="text/javascript"></script> 
	<script src="{{ url('assets', filepath='plugins/jquery-unveil/jquery.unveil.min.js') }}" type="text/javascript"></script> 
	<script src="{{ url('assets', filepath='plugins/jquery-block-ui/jqueryblockui.js') }}" type="text/javascript"></script>
	<script src="{{ url('assets', filepath='plugins/jquery-scrollbar/jquery.scrollbar.min.js') }}" type="text/javascript"></script>
	<script src="{{ url('assets', filepath='plugins/pace/pace.min.js') }}" type="text/javascript"></script>  
	<script src="{{ url('assets', filepath='plugins/jquery-numberAnimate/jquery.animateNumbers.js') }}" type="text/javascript"></script>
	<script src="{{ url('assets', filepath='js/core.js') }}" type="text/javascript"></script> 
	<script src="{{ url('assets', filepath='js/demo.js') }}" type="text/javascript"></script>

	<!-- Data tables scripts -->
	<script src="{{ url('assets', filepath='plugins/jquery-scrollbar/jquery.scrollbar.min.js') }}" type="text/javascript"></script>
	<script src="{{ url('assets', filepath='plugins/bootstrap-select2/select2.min.js') }}" type="text/javascript"></script>
	<script src="{{ url('assets', filepath='plugins/jquery-datatable/js/jquery.dataTables.min.js') }}" type="text/javascript" ></script>
	<script src="{{ url('assets', filepath='plugins/jquery-datatable/extra/js/dataTables.tableTools.min.js') }}" type="text/javascript" ></script>
	<script src="{{ url('assets', filepath='plugins/datatables-responsive/js/lodash.min.js') }}" type="text/javascript"></script>
	<script src="{{ url('assets', filepath='plugins/datatables-responsive/js/datatables.responsive.js') }}" type="text/javascript"></script>
	<script src="{{ url('assets', filepath='secmon/js/datatables.js') }}" type="text/javascript"></script>

	<!-- Notification scripts -->
	<script src="{{ url('assets', filepath='plugins/jquery-notifications/js/messenger.min.js') }}" type="text/javascript"></script>
	<script src="{{ url('assets', filepath='plugins/jquery-notifications/js/messenger-theme-future.js') }}" type="text/javascript"></script>	
	<script src="{{ url('assets', filepath='js/notifications.js') }}" type="text/javascript"></script>

	<!-- Form validation scripts -->
	<script src="{{ url('assets', filepath='plugins/boostrap-form-wizard/js/jquery.bootstrap.wizard.min.js') }}" type="text/javascript"></script>
	<script src="{{ url('assets', filepath='plugins/jquery-validation/js/jquery.validate.min.js') }}" type="text/javascript"></script>
	<script src="{{ url('assets', filepath='js/form_validations.js') }}" type="text/javascript"></script>

	<!-- This is for the "select all" checkbox -->
	<script type="text/javascript" >
		$('table .checkbox input').click( function() {            
		    if($(this).is(':checked')){            
		        $(this).parent().parent().parent().toggleClass('row_selected');                    
		        }
		    else{    
		        $(this).parent().parent().parent().toggleClass('row_selected');        
		        }
		    });
	</script>

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