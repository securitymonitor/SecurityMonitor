% rebase('base.tpl', title='Rules', url=url, rule=rule)
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

						<!-- Rule Title -->
						% if defined('rule'):
						<h1>{{rule}}</h1>
						% end

						<form action="/rules/{{rule}}" method="post">
							<div class="form-group">
								<div class="controls">
									<label class="form-label">Rule content</label>
									<textarea placeholder="Rule content will be loaded here.." class="form-control" rows="30" name="content" id="content">{{rule_content}</textarea><br />

									<button class="btn btn-success btn-cons btn-add" type="submit">Save</button>
									<button class="btn btn-white btn-cons btn-cancel" type="button" onclick="goBack()">Cancel</button>
								</div>
							</div>
						</form>

					</div>
				</div>
			</div>
		</div>
	</div>
</div>