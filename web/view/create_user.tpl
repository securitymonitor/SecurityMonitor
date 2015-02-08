% rebase('base.tpl', title='Users', url=url)
<div class="page-content"> 
	<div class="content">
		<div class="row-fluid">
			<div class="span12">
				<div class="grid simple ">
					<div class="grid-title">
						<h4><span class="semi-bold">Create user</span></h4>
						<div class="tools">
							<a href="javascript:;" class="collapse"></a>
							<a href="javascript:;" class="reload"></a>
							<a href="javascript:;" class="remove"></a>
						</div>
					</div>

					<div class="grid-body ">

				<form id="commentForm" action="/create_user" method="post">

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
        <br>

        <h4 class="semi-bold">Step 2 - <span class="light">Submit</span></h4>
        <br>
        <p><button class="btn btn-info" type="submit">&nbsp;&nbsp;Create user&nbsp;&nbsp;</button></p>
        
        </form>


					</div>
				</div>
			</div>
		</div>
	</div>
</div>
