% rebase('base.tpl', title='Rules', url=url)
% import os
% list_rule_dir = os.listdir(config["paths"]["dir_secmon_rules"])
% i = 2

  <div class="page-content"> 
    <div class="content">
      <div class="row-fluid">
        <div class="span12">
          <div class="grid simple ">
            <div class="grid-title">
              <h4><span class="semi-bold">Rules</span></h4>
            </div>
            <div class="grid-body">
              <form action="/rules" method="POST">
                <table class="table table-hover table table-striped" id="example2">
                  <thead>
                    <tr>
                      <th style="width:1%">
                        <div class="checkbox check-default ">
                          <input id="checkbox1" type="checkbox" value="1" class="checkall">
                          <label for="checkbox1"></label>
                        </div>
                      </th>
                      <th style="width:24%">Rule</th>
                    </tr>
                  </thead>
                  <tbody>
                    % for item in list_rule_dir:
                      % if (item.endswith('.txt')) and (item != 'RuleDefinitionTable.txt'):
                      <tr >
                        <td class="v-align-middle">
                         <div class="checkbox check-default">
                          <input type="checkbox" name="chkBox" id="checkbox{{i}}" value="{{item}}">
                          <label for="checkbox{{i}}"></label>
                        </div>
                        </td>
                        <td class="v-align-middle"><a href="rules/{{item}}"><span style="color:#505458">{{item[:-4]}}</span></a></td>
                      </tr>
                      % i += 1
                      % end
                    % end
                </tbody>
              </table>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>