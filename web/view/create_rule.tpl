% rebase('base.tpl', title='Rules', url=url)


<div class="page-content"> 
    <div class="content">
        <div class="row">
            <div class="col-md-12">
                <div class="grid simple ">
                    <div class="grid-body ">
                    <h1>Create new rule</h1>
                        <div class="col-md-6">
                            <div class="form-group">
                                <form action="/create_rule" method="POST">


                                <label class="form-label">Rule name</label>
                                <span class="help">Required</span>
                                    <div class="input-with-icon  right">                                       
                                        <i class=""></i>
                                        <input type="text" name="rule_name" id="rule_name" class="form-control">                                 
                                    </div><br />

                                <label class="form-label">Rule Description</label>
                                <span class="help">Required</span>
                                    <div class="input-with-icon  right">                                       
                                        <i class=""></i>
                                        <input type="text" name="rule_description" id="rule_description" class="form-control">                                 
                                    </div><br />

                                <label class="form-label">Source IP-address</label>
                                    <div class="input-with-icon  right">                                       
                                        <i class=""></i>
                                        <input type="text" name="source-ip-address" id="source-ip-address" class="form-control">                                 
                                    </div><br />
                            
                                <label class="form-label">Source IP-port</label>
                                    <div class="input-with-icon  right">                                       
                                        <i class=""></i>
                                        <input type="text" name="source-ip-port" id="source-ip-port" class="form-control">                                 
                                    </div><br />

                                <label class="form-label">Target IP-address</label>
                                    <div class="input-with-icon  right">                                       
                                        <i class=""></i>
                                        <input type="text" name="target-ip-address" id="target-ip-address" class="form-control">                                 
                                    </div><br />

                                <label class="form-label">Target IP-port</label>
                                    <div class="input-with-icon  right">                                       
                                        <i class=""></i>
                                        <input type="text" name="target-ip-port" id="target-ip-port" class="form-control">                                 
                                    </div><br />

                                <label class="form-label">Protocol</label>
                                    <div class="input-with-icon  right">                                       
                                        <i class=""></i>
                                        <select name="protocol" id="protocol" class="select2 form-control">
                                            <option value="" selected>&#32;</option>
                                            <option value="UDP">UDP</option>
                                            <option value="TCP">TCP</option>
                                        </select>                              
                                    </div><br />


                                </div> <!-- /form-froup -->
                            </div> <!-- /col-md-6 -->
                            <div class="col-md-6">
                                <div class="form-group">

                                <label class="form-label">Search in this logfile (LOG)</label>
                                <span class="help">Required</span>
                                    <div class="input-with-icon  right">                                       
                                        <i class=""></i>
                                        <input type="text" name="log" id="log" class="form-control" placeholder="full logfile directory path here.">
                                    </div><br />

                                <label class="form-label">Match against these keywords (MATCH)</label>
                                <span class="help">Required</span>
                                    <div class="input-with-icon  right">                                       
                                        <i class=""></i>
                                        <input type="text" name="match" id="match" class="form-control" placeholder="SOURCEIP, TARGETIP, PROTOCOL">                                 
                                    </div><br />

                                <label class="form-label">Search for error message in logfile (MESSAGE)</label>
                                    <div class="input-with-icon  right">                                       
                                        <i class=""></i>
                                        <input type="text" name="message" id="message" class="form-control">                                 
                                    </div><br />

                                <label class="form-label">Package count operator (COUNT)</label>
                                <span class="help">Required</span>
                                    <div class="input-with-icon  right">
                                        <div class="radio">
                                            <input type="radio" name="count_operator" id="<" value="<" checked="checked">
                                            <label for="<">&#60;</label>
                                            <input type="radio" name="count_operator" id="<=" value="<=">
                                            <label for="<=">&#60;&#61;</label>
                                            <input type="radio" name="count_operator" id=">" value=">">
                                            <label for=">">&#62;</label>
                                            <input type="radio" name="count_operator" id=">=" value=">=">
                                            <label for=">=">&#62;&#61;</label>
                                            <input type="radio" name="count_operator" id="=" value="=">
                                            <label for="=">&#61;</label>
                                        </div>
                                    </div><br />

                                <label class="form-label">Package Count (COUNT)</label>
                                <span class="help">Required</span>
                                    <div class="input-with-icon  right">                                       
                                        <i class=""></i>
                                        <input type="text" name="count" id="count" class="form-control">                                 
                                    </div><br />

                                <label class="form-label">Interval</label>
                                    <div class="input-with-icon  right">                                       
                                        <i class=""></i>
                                        <input type="text" name="interval" id="interval" class="form-control" placeholder="hh:mm:ss">                                 
                                    </div><br />

                                <label class="form-label">Execute this script on match (ACTION)</label>
                                <span class="help">Required</span>
                                    <div class="input-with-icon  right">                                       
                                        <i class=""></i>
                                        <select name="action" id="action" class="select2 form-control">

                                        % # This script will read all action python files from the action directory.
                                        % import os
                                        % action_dir_path = config["paths"]["dir_secmon_root"] + 'custom/actions/'
                                        % action_files_array = os.listdir( action_dir_path )
                                        % for item in action_files_array:
                                            % if (item.endswith('.py')) and (item != '__init__.py'):
                                            <option value="{{item}}">{{item}}</option>
                                            % end
                                        % end

                                        </select>                                  
                                    </div><br />

                                    <button class="btn btn-info btn-cons btn-cancel" type="submit">Create</button>
                                    <button class="btn btn-white btn-cons btn-cancel" type="button" onclick="goBack()">Back</button>


                                </form>
                            </div> <!-- /form-froup -->
                        </div> <!-- /col-md-6 -->
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
