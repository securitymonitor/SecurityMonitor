% rebase('base.tpl', title='Dashboard', url=url)
% import glob, os
% # List the directory with rule files. -1 beceause of the rule template file "RuleDefinitionTable.txt", needed for the application to work but not a logfile.
% rule_count = len(glob.glob(config["paths"]["dir_secmon_rules"] + '*.txt')) - 1 
% # List the directory with log files. Notice: webserver log (bottle.log) will also be loaded from the webserver dir so +1 for the webserver logfile.
% log_count = len(glob.glob(config["paths"]["dir_secmon_core"] + '*.log')) + 1
% daemon_running = os.path.isfile('/tmp/secmon.pid')
% os.system('python ' + config["paths"]["dir_secmon_core"] + 'securitymonitor.py start')

<div class="page-content"> 
	<div class="content">
		<div class="row-fluid">
			<div class="row">

	<div class="col-md-12">
		% if daemon_running:
		<div class="grid simple vertical green">
		% else:
		<div class="grid simple vertical red">
		% end
			<div class="grid-title">
				<h4><span class="semi-bold">Daemon Status</span></h4>
				<div class="tools">
					<a href="javascript:;" class="collapse"></a>
					<a href="javascript:;" class="reload"></a> <a href="javascript:;" class="remove"></a>
            	</div>
			</div>
			<div class="grid-body">
				<div class="row-fluid">	
					<form action="" method="POST">
					% if daemon_running:
					<h1><span class="bold text-success">RUNNING<button type="submit" class="btn btn-white btn-cons" style="float:right">Stop daemon</button></span></h1>		
					% else:
					<h1><span class="bold text-error">STOPPED<button type="submit" class="btn btn-white btn-cons" style="float:right">Start daemon</button></span></h1>
					% end
					</form>								 
				</div>
			</div>
		</div> 
	</div>


	<div class="col-md-12">
		% if rule_count >= 1:
		<div class="grid simple vertical green">
		% else:
		<div class="grid simple vertical red">
		% end
			<div class="grid-title">
				<h4><span class="semi-bold">Rules</span></h4>
				<div class="tools">
					<a href="javascript:;" class="collapse"></a>
					<a href="javascript:;" class="reload"></a> <a href="javascript:;" class="remove"></a>
            	</div>
			</div>
			<div class="grid-body">
				<div class="row-fluid ">
					% if rule_count >= 1:
					<h1><span class="bold text-success">{{rule_count}}</span></h1>	
					% else:
					<h1><span class="bold text-error">{{rule_count}}</span></h1>
					% end							 
				</div>
			</div>
		</div> 
	</div>

	<div class="col-md-12">
		% if log_count >= 1:
		<div class="grid simple vertical green">
		% else:
		<div class="grid simple vertical red">
		% end
			<div class="grid-title">
				<h4><span class="semi-bold">Logfiles</span></h4>
				<div class="tools">
					<a href="javascript:;" class="collapse"></a>
					<a href="javascript:;" class="reload"></a> <a href="javascript:;" class="remove"></a>
            	</div>
			</div>
			<div class="grid-body">
				<div class="row-fluid ">
					% if rule_count >= 1:
					<h1><span class="bold text-success">{{log_count}}</span></h1>	
					% else:
					<h1><span class="bold text-error">{{log_count}}</span></h1>	
					% end									 
				</div>
			</div>
		</div> 
	</div>






		</div>
	</div>
</div>