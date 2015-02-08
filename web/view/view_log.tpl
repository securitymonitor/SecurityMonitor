% rebase('base.tpl', title='Logs', url=url)

<script>
	function goBack() {
		window.history.back()
	}
</script>

<div class="page-content"> 
	<div class="content">
		<div class="row-fluid">
			<div class="span12">
				<div class="grid simple ">
					<div class="grid-body ">



							<div class="form-group">
								<div class="controls">

% # This code block will process single view of a log file							

% if defined('log'):

% # Beceause the webserver logfile (bottle.log) is located in a diffirent dir we've to create this little loop as a fix for that.
% if log == 'bottle.log':
% path = config["paths"]["dir_webserver_log"]
% else:
% path = config["paths"]["dir_secmon_core"]
% end

% with open(path + log) as f:
<h1>{{log[:-4]}}</h1>
<textarea id="text-editor" placeholder="empty" class="form-control" rows="30">
% for line in f:
{{line}}
% end
</textarea><br />
% end
<button class="btn btn-white btn-cons btn-cancel" type="button" onclick="goBack()">Back</button>
% end

% # This code block will process the multi view of a selected log file	

% if defined('form_data'):

% # Beceause the webserver logfile (bottle.log) is located in a diffirent dir we've to create this little loop as a fix for that.
% if form_data == 'bottle.log':
% path = config["paths"]["dir_webserver_log"]
% else:
% path = config["paths"]["dir_secmon_core"]
% end

% for item in form_data:
<h1>{{item[:-4]}}</h1>
<textarea id="text-editor" placeholder="empty" class="form-control" rows="10">

% if item != 'bottle.log':
% path = config["paths"]["dir_secmon_core"]
% with open(path + item) as lines:
% for coll in lines:
{{coll}}
% end
</textarea><br />
% end

% else:
% path = config["paths"]["dir_webserver_log"]
% with open(path + item) as lines:
% for coll in lines:
{{coll}}
% end
</textarea><br />
% end

% end
% end
<button class="btn btn-white btn-cons btn-cancel" type="button" onclick="goBack()">Back</button>
% end


								</div>
							</div>

					</div>
				</div>
			</div>
		</div>
	</div>
</div>