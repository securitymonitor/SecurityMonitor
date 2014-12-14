		<div class="page-content"> 
			<div class="content">

      <div class="row-fluid">
        <div class="span12">
          <div class="grid simple ">
            <div class="grid-title">
              <h4>Security Monitor <span class="semi-bold">Rules</span></h4>
              <div class="tools"> <a href="javascript:;" class="collapse"></a><a href="javascript:;" class="reload"></a> <a href="javascript:;" class="remove"></a> </div>
            </div>
            <div class="grid-body ">
              <table class="table table-hover table-condensed" id="example">
                <thead>
                  <tr>
                    <th style="width:1%"><div class="checkbox check-default" style="margin-right:auto;margin-left:auto;">
                        <input type="checkbox" value="1" id="checkbox1">
                        <label for="checkbox1"></label>
                      </div></th>
                    <th style="width:24%">Rule name</th>
                    <th style="width:24%" data-hide="phone,tablet">Description</th>
                  </tr>
                </thead>
                <tbody>
                	% for item in list_rules:
                		<tr >
                    		<td class="v-align-middle">
                    			<div class="checkbox check-default">
                        		<input type="checkbox" value="3" id="checkbox2">
                        		<label for="checkbox2"></label>
                      			</div>
                      		</td>
                    		<td class="v-align-middle"><a href="/rules/{{item}}">{{item}}</a></td>
                    		<td class="v-align-middle"><span class="muted">TEST</span></td>
                  		</tr>
                	% end	
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
