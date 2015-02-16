% rebase('base.tpl', title='Dashboard', url=url)
% import glob, os

<div class="page-content"> 
	<div class="content">
		<div class="row-fluid">


			% daemon_running = os.path.isfile('/tmp/secmon.pid')
			<div class="col-md-12">
				% if daemon_running:
				<div class="grid simple vertical green">
				% else:
				<div class="grid simple vertical red">
				% end
					<div class="grid">


						<div class="grid-body">
							<div class="col-md-4 col-sm-4">
								<h3 class="no-margin">Daemon Status</h3>
								<form action="" method="POST">
								% if daemon_running:
									<h4><span class="bold text-success">Running | <button type="submit" class="btn btn-white btn-small">Stop daemon</button></span></h4>		
								% else:
									<h4><span class="bold text-error">Stopped | <button type="submit" class="btn btn-white btn-small">Start daemon</button></span></h4>
								% end
							</div>

							% log_count = len(glob.glob(config["paths"]["dir_secmon_core"] + '*.log')) + 1
							<div class="col-md-4 col-sm-4">
								<h3 class="no-margin">Logs</h3>
								<h3><span class="item-count animate-number semi-bold" data-value="{{log_count}}" data-animation-duration="1500">0</span></h3>
							</div>

							% rule_count = len(glob.glob(config["paths"]["dir_secmon_rules"] + '*.txt')) - 1 
							<div class="col-md-4 col-sm-4">
								<h3 class="no-margin">Rules</h3>
								<h3><span class="item-count animate-number semi-bold" data-value="{{rule_count}}" data-animation-duration="1500">0</span></h3>
							</div>


						</div> <!-- / grid-body -->
					</div> <!-- / grid -->
				</div> <!-- / grid simple vertical -->
			</div> <!-- / col-md-12 -->


		</div>
	</div>
</div>