% rebase('base.tpl', title='Users', url=url)
<div class="page-content"> 
	<div class="content">
		<div class="row-fluid">
			<div class="span12">
				<div class="grid simple ">
					<div class="grid-title">
						<h4><span class="semi-bold">Create Iser</span></h4>
						<div class="tools">
							<a href="javascript:;" class="collapse"></a>
							<a href="javascript:;" class="reload"></a>
							<a href="javascript:;" class="remove"></a>
						</div>
					</div>

					<div class="grid-body ">

				<form id="commentForm" action="/create_user" method="post">
                  <div id="rootwizard" class="col-md-12">
                    <div class="form-wizard-steps">
                      <ul class="wizard-steps">
                        <li class="" data-target="#step1"> <a href="#tab1" data-toggle="tab"> <span class="step">1</span> <span class="title">User information</span> </a> </li>
                        <li data-target="#step2" class=""> <a href="#tab2" data-toggle="tab"> <span class="step">2</span> <span class="title">Rights</span> </a> </li>
                        <li data-target="#step3" class=""> <a href="#tab3" data-toggle="tab"> <span class="step">3</span> <span class="title">Overview</span> </a> </li>
                      </ul>
                      <div class="clearfix"></div>
                    </div>
                    <div class="tab-content transparent">
                      <div class="tab-pane" id="tab1"> <br>
                        <h4 class="semi-bold">Step 1 - <span class="light">User information</span></h4>
                        <br>
                        <div class="row form-row">
                          <div class="col-md-12">
                            <input type="text" placeholder="Username" class="form-control no-boarder " name="new_uname" id="new_uname">
                          </div>
                        </div>
                        <div class="row form-row">
                          <div class="col-md-12">
                            <input type="password" placeholder="Password" class="form-control no-boarder " name="new_passwd" id="new_passwd">
                          </div>
                        </div>
                      </div>
                      <div class="tab-pane" id="tab2"> <br>
                        <h4 class="semi-bold">Step 2 - <span class="light">Rights</span></h4>
                        <br>
                        <div class="row form-row">

						<div class="row-fluid">
		                    <div class="checkbox check-primary">
		                      <input id="check1" type="checkbox" name="check" value="check1" checked="checked" disabled="disabled">
		                      <label for="check1">View rules</label>
		                      <br>
		                      <input id="check2" type="checkbox" name="check" value="check2" checked="checked" disabled="disabled">
		                      <label for="check2">Create new rules</label>
		                      <br>
		                      <input id="check3" type="checkbox" name="check" value="check3" checked="checked" disabled="disabled">
		                      <label for="check3">Remove rules</label>
		                      <br>
		                      <input id="check4" type="checkbox" name="check" value="check4" checked="checked" disabled="disabled">
		                      <label for="check4">View users</label>
		                      <br>
		                      <input id="check5" type="checkbox" name="check" value="check5" checked="checked" disabled="disabled">
		                      <label for="check5">Create new users</label>
		                      <br>
		                      <input id="check6" type="checkbox" name="check" value="check6" checked="checked" disabled="disabled">
		                      <label for="check6">Remove users</label>
		                    </div>
	                  	</div>

                        </div>
                      </div>
                      <div class="tab-pane" id="tab3"> <br>
                        <h4 class="semi-bold">Step 3 - <span class="light">Overview</span></h4>
                        <br>
                   		<pre>
                   		<p>Username: <span id="ShowUsername"></span></p>
          						<p>Password: ***HIDDEN***</p>
          						<p>Rights: All Rights</p>
                      <p><button class="btn btn-info" type="submit">&nbsp;&nbsp;Create user&nbsp;&nbsp;</button></p>
                   		</pre>
                      </div>
                      <ul class=" wizard wizard-actions">
                        <li class="previous first" style="display:none;"><a href="javascript:;" class="btn">&nbsp;&nbsp;First&nbsp;&nbsp;</a></li>
                        <li class="previous"><a href="javascript:;" class="btn">&nbsp;&nbsp;Previous&nbsp;&nbsp;</a></li>
                        <li class="next"><a href="javascript:;" class="btn btn-primary">&nbsp;&nbsp;Next&nbsp;&nbsp;</a></li>
                      </ul>
                    </div>
                  </div>
                </form>


					</div>
				</div>
			</div>
		</div>
	</div>
</div>
