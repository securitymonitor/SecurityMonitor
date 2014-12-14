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
		            	% if defined('rule'):
		            		<h1>{{rule}}</h1>
		            	% end

                      	<div class="form-group">
                        	<label class="form-label">Desctiption</label>
                        	<span class="help">Optional</span>
                        	<div class="controls">
                          		<input type="text" class="form-control"><br />
                        </div>
                        <div class="form-group">
                        	<label class="form-label">Rule content</label>
                        	<div class="controls">
                          		<textarea id="text-editor" placeholder="Enter text ..." class="form-control" rows="25"></textarea><br />
                        </div>
                        <button class="btn btn-success btn-cons btn-add" type="button"><i class="icon-envelope"></i> Save</button>
						<button class="btn btn-white btn-cons btn-cancel" type="button" onclick="goBack()">Cancel</button>

		            </div>
		          </div>
		        </div>
		      </div>