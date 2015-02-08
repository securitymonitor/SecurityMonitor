% rebase('base.tpl', title='Rules', url=url)
% import os
% # List the directory with action files.
% action_dir_path = config["paths"]["dir_secmon_root"] + 'custom/actions/'
% action_files_array = os.listdir( action_dir_path )

<script>
	function goBack() {
		window.history.back()
	}
</script>

<div class="page-content"> 
	<div class="content">
		<div class="row">
			<div class="col-md-12">
				<div class="grid simple ">
					<div class="grid-body ">
					<h1>Create new rule</h1>
						<div class="col-md-6">
							<div class="form-group">
								<form action="/create_rule" method="POST">


								<label class="form-label">Rule name</label>
								<span class="help">Required</span>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										<input type="text" name="rule_name" id="rule_name" class="form-control">                                 
									</div><br />

								<label class="form-label">Rule Description</label>
								<span class="help">Required</span>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										<input type="text" name="rule_description" id="rule_description" class="form-control">                                 
									</div><br />

								<label class="form-label">Source IP-address</label>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										<input type="text" name="source-ip-address" id="source-ip-address" class="form-control">                                 
									</div><br />
							
								<label class="form-label">Source IP-port</label>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										<input type="text" name="source-ip-port" id="source-ip-port" class="form-control">                                 
									</div><br />

								<label class="form-label">Target IP-address</label>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										<input type="text" name="target-ip-address" id="target-ip-address" class="form-control">                                 
									</div><br />

								<label class="form-label">Target IP-port</label>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										<input type="text" name="target-ip-port" id="target-ip-port" class="form-control">                                 
									</div><br />

								<label class="form-label">Protocol</label>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										<select name="protocol" id="protocol" class="select2 form-control">
											<option value="UDP">UDP</option>
											<option value="TCP">TCP</option>
										</select>                              
									</div><br />


								</div> <!-- /form-froup -->
							</div> <!-- /col-md-6 -->
							<div class="col-md-6">
								<div class="form-group">

								<label class="form-label">Package Count</label>
								<span class="help">Required</span>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										<input type="text" name="count" id="count" class="form-control">                                 
									</div><br />

								<label class="form-label">Interval</label>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										<input type="text" name="interval" id="interval" class="form-control" placeholder="hh:mm:ss">                                 
									</div><br />

								<label class="form-label">Action</label>
								<span class="help">Required</span>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										<select name="action" id="action" class="select2 form-control">

										% # This script will read all action python files from the action directory.
										% for item in action_files_array:
											% if (item.endswith('.py')) and (item != '__init__.py'):
											<option value="{{item}}">{{item}}</option>
											% end
										% end

										</select>                                  
									</div><br />

								<label class="form-label">Log</label>
								<span class="help">Required</span>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										<select name="log" id="log" class="select2 form-control">   

										% # This code will read all "log files" from the log directory.
										% log_dir_path = config["paths"]["dir_secmon_core"]
										% log_files_array = os.listdir( log_dir_path )

										% for item in log_files_array:
											% if item.endswith('.log'):
											<option value="{{item}}">{{item}}</option>
											% end
										% end

										</select> 
									</div><br />

								<label class="form-label">Message</label>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										<input type="text" name="message" id="message" class="form-control" placeholder="ipv4">                                 
									</div><br />

								<label class="form-label">Match</label>
								<span class="help">Required</span>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										<input type="text" name="match" id="match" class="form-control" placeholder="SOURCEIP, TARGETIP, PROTOCOL">                                 
									</div><br />

									<button class="btn btn-info btn-cons btn-cancel" type="submit">Create</button>
									<button class="btn btn-white btn-cons btn-cancel" type="button" onclick="goBack()">Back</button>


								</form>
							</div> <!-- /form-froup -->
						</div> <!-- /col-md-6 -->
						<div class="col-md-12">
						Click here for the explenation.
						</div> <!-- /col-md-12 -->
					</div>
				</div>
			</div>
		</div>
	</div>
</div>