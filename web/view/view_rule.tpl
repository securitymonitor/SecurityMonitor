% rebase('base.tpl', title='Rules', url=url)
% import os
% values = configlist.values()


<div class="page-content"> 
	<div class="content">
		<div class="row">
			<div class="col-md-12">
				<div class="grid simple ">
					<div class="grid-body ">
					% value = configlist.get('NAME=')
					<h1>{{value}}</h1>

						<div class="col-md-6">
							<div class="form-group">
								<form action="/create_rule" method="POST">

								% # current_rulename is the name of the rule .txt (example.txt)
								% # If this is edited, the server needs to know this to make sure the modification is done corerctly.
								% current_rulename = configlist.get('NAME=')
								<input type="hidden" name="current_rulename" value="{{current_rulename}}"> 

								% value = configlist.get('NAME=')
								<label class="form-label">Rule name</label>
								<span class="help">Required</span>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										% if value:
										<input type="text" name="rule_name" id="rule_name" class="form-control" value="{{value}}">
										% else:
										<input type="text" name="rule_name" id="rule_name" class="form-control">
										% end                                 
									</div><br />

								% value = configlist.get('DESCRIPTION=')
								<label class="form-label">Rule Description</label>
								<span class="help">Required</span>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										% if value:
										<input type="text" name="rule_description" id="rule_description" class="form-control" value="{{value}}">
										% else:
										<input type="text" name="rule_description" id="rule_description" class="form-control">
										% end
									</div><br />

								% value = configlist.get('SOURCEIP=')
								<label class="form-label">Source IP-address</label>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										% if value:
										<input type="text" name="source-ip-address" id="source-ip-address" class="form-control" value="{{value}}">
										% else:
										<input type="text" name="source-ip-address" id="source-ip-address" class="form-control">
										% end
									</div><br />
							
								% value = configlist.get('SOURCEPT=')
								<label class="form-label">Source IP-port</label>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										% if value:
										<input type="text" name="source-ip-port" id="source-ip-port" class="form-control" value="{{value}}">
										% else:
										<input type="text" name="source-ip-port" id="source-ip-port" class="form-control">
										% end

									</div><br />

								% value = configlist.get('TARGETIP=')
								<label class="form-label">Target IP-address</label>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										% if value:
										<input type="text" name="target-ip-address" id="target-ip-address" class="form-control" value="{{value}}">
										% else:
										<input type="text" name="target-ip-address" id="target-ip-address" class="form-control">
										% end
									</div><br />

								% value = configlist.get('TARGETPT=')
								<label class="form-label">Target IP-port</label>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										% if value:
										<input type="text" name="target-ip-port" id="target-ip-port" class="form-control" value="{{value}}">
										% else:
										<input type="text" name="target-ip-port" id="target-ip-port" class="form-control">
										% end
									</div><br />

								% value = configlist.get('PROTOCOL=')
								<label class="form-label">Protocol</label>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										% if value:
										<select name="protocol" id="protocol" class="select2 form-control" value="{{value}}">
										% else:
										<select name="protocol" id="protocol" class="select2 form-control">
										% end
											<option value="UDP">UDP</option>
											<option value="TCP">TCP</option>
										</select>                              
									</div><br />

							</div> <!-- /form-froup -->
						</div> <!-- /col-md-6 -->
						<div class="col-md-6">
								<div class="form-group">

								% value = configlist.get('COUNT=')
								<label class="form-label">Count</label>
								<span class="help">Required</span>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										% if value:
										<input type="text" name="count" id="count" class="form-control" placeholder="Package count" value="{{value}}">
										% else:
										<input type="text" name="count" id="count" class="form-control" placeholder="Package count">
										% end
									</div><br />

								% value = configlist.get('INTERVAL=')
								<label class="form-label">Interval</label>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										% if value:
										<input type="text" name="interval" id="interval" class="form-control" value="{{value}}">
										% else:
										<input type="text" name="interval" id="interval" class="form-control">
										% end
									</div><br />

								% value = configlist.get('ACTION=')
								<label class="form-label">Action</label>
								<span class="help">Required</span>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										% if value:
										<select name="action" id="action" class="select2 form-control" value="{{value}}">
										% else:
										<select name="action" id="action" class="select2 form-control">
										% end


										% # This code will read all "action files" from the action directory.
										% action_dir_path = config["paths"]["dir_secmon_root"] + 'custom/actions/'
										% action_files_array = os.listdir( action_dir_path )

										% for item in action_files_array:
											% if (item.endswith('.py')) and (item != '__init__.py'):
											<option value="{{item}}">{{item[:-3]}}</option>
											% end
										% end
										</select>                                  
									</div><br />

								% value = configlist.get('LOG=')
								<label class="form-label">Log</label>
								<span class="help">Required</span>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										% if value:
										<select name="log" id="log" class="select2 form-control" value="{{value}}">
										% else:
										<select name="log" id="log" class="select2 form-control">
										% end

										% # This code will read all "log files" from the log directory.
										% log_dir_path = config["paths"]["dir_secmon_core"]
										% log_files_array = os.listdir( log_dir_path )

										% for item in log_files_array:
											% if item.endswith('.log'):
											<option value="{{item}}">{{item[:-4]}}</option>
											% end
										% end
										</select>
									</div><br />

								% value = configlist.get('MESSAGE=')
								<label class="form-label">Message</label>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										% if value:
										<input type="text" name="message" id="message" class="form-control" placeholder="ipv4" value="{{value}}">
										% else:
										<input type="text" name="message" id="message" class="form-control" placeholder="ipv4">
										% end
									</div><br />

								% value = configlist.get('MATCH=')
								<label class="form-label">Match</label>
								<span class="help">Required</span>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										% if value:
										<input type="text" name="match" id="match" class="form-control" placeholder="SOURCEIP, TARGETIP, PROTOCOL" value="{{value}}">
										% else:
										<input type="text" name="match" id="match" class="form-control" placeholder="SOURCEIP, TARGETIP, PROTOCOL">
										% end
									</div><br />

									<button class="btn btn-info btn-cons btn-cancel" type="submit">Modify</button>
									<button class="btn btn-white btn-cons btn-cancel" type="button" onclick="goBack()">Back</button>


								</form>
							</div> <!-- /form-froup -->
						</div> <!-- /col-md-6 -->
					</div>
				</div>
			</div>
		</div>
	</div>
</div>