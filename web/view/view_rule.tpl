% rebase('base.tpl', title='Rules', url=url)
% from math import *
% keys = configlist.keys()
% values = configlist.values()
% a = len(keys) % 2
% b = len(keys) / 2
% c = a + b

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
						

% if defined('configlist'):
<h1>{{rule}}</h1>
<div class="col-md-6">
% i = 0
% for line in configlist:

% if i == c:
						</div>
						<div class="col-md-6">
% end

<div class="form-group">
	<label class="form-label">{{keys[i]}}</label>
	<div class="input-with-icon  right">                                       
		<i class=""></i>
		<input type="text" name="form1Email" id="form1Email" class="form-control" value="{{values[i]}}">                                 
	</div>
</div>

% i += 1
% end
<div class="col-md-12">
<button class="btn btn-info btn-cons btn-cancel" type="button" onclick="goBack()">Back</button>
</div>
% end

% if defined('form_data'):
% for item in form_data:
<h1>{{item}}</h1>
<textarea id="text-editor" placeholder="Log is empty. :(" class="form-control" rows="10">
% with open(config["paths"]["dir_secmon_core"] + item) as lines:
% for coll in lines:
{{coll}}
% end
</textarea><br />
% end
% end
<button class="btn btn-info btn-cons btn-cancel" type="button" onclick="goBack()">Back</button>
% end

						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>