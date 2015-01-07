% rebase('base.tpl', title='Rules', url=url)
<div class="page-content"> 
  <div class="content">
    <div class="row-fluid">
      <div class="span12">
        <div class="grid simple ">
          <div class="grid-title">
            <h4><span class="semi-bold">Rules</span></h4>
          </div>
          <div class="grid-body ">

            <table class="table table-hover table-condensed" id="example3">
              <thead>
                <tr>
                  <th style="width:1%">
                    <div class="checkbox check-default ">
                      <input id="checkbox1" type="checkbox" value="1" class="checkall">
                      <label for="checkbox1"></label>
                    </div>
                  </th>
                  <th style="width:24%">Rule name</th>
                </tr>
              </thead>
              <tbody>
                % import os
                % list_rule_dir = os.listdir(config["paths"]["dir_secmon_rules"])
                % i = 2
                % for item in list_rule_dir:
                <tr >
                  <td class="v-align-middle">
                   <div class="checkbox check-default">
                    <input type="checkbox" value="3" id="checkbox{{i}}">
                    <label for="checkbox{{i}}"></label>
                  </div>
                </td>
                <td class="v-align-middle">{{item}}</td>
              </tr>
              % i += 1
              % end	
            </tbody>
          </table>
          
        </div>
      </div>