% rebase('base.tpl', title='Users', url=url)
<div class="page-content"> 
	<div class="content">
		<div class="row-fluid">
			<div class="span12">
				<div class="grid simple ">
					<div class="grid-body ">
					<form action="/create_user" method="post">

			        <h4 class="light">Please enter <span class="semi-bold">user information.</span></h4>
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
				        <div class="row form-row">
				          <div class="col-md-12">
				            <input type="password" placeholder="Repeat password" class="form-control no-boarder " name="new_passwd_check" id="new_passwd_check">
				          </div>
				        </div>
			        <p><button class="btn btn-info" type="submit" name="submit_btn" value="create">&nbsp;&nbsp;Create user&nbsp;&nbsp;</button></p>
			        
			        </form>


					</div>
				</div>
			</div>
		</div>
	</div>
</div>
