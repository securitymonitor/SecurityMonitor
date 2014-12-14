<%

include('block_navigation.tpl')

if page == 'Dashboard':
	include('block_dashboard.tpl')
elif page == 'Settings':
	include('block_settings.tpl')
elif page == 'Rules':
	include('block_rules.tpl')
elif page == 'Debug':
	include('block_debug.tpl')
elif page == rule:
	include('block_rule_manage.tpl')
else:
	include('404.tpl')
end

include('block_footer.tpl')

%>