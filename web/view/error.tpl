<!DOCTYPE html>
% try:
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=UTF-8" />
<meta charset="utf-8" />
<title>SecMon | {{e.status}}</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
<meta content="" name="description" />
<meta content="" name="author" />

<link href="{{ url('assets', filepath='plugins/pace/pace-theme-flash.css') }}" rel="stylesheet" type="text/css" media="screen"/>
<link href="{{ url('assets', filepath='plugins/boostrapv3/css/bootstrap.min.css') }}" rel="stylesheet" type="text/css"/>
<link href="{{ url('assets', filepath='plugins/boostrapv3/css/bootstrap-theme.min.css') }}" rel="stylesheet" type="text/css"/>
<link href="{{ url('assets', filepath='plugins/font-awesome/css/font-awesome.css') }}" rel="stylesheet" type="text/css"/>
<link href="{{ url('assets', filepath='css/animate.min.css') }}" rel="stylesheet" type="text/css"/>

<link href="{{ url('assets', filepath='css/style.css') }}" rel="stylesheet" type="text/css"/>
<link href="{{ url('assets', filepath='css/responsive.css') }}" rel="stylesheet" type="text/css"/>
<link href="{{ url('assets', filepath='css/custom-icon-set.css') }}" rel="stylesheet" type="text/css"/>

</head>

<body class="error-body no-top">

	<div class="error-wrapper container">
	<div class="row">
	    <div class="col-md-4 col-md-offset-4 col-sm-6 col-sm-offset-3 col-xs-offset-1 col-xs-10">
	   <div class="error-container" >
	    <div class="error-main">
	      <div class="error-number"> {{e.status[0:3]}} </div>
	      <div class="error-description" > {{e.status[3:1000]}} </div>
	      <div class="error-description-mini"><pre>{{e.body}}</pre></div>
			%if debug and e.exception:
				<h2>Exception:</h2>
				<pre>{{repr(e.exception)}}</pre>
			%end
			%if debug and e.traceback:
				<h2>Traceback:</h2>
				<pre>{{e.traceback}}</pre>
			%end
	    </div>
	    </div>
	  
	  </div>
	</div>
	</div>


<script src="{{ url('assets', filepath='plugins/jquery-1.8.3.min.js') }}" type="text/javascript"></script>
<script src="{{ url('assets', filepath='plugins/bootstrap/js/bootstrap.min.js') }}" type="text/javascript"></script>
<script src="{{ url('assets', filepath='plugins/pace/pace.min.js') }}" type="text/javascript"></script>

</body>
</html>
%except ImportError:
    <b>ImportError:</b> Could not generate the error page. Please add bottle to
    the import path.
%end