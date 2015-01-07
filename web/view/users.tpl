% rebase('base.tpl', title='Users', url=url)
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
              <a href="/create_user"><button type="button" class="btn btn-primary btn-cons"><i class="fa fa-plus"></i>&nbsp;New user</button></a>
              <button type="submit" class="btn btn-danger btn-cons"><i class="fa fa-trash-o"></i>&nbsp;Delete</button>
              <table class="table table-striped table-flip-scroll cf">
                <thead class="cf">
                  <tr>
                    <th>
                      <div class="checkbox check-default ">
                        <input id="checkbox1" type="checkbox" value="1" class="checkall">
                        <label for="checkbox1"></label>
                      </div>
                    </th>
                    <th>ID</th>
                    <th>Username</th>
                    <th>Password</th>
                  </tr>
                </thead>
                <tbody>
                  % i = 2
                  %for row in rows:
                  <tr>
                    <td>
                      <div class="checkbox check-default">
                        <input type="checkbox" name="chkBox" id="checkbox{{i}}" value="{{row[0]}}">
                        <label for="checkbox{{i}}"></label>
                      </div>
                    </td>
                    % i += 1
                    %for col in row:
                    <td>{{col}}</td>
                    %end
                  </tr>
                  %end
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
