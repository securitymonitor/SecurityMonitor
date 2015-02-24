% rebase('base.tpl', title='Users', url=url)
% import sqlite3

% # For this page we need to request all current users from the database.
% conn = sqlite3.connect(config["paths"]["file_auth_database"])
% c = conn.cursor()

% # Select all users from the database
% c.execute("SELECT ID, Username from secure_login")
    
% # List all users in the variable result
% rows = c.fetchall()
% c.close()

<div class="page-content"> 
  <div class="content">
    <div class="row-fluid">
      <div class="span12">
        <div class="grid simple ">
          <div class="grid-title">
            <h4><span class="semi-bold">Users</span></h4>
          </div>
          <div class="grid-body ">
            <form action="" method="POST">
              <table class="table table-hover table table-striped" id="example3">
                <thead class="cf">
                  <tr>
                    <th style="width:1%">
                      <div class="checkbox check-default ">
                        <input id="checkbox1" type="checkbox" value="1" class="checkall">
                        <label for="checkbox1"></label>
                      </div>
                    </th>
                    <th style="width:24%">Users</th>
                  </tr>
                </thead>
                <tbody>
                  % i = 2
                  % for row in rows:
                  <tr>
                    <td class="v-align-middle">
                      <div class="checkbox check-default">
                        <input type="checkbox" name="chkBox" id="checkbox{{i}}" value="{{row[0]}}">
                        <label for="checkbox{{i}}"></label>
                      </div>
                    </td>
                    <td class="v-align-middle"><span style="color:#505458">{{row[1]}}</span></td>
                  </tr>
                  % i += 1
                  % end
                </tbody>
              </table>
            </form>
            <br />
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
