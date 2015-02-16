% rebase('base.tpl', title='Users', url=url)
% import sqlite3

<div class="page-content"> 
	<div class="content">
		<div class="row-fluid">
			<div class="span12">
				<div class="grid simple ">
					<div class="grid-body ">
					<form action="/create_user" method="post">

			        % # Single user password change
			        % if defined('user'):

			        	<h4 class="light">Choose a <span class="semi-bold">new password.</span></h4>
			        	<br>
				        <div class="row form-row">
				          <div class="col-md-12">
				            <input type="test" placeholder="{{user}}" class="form-control no-boarder" name="username" id="{{user}}" value="{{user}}" disabled>
				          </div>
				        </div>
				        <div class="row form-row">
				          <div class="col-md-12">
				            <input type="password" placeholder="New password" class="form-control no-boarder" name="updated_passwd" id="updated_passwd">
				          </div>
				        </div>
				        <div class="row form-row">
				          <div class="col-md-12">
				            <input type="password" placeholder="Repeat new password" class="form-control no-boarder " name="updated_passwd_check" id="updated_passwd_check">
				          </div>
				        </div>
			        	<p><button class="btn btn-info" type="submit">&nbsp;&nbsp;Change password&nbsp;&nbsp;</button></p>

			        % end

			        % # Multiple users password change
			        % if defined('form_data'):

						<h4 class="light">Choose <span class="semi-bold">new passwords.</span></h4>

			        % for item in form_data:




					% # For this page we need to request all current users from the database.
					% conn = sqlite3.connect(config["paths"]["file_auth_database"])
					% c = conn.cursor()

					% # Select all users from the database
					% item = c.execute("SELECT Username FROM secure_login WHERE ID = ?", (item))
					    
					% # List all users in the variable result
					% item = c.fetchall()
					% item = str(item)
					% c.close()

			        	<br>
				        <div class="row form-row">
				          <div class="col-md-12">
				            <input type="text" placeholder="{{item[4:-4]}}" class="form-control no-boarder" name="username" id="{{item[4:-4]}}" value="{{item[4:-4]}}" disabled>
				          </div>
				        </div>
				        <div class="row form-row">
				          <div class="col-md-12">
				            <input type="password" placeholder="New password" class="form-control no-boarder" name="updated_passwd" id="updated_passwd">
				          </div>
				        </div>
				        <div class="row form-row">
				          <div class="col-md-12">
				            <input type="password" placeholder="Repeat new password" class="form-control no-boarder " name="updated_passwd_check" id="updated_passwd_check">
				          </div>
				        </div>

					% end

						<p><button class="btn btn-info" type="submit" name="submit_btn" value="modify">&nbsp;&nbsp;Change passwords&nbsp;&nbsp;</button></p>

			        % end

			        </form>

					</div>
				</div>
			</div>
		</div>
	</div>
</div>
