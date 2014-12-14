<!DOCTYPE html>
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=UTF-8" />
<meta charset="utf-8" />
<title>SecMon | Log-in</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
<meta content="" name="description" />
<meta content="" name="author" />

<link href="assets/plugins/pace/pace-theme-flash.css" rel="stylesheet" type="text/css" media="screen"/>
<link href="assets/plugins/boostrapv3/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
<link href="assets/plugins/boostrapv3/css/bootstrap-theme.min.css" rel="stylesheet" type="text/css"/>
<link href="assets/plugins/font-awesome/css/font-awesome.css" rel="stylesheet" type="text/css"/>
<link href="assets/css/animate.min.css" rel="stylesheet" type="text/css"/>
<link href="assets/plugins/jquery-notifications/css/messenger.css" rel="stylesheet" type="text/css" media="screen"/>
<link href="assets/plugins/jquery-notifications/css/messenger-theme-flat.css" rel="stylesheet" type="text/css" media="screen"/>
<link href="assets/plugins/jquery-notifications/css/location-sel.css" rel="stylesheet" type="text/css" media="screen"/>

<link href="assets/css/style.css" rel="stylesheet" type="text/css"/>
<link href="assets/css/responsive.css" rel="stylesheet" type="text/css"/>
<link href="assets/css/custom-icon-set.css" rel="stylesheet" type="text/css"/>

</head>

<body class="error-body no-top">
<div class="container">
  <div class="row login-container column-seperation">  

          <h2>Security Monitor Log-in</h2><br>
		 <form id="login-form" class="login-form" action="/" method="post">
		 <div class="row">
		 <div class="form-group col-md-10">
            <label class="form-label">Username</label>
            <div class="controls">
				<div class="input-with-icon  right">                                       
					<i class=""></i>
					<input type="text" name="username" id="username" class="form-control">                                 
				</div>
            </div>
          </div>
          </div>
		  <div class="row">
          <div class="form-group col-md-10">
            <label class="form-label">Password</label>
            <span class="help"></span>
            <div class="controls">
				<div class="input-with-icon  right">                                       
					<i class=""></i>
					<input type="password" name="password" id="password" class="form-control">                                 
				</div>
            </div>
          </div>
          </div>
		  <div class="row">
          </div>
          <div class="row">
            <div class="col-md-10">
              <button class="btn btn-info btn-cons pull-right" type="submit">Login</button>
            </div>
          </div>
		  </form>   
  </div>
</div>


<script src="assets/js/login.js" type="text/javascript"></script>

<script src="assets/plugins/jquery-1.8.3.min.js" type="text/javascript"></script> 
<script src="assets/plugins/jquery-ui/jquery-ui-1.10.1.custom.min.js" type="text/javascript"></script> 
<script src="assets/plugins/bootstrap/js/bootstrap.min.js" type="text/javascript"></script> 
<script src="assets/plugins/breakpoints.js" type="text/javascript"></script> 
<script src="assets/plugins/jquery-unveil/jquery.unveil.min.js" type="text/javascript"></script> 
<script src="assets/plugins/jquery-block-ui/jqueryblockui.js" type="text/javascript"></script> 
<script type="text/javascript" src="http://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.4.3/underscore-min.js"></script>
<script type="text/javascript" src="http://cdnjs.cloudflare.com/ajax/libs/backbone.js/0.9.10/backbone-min.js"></script>
 
<script src="assets/plugins/jquery-scrollbar/jquery.scrollbar.min.js" type="text/javascript"></script>
<script src="assets/plugins/pace/pace.min.js" type="text/javascript"></script>  
<script src="assets/plugins/jquery-numberAnimate/jquery.animateNumbers.js" type="text/javascript"></script>
<script src="assets/plugins/jquery-notifications/js/messenger.min.js" type="text/javascript"></script>
<script src="assets/plugins/jquery-notifications/js/messenger-theme-future.js" type="text/javascript"></script>

 
<script type="text/javascript" src="assets/plugins/jquery-notifications/js/demo/location-sel.js"></script>
<script type="text/javascript" src="assets/plugins/jquery-notifications/js/demo/theme-sel.js"></script>
<script type="text/javascript" src="assets/js/notifications.js"></script>
 
<script src="assets/js/core.js" type="text/javascript"></script> 
<script src="assets/js/demo.js" type="text/javascript"></script> 

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