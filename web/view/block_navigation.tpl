<!DOCTYPE html>
<html>
<head>
	<title>Secmon | {{page}}</title>
	<meta http-equiv="content-type" content="text/html;charset=UTF-8" />
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
	<meta content="" name="description" />
	<meta content="" name="author" />


	<!-- Data Table Plugin CSS -->
	<link href="{{ url('assets', filepath='plugins/bootstrap-select2/select2.css') }}" rel="stylesheet" type="text/css" media="screen"/>
	<link href="{{ url('assets', filepath='plugins/jquery-datatable/css/jquery.dataTables.css') }}" rel="stylesheet" type="text/css"/>
	<link href="{{ url('assets', filepath='plugins/datatables-responsive/css/datatables.responsive.css') }}" rel="stylesheet" type="text/css" media="screen"/>

	<!-- Core Plugin CSS -->
	<link href="{{ url('assets', filepath='plugins/boostrapv3/css/bootstrap.min.css') }}" rel="stylesheet" type="text/css"/>
	<link href="{{ url('assets', filepath='plugins/boostrapv3/css/bootstrap-theme.min.css') }}" rel="stylesheet" type="text/css"/>
	<link href="{{ url('assets', filepath='plugins/font-awesome/css/font-awesome.css') }}" rel="stylesheet" type="text/css"/>
	<link href="{{ url('assets', filepath='css/animate.min.css') }}" rel="stylesheet" type="text/css"/>
	<link href="{{ url('assets', filepath='plugins/jquery-scrollbar/jquery.scrollbar.css') }}" rel="stylesheet" type="text/css"/>

	<!-- Notification CSS -->
	<link href="{{ url('assets', filepath='plugins/pace/pace-theme-flash.css') }}" rel="stylesheet" type="text/css" media="screen"/>
	<link href="{{ url('assets', filepath='plugins/jquery-notifications/css/messenger.css') }}" rel="stylesheet" type="text/css" media="screen"/>
	<link href="{{ url('assets', filepath='plugins/jquery-notifications/css/messenger-theme-flat.css') }}" rel="stylesheet" type="text/css" media="screen"/>
	<link href="{{ url('assets', filepath='plugins/jquery-notifications/css/location-sel.css') }}" rel="stylesheet" type="text/css" media="screen"/>

	<!-- Core template CSS -->
	<link href="{{ url('assets', filepath='css/style.css') }}" rel="stylesheet" type="text/css"/>
	<link href="{{ url('assets', filepath='css/responsive.css') }}" rel="stylesheet" type="text/css"/>
	<link href="{{ url('assets', filepath='css/custom-icon-set.css') }}" rel="stylesheet" type="text/css"/>

</head>
<body class="">
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
				<img src="assets/img/logo2.png" class="logo" alt="" data-src="{{ url('assets', filepath='img/logo2.png') }}" data-src-retina="{{ url('assets', filepath='img/logo2.png') }}" width="106" height="21"/>
			</a>
			<ul class="nav pull-right notifcation-center">	
				<li class="dropdown" id="header_task_bar">
					<a href="#" class="dropdown-toggle active" data-toggle="">
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
					<li class="quicklinks"><a href="#" onclick="pageReload()" class=""><div class="iconset top-reload"></div></a></li>
				</ul>			
			</div>
		</div> 
	</div>
</div>
	
<!-- Start left menu index-->
<div class="page-container row-fluid">

	<div class="page-sidebar" id="main-menu"> 
		  <div class="page-sidebar-wrapper scrollbar-dynamic" id="main-menu-wrapper">

		<div class="user-info-wrapper">	
			<div class="user-info">
			</div>
		</div>
		<ul>	

			%if page == 'Dashboard':
			   	<li class="start active">
			%else:
			   	<li class="">
			%end
				<a href="dashboard">
					<i class="icon-custom-home"></i>
					<span class="title">Dashboard</span>
					<span class="selected"></span>
				</a>
			</li>

			%if page == 'Rules':
			   	<li class="start active">
			%else:
			   	<li class="">
			%end
					<a href="rules">
						<i class="icon-custom-ui"></i>
						<span class="title">Rules</span>
					</a>
				</li>


			%if page == 'Users':
			   	<li class="start active">
			%else:
			   	<li class="">
			%end
					<a href="users">
						<i class="fa fa-user"></i>
						<span class="title">User</span>
						<span class="arrow"></span
					</a>
					<ul class="sub-menu">
						<li><a href="/users/manage">All Users</a></li>
						<li><a href="/users/add">Add New</a></li>
						<li><a href="/users/remove">Your Profile</a></li>
					</ul>
				</li>

			%if page == 'Settings':
			   	<li class="start active">
			%else:
			   	<li class="">
			%end
				<a href="settings">
					<i class="fa fa-gear"></i>
					<span class="title">Settings</span>
				</a>
			</li>


			   	<li class="">
				<a href="logout">
					<i class="fa fa-power-off"></i>
					<span class="title">Logout</span>
				</a>
			</li>

		</ul>
	</div>
</div>
<a href="#" class="scrollup">Scroll</a>
<div class="footer-widget"><a href="https://github.com/zaanpenguin/SecurityMonitor" target="_blank"><sctrong>Development</strong> Version</a></div>  