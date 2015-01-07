<%

include('header.tpl')

include('{{block}}')

if page == 'Dashboard':
	include('block_dashboard.tpl')
elif page == 'Settings':
	include('block_settings.tpl')
elif page == 'Rules':
	include('block_rules.tpl')
elif page == 'Debug':
	include('block_debug.tpl')
elif page == 'Users':
	include('block_users.tpl')
elif page == rule:
	include('block_rule_manage.tpl')
else:
	include('404.tpl')
end

include('footer.tpl')

%>