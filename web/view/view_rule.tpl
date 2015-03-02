% rebase('base.tpl', title='Rules', url=url)
% import os

<div class="page-content"> 
	<div class="content">
		<div class="row">
			<div class="col-md-12">
				<div class="grid simple ">
					<div class="grid-body ">
					% value = configlist.get('NAME =').strip("'")
					<h1>{{value}}</h1>

						<div class="col-md-6">
							<div class="form-group">
								<form action="/create_rule" method="POST">

								<input type="hidden" name="current_rulename" value="{{value}}"> 

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

								% value = configlist.get('DESCRIPTION =').strip("'")
								<label class="form-label">Rule description</label>
								<span class="help">Required</span>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										% if value:
										<input type="text" name="rule_description" id="rule_description" class="form-control" value="{{value}}">
										% else:
										<input type="text" name="rule_description" id="rule_description" class="form-control">
										% end
									</div><br />

								% value = configlist.get('SOURCEIP =')
								<label class="form-label">Source IP-address</label>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										% if value:
										<input type="text" name="source-ip-address" id="source-ip-address" class="form-control" value="{{value}}">
										% else:
										<input type="text" name="source-ip-address" id="source-ip-address" class="form-control">
										% end
									</div><br />
							
								% value = configlist.get('SOURCEPT =')
								<label class="form-label">Source IP-port</label>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										% if value:
										<input type="text" name="source-ip-port" id="source-ip-port" class="form-control" value="{{value}}">
										% else:
										<input type="text" name="source-ip-port" id="source-ip-port" class="form-control">
										% end

									</div><br />

								% value = configlist.get('TARGETIP =')
								<label class="form-label">Target IP-address</label>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										% if value:
										<input type="text" name="target-ip-address" id="target-ip-address" class="form-control" value="{{value}}">
										% else:
										<input type="text" name="target-ip-address" id="target-ip-address" class="form-control">
										% end
									</div><br />

								% value = configlist.get('TARGETPT =')
								<label class="form-label">Target IP-port</label>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										% if value:
										<input type="text" name="target-ip-port" id="target-ip-port" class="form-control" value="{{value}}">
										% else:
										<input type="text" name="target-ip-port" id="target-ip-port" class="form-control">
										% end
									</div><br />

                                % value = configlist.get('PROTOCOL =')
                                % options = ['UDP','TCP']
                                <label class="form-label">Protocol</label>
                                    <div class="input-with-icon  right">                                       
                                        <i class=""></i>
                                        <select name="protocol" id="protocol" class="select2 form-control">
                                        % for option in options:
                                            % if option == value:
                                            <option value="{{option}}" selected>{{option}}</option>
                                            % else:
                                            <option value="{{option}}">{{option}}</option>
                                            % end
                                        % end
                                        % if value == None:
                                        <option value=""  selected>&#32;</option>
                                        % else:
                                        <option value="">&#32;</option>
                                        % end
                                        </select>                              
                                    </div><br />

							</div> <!-- /form-froup -->
						</div> <!-- /col-md-6 -->
						<div class="col-md-6">
								<div class="form-group">

                                % value = configlist.get('LOG =')
                                <label class="form-label">Search in this logfile (LOG)</label>
                                <span class="help">Required</span>
                                    <div class="input-with-icon  right">
                                        <i class=""></i>
                                        % if value:
                                        <input type="text" name="log" id="log" class="form-control" placeholder="full logfile directory path here." value="{{value}}"></input>
                                        % else:
                                        <input type="text" name="log" id="log" class="form-control" placeholder="full log file directory path here."
                                        % end
                                    </div><br />

                                % value = configlist.get('MATCH =')
                                <label class="form-label">Match against these keywords (MATCH)</label>
                                <span class="help">Required</span>
                                    <div class="input-with-icon  right">                                       
                                        <i class=""></i>
                                        % if value:
                                        <input type="text" name="match" id="match" class="form-control" placeholder="example: SOURCEPT, TARGETIP, PROTOCOL" value="{{value}}">
                                        % else:
                                        <input type="text" name="match" id="match" class="form-control" placeholder="example: SOURCEIP, TARGETIP, PROTOCOL">
                                        % end
                                    </div><br />

                                % value = configlist.get('MESSAGE =')
                                <label class="form-label">Search for this error message (MESSAGE)</label>
                                    <div class="input-with-icon  right">                                       
                                        <i class=""></i>
                                        % if value:
                                        <input type="text" name="message" id="message" class="form-control" value="{{value}}">
                                        % else:
                                        <input type="text" name="message" id="message" class="form-control">
                                        % end
                                    </div><br />

                                % operators = ['COUNT <' , 'COUNT <=' , 'COUNT >' , 'COUNT >=' , 'COUNT =']
                                <label class="form-label">Packet count operator (COUNT)</label>
                                <span class="help">Required</span>
                                    <div class="input-with-icon  right">
                                        <div class="radio">
                                            % for operator in operators:
                                                % if configlist.get(operator) != None:
                                                % operator = operator.replace('COUNT ', '')
                                                <input type="radio" name="count_operator" id="{{operator}}" value="{{operator}}" checked="checked">
                                                <label for="{{operator}}">{{operator}}</label>
                                                % else:
                                                % operator = operator.replace('COUNT ', '')
                                                <input type="radio" name="count_operator" id="{{operator}}" value="{{operator}}">
                                                <label for="{{operator}}">{{operator}}</label>
                                                % end
                                            % end
                                        </div>
                                    </div><br />

                                <label class="form-label">Packet count (COUNT)</label>
                                <span class="help">Required</span>
                                    <div class="input-with-icon  right">
                                        <i class=""></i>
                                            % if configlist.get('COUNT <'):
                                            % value = configlist.get('COUNT <')
                                            <input type="text" name="count" id="count" class="form-control" value="{{value}}">
                                            % elif configlist.get('COUNT <='):
                                            % value = configlist.get('COUNT <=')
                                            <input type="text" name="count" id="count" class="form-control" value="{{value}}">
                                            % elif configlist.get('COUNT >'):
                                            % value = configlist.get('COUNT >')
                                            <input type="text" name="count" id="count" class="form-control" value="{{value}}">
                                            % elif configlist.get('COUNT >='):
                                            % value = configlist.get('COUNT >=')
                                            <input type="text" name="count" id="count" class="form-control" value="{{value}}">
                                            % elif configlist.get('COUNT ='):
                                            % value = configlist.get('COUNT =')
                                            <input type="text" name="count" id="count" class="form-control" value="{{value}}">
                                            % else:
                                            <input type="text" name="count" id="count" class="form-control" value="">
                                            % end
                                    </div><br />

								% value = configlist.get('INTERVAL =')
								<label class="form-label">Interval</label>
									<div class="input-with-icon  right">                                       
										<i class=""></i>
										% if value:
										<input type="text" name="interval" id="interval" class="form-control" placeholder="hh:mm:ss" value="{{value}}">
										% else:
										<input type="text" name="interval" id="interval" class="form-control" placeholder="hh:mm:ss">
										% end
									</div><br />

								% value = configlist.get('ACTION =').strip("'")
                                <label class="form-label">Execute script on match (ACTION)</label>
                                <span class="help">Required</span>
                                    <div class="input-with-icon  right">                                       
                                        <i class=""></i>
                                        <select name="action" id="action" class="select2 form-control">

                                        % # This code will read all "action files" from the action directory.
                                        % action_dir_path = config["paths"]["dir_secmon_root"] + 'custom/actions/'
                                        % action_files_array = os.listdir( action_dir_path )

                                        % for item in action_files_array:
                                            % if (item.endswith('.py')) and (item != '__init__.py') and item == value:
                                                <option value="{{item}}" selected>{{item[:-3]}}</option>
                                            % elif (item.endswith('.py')) and (item != '__init__.py'):
                                                <option value="{{item}}">{{item[:-3]}}</option>
                                            % end
                                        % end
                                        </select>                                  
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
